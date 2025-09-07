import os 
import sqlite3
#import json
import random
from flask import Flask, session, render_template, request, g, jsonify

import math


from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
p = os.getenv('secretKey')
app.secret_key = p

@app.route("/")
def home(): 
    return render_template("home.html")



@app.route("/colors", methods=['GET','POST'])
def colors():

    if request.method == 'POST':
        try:
            data = request.get_json()
            color = data.get('color')
            color = color.replace('_', ' ')
                        
            session['selected_color'] = color  
            print("Session color:", color)
            return '', 204
        
        except Exception as e:
            return '', 400

    data = get_db()
    
    try:
    # Process and send all_data
        return render_template("colors.html", all_data= data)
    except Exception as e:
        print("Error:", e)
        return "Internal Server Error", 500 
    
@app.route('/check_color', methods=['POST'])
def check_cclor(): 
    try:
        data = request.get_json()
        input_color = data.get('input_color')       
        session['session_colorinput'] = input_color  
        print("User color:", input_color)
        return '', 204
        
    except Exception as e:
        print('POST error:', e)
        return '', 400


@app.route('/search_color')
def search_color(): 
    color = session.get("session_colorinput")
    print("Session color:", color)
    if not color:
        return "No color selected", 400  
    
    
    db_colors = color_for_search()


    try: 
    
        data = find_closest_colors(color, db_colors, num_results=6)
        clean_data = [item[1] for item in data]
        return render_template("search_color.html", all_data= clean_data)
    
    except Exception as e: 
        print(e)
        return render_template("colors.html", all_data= db_colors)
    



def hex_to_rgb(hex_code):
    """Converts a hex color string to a tuple of RGB values scaled [0–1]."""
    hex_code = hex_code.lstrip('#')
    r = int(hex_code[0:2], 16) / 255.0
    g = int(hex_code[2:4], 16) / 255.0
    b = int(hex_code[4:6], 16) / 255.0
    return (r, g, b)

def rgb_to_xyz(r, g, b):
    """Converts RGB [0–1] to CIE XYZ."""
    # Apply gamma correction (sRGB)
    def gamma_correct(c):
        return ((c / 12.92) if c <= 0.04045 else (((c + 0.055) / 1.055) ** 2.4))
    
    r = gamma_correct(r)
    g = gamma_correct(g)
    b = gamma_correct(b)

    # sRGB to XYZ (D65)
    x = r * 0.4124 + g * 0.3576 + b * 0.1805
    y = r * 0.2126 + g * 0.7152 + b * 0.0722
    z = r * 0.0193 + g * 0.1192 + b * 0.9505
    return (x, y, z)

def xyz_to_lab(x, y, z):
    """Converts XYZ to LAB (CIE 1976)."""
    # D65 reference white
    x /= 0.95047
    y /= 1.00000
    z /= 1.08883

    def f(t):
        return t ** (1/3) if t > 0.008856 else (7.787 * t + 16 / 116)

    fx = f(x)
    fy = f(y)
    fz = f(z)

    l = (116 * fy) - 16
    a = 500 * (fx - fy)
    b = 200 * (fy - fz)
    return (l, a, b)

def hex_to_lab(hex_code):
    """Converts a hex string to LAB color."""
    r, g, b = hex_to_rgb(hex_code)
    x, y, z = rgb_to_xyz(r, g, b)
    return xyz_to_lab(x, y, z)

def delta_e_cie1976(lab1, lab2):
    """Returns the Euclidean distance between two LAB colors."""
    return math.sqrt(
        (lab1[0] - lab2[0]) ** 2 +
        (lab1[1] - lab2[1]) ** 2 +
        (lab1[2] - lab2[2]) ** 2
    )

def find_closest_colors(input_hex, color_db, num_results=6):
    """Returns the N closest colors from color_db to the input color."""
    input_lab = hex_to_lab(input_hex)
    distances = []

    for item in color_db:
        db_lab = hex_to_lab(item['rgb'])
        delta_e = delta_e_cie1976(input_lab, db_lab)
        distances.append((delta_e, item))

    distances.sort(key=lambda x: x[0])  # Sort by smallest distance
    return distances[:num_results]



def color_for_search(): 
    db = getattr(g, '_database', None)
    if db is None: 
        db = g._database = sqlite3.connect('./Colors.db')
    cursor = db.cursor()
    try: 
        cursor.execute("SELECT rgb, name, category FROM colors;")
        rgb_name = cursor.fetchall() 

    except Exception as e: 
        print(e)
        return []

    
    all_data = []

    try: 

        for item in rgb_name: 
            data={}

            
            data['rgb'] = '#{0:06X}'.format(item[0])
            data['name'] = item[1]
            data['category'] = item[2]

            all_data.append(data)

        return all_data
    
    except Exception as e: 
        print(e)
        return []

            


    


def get_db(): 
    db = getattr(g, '_database', None)
    if db is None: 
        db = g._database = sqlite3.connect('./Colors.db')
    cursor = db.cursor()
    cursor.execute("SELECT rgb, name FROM colors;")
    rgb_name = cursor.fetchall() 

    data = {}
    all_data = []

    for item in rgb_name: 
        prefix='#'
        if len(hex(item[0]).lstrip('0x'))<6:
            while  len(prefix+hex(item[0]).lstrip('0x'))<7: 
                prefix += '0'


            data['rgb'] = prefix + hex(item[0]).lstrip('0x')

        else:

            data['rgb'] = '#' + hex(item[0]).lstrip('0x')
            
            name = item[1].split()
            data['name'] = "_".join(name)

            all_data.append(data)
            data={}
        
   
    return all_data



@app.teardown_appcontext
def close_connection(exception): 
    db = getattr(g, '_database', None)
    if db is not None: 
        db.close()
    
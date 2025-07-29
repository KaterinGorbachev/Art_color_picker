import os 
import sqlite3
import random
from flask import Flask, session, render_template, request, g, jsonify
import math
from dotenv import load_dotenv
from werkzeug.exceptions import HTTPException
from flask import abort


load_dotenv()

app = Flask(__name__)
p = os.getenv('secretKey')
app.secret_key = p

class AppError(Exception):
    """Custom exception class for application-specific errors."""
    def __init__(self, message="An internal application error occurred 😔", status_code=500):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP errors"""
    if 400 <= e.code < 500:
        
        return render_template("error.html", error_message=e.description, error_code=e.code, error_name=e.name), e.code
    
    elif e.code >= 500: 
        
        return render_template("500.html", error_message="An internal server error occurred 😔"), 500

    
    return e  


@app.errorhandler(AppError)
def handle_app_error(e): 
    """Handle application errors."""
    
    return render_template("500.html", error_message=e.message), e.status_code


@app.route('/simulate-error')
def simulate_error():
    """Test application errors page"""
    #raise AppError("Simulated failure in the app", status_code=400)

    abort(400)



@app.route("/")
def home(): 
    return render_template("home.html")

@app.route("/about")
def about(): 
    return render_template("about.html")

@app.route("/privacy")
def privacy(): 
    return render_template("privacy.html")

@app.route("/service")
def service(): 
    return render_template("service.html")

@app.route("/load_collection", methods=['POST'])
def load_collection(): 
    try:
        data = request.get_json()
        palettes = data.get('collection')       
        session['session_collection'] = palettes  
        print("Collection:", palettes)
        return '', 204
        
    except Exception as e:
        print('POST error:', e)
        return '', 400


@app.route("/collection")
def collection(): 
    
    pal = session.get('session_collection')
    print("Session collection:", pal)
    if not pal:
        return render_template("collection.html", palettes={})
    
    for i in range(len(pal)): 
        pal[i] = int(pal[i])

    
    all_data = get_collection(pal)


    return render_template("collection.html", palettes=all_data)



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

    try: 
        data = color_for_search()
        
    except Exception as e:
        print("Error:", e)
        return "Internal Server Error", 500 

    
    try:
    
        return render_template("colors.html", all_data= data)
    except Exception as e:
        print("Error:", e)
        return "Internal Server Error", 500 
    


@app.route('/palettes')
def palettes():
    color = session.get('selected_color') 
    print("Session color:", color)
    if not color:
        return "No color selected", 400  

    palettes_num = get_palettes(color)
    data = {}
    palettes_info = pal_colors_info()
    print(palettes_info)
    print(palettes_num)
    for item in palettes_num: 
        data[item] = palettes_info[item]

    
   
    return render_template("palettes.html", palettes=data)


@app.route('/all_palettes')
def all_palettes(): 
    #palettes = get_all_palettes()
    palettes = pal_colors_info()
    print(palettes)
    return render_template("all_palettes.html", palettes=palettes)


@app.route('/random')
def random_palettes(): 
    palettes = pal_colors_info()  
    random_palettes_k = random.choices(list(palettes.keys()), k=5)
    data = {}
    
    for key in random_palettes_k: 
        data[key] = palettes[key]
        


    return render_template("random.html", palettes=data)


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




def get_collection(pal):

    db = getattr(g, '_database', None)

    if db is None: 
        db = g._database = sqlite3.connect('./Colors.db')

    cursor = db.cursor()


    sql="SELECT palletes_has_colors.palletes_number, palletes_has_colors.colors_rgb, colors.name, colors.cmyk, colors.category FROM palletes_has_colors LEFT JOIN colors ON palletes_has_colors.colors_rgb = colors.rgb WHERE palletes_has_colors.palletes_number = ?"

    data=[]

    for num in pal: 
            
        cursor.execute(sql, (num,))
        all_info = cursor.fetchall() 
        
        data.append(all_info)
        #
        #print(data)

        
    palettes_info = {}
    for k in data: 
        plt = k
        for i in plt: 
            p = [i]

            for item in p:
                color_info = {}
                prefix='#'
                if len(hex(item[1]).lstrip('0x'))<6:
                    while  len(prefix+hex(item[1]).lstrip('0x'))<7: 
                        prefix += '0'


                    color_info['rgb'] = prefix + hex(item[1]).lstrip('0x')

                else:

                    color_info['rgb'] = '#' + hex(item[1]).lstrip('0x')
                        
                color_info['name'] = item[2]
                color_info['cmyk'] = item[3]
                color_info['category'] = item[4]
                if item[0] in palettes_info.keys(): 
                    palettes_info[item[0]].append(color_info)

                else: 
                    palettes_info[item[0]] = [color_info]

    return palettes_info



def pal_colors_info(): 

    db = getattr(g, '_database', None)
    

    if db is None: 
        db = g._database = sqlite3.connect('./Colors.db')


    cursor = db.cursor()

    cursor.execute("SELECT palletes_has_colors.palletes_number, palletes_has_colors.colors_rgb, colors.name, colors.cmyk, colors.category FROM palletes_has_colors LEFT JOIN colors ON palletes_has_colors.colors_rgb = colors.rgb;")
    all_info = cursor.fetchall() 
            
    palettes_info = {}

    for item in all_info:
        color_info = {}
        prefix='#'
        if len(hex(item[1]).lstrip('0x'))<6:
            while  len(prefix+hex(item[1]).lstrip('0x'))<7: 
                prefix += '0'


            color_info['rgb'] = prefix + hex(item[1]).lstrip('0x').upper()

        else:

            color_info['rgb'] = '#'+hex(item[1]).lstrip('0x').upper()
                
        color_info['name'] = item[2]
        color_info['cmyk'] = item[3]
        color_info['category'] = item[4]
        if item[0] in palettes_info.keys(): 
            palettes_info[item[0]].append(color_info)

        else: 
            palettes_info[item[0]] = [color_info]

        
    return palettes_info


def get_all_palettes(): 
    
    db = getattr(g, '_database', None)

    if db is None: 
        db = g._database = sqlite3.connect('./Colors.db')

     
    
    cursor = db.cursor()
    try: 
        query = f"SELECT * FROM palletes_has_colors;"
        cursor.execute(query)
                    
        palettes = cursor.fetchall()
        palettes_has_colors = {}

        for item in palettes: 
                
            rgb=item[0]
            prefix='#'
            if len(hex(rgb).lstrip('0x'))<6:
                while  len(prefix+hex(rgb).lstrip('0x'))<7: 
                    prefix += '0'

                rgb = prefix + hex(rgb).lstrip('0x')
            else:

                rgb = prefix + hex(rgb).lstrip('0x')

            color = rgb

            if item[1] in palettes_has_colors.keys(): 
                palettes_has_colors[item[1]].append(color)

            else: 
                palettes_has_colors[item[1]] = [color]

        return palettes_has_colors
        
    except: 
            
        return 'There are no palettes'


    
 
def get_palettes(color): 
    db = getattr(g, '_database', None)
    

    if db is None: 
        db = g._database = sqlite3.connect('./Colors.db')
    cursor = db.cursor()
    try: 
        query = f"SELECT palletes_number FROM palletes_has_colors WHERE colors_rgb = (SELECT rgb FROM colors WHERE name = ?);"
        cursor.execute(query, (color,))
                
        num = cursor.fetchall()
        palettes_num =[]
        for item in num:
            for i in item:
                palettes_num.append(i)

            

        return palettes_num
        
    except Exception as e: 
        print(e)
                
             


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



if __name__ == "__main__":
    app.run(debug=False)
    
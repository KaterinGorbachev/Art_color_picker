import os 
import sqlite3
#import json
import random
from flask import Flask, session, render_template, request, g, jsonify

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
p = os.getenv('secretKey')
app.secret_key = p


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
        return "No color selected", 400  
    
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

    data = get_db()
    
    try:
    # Process and send all_data
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
    
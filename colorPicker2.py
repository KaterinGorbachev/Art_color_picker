import os 
import sqlite3
import json
import random
from flask import Flask, session, render_template, request, g, jsonify, redirect, url_for

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
p = os.getenv('secretKey')
app.secret_key = p


@app.route("/")
def index():
    data = get_db()
    
    
    try:
    # Process and send all_data
        return render_template("index.html", all_data= data)
    except Exception as e:
        print("Error:", e)
        return "Internal Server Error", 500 
    


@app.route('/palettes/<color>')
def palletes():
    try:
        data = request.get_json()
        color = data.get('color')
        print("🟢 Received color:", color)
        color = color.split('_')
        color = " ".join(color)
        print("🟢 Parsed color:", color)
        palettes = get_palettes(color)
        print("🟢 Got palettes:", palletes)

        return render_template("palettes.html", palettes=palettes)
    
    except Exception as e:
        print("❌ Error in /get_palette:", e)
        return jsonify({'error': str(e)}), 500

 

     
    
    
 
def get_palettes(color): 
    db = getattr(g, '_database', None)

    if db is None: 
        db = g._database = sqlite3.connect('./Colors.db')
        cursor = db.cursor()
        try: 
            query = f"SELECT palletes_number FROM palletes_has_colors WHERE colors_rgb = (SELECT rgb FROM colors WHERE name = ?);"
            cursor.execute(query, (color,))
                
            palletes_num = cursor.fetchall()
            palletes = {}

            for num in palletes_num: 
                number = num[0]
                data = []
            
                query = f"SELECT colors_rgb FROM palletes_has_colors WHERE palletes_number = {number};"
                cursor.execute(query)
                colors = cursor.fetchall()
                for item in colors: 
                    rgb = item[0]
                    prefix='#'
                    if len(hex(rgb).lstrip('0x'))<6:
                        while  len(prefix+hex(rgb).lstrip('0x'))<7: 
                            prefix += '0'

                        rgb = prefix + hex(rgb).lstrip('0x')
                    else:

                        rgb = prefix + hex(rgb).lstrip('0x')
                
                    data.append(rgb)  

                palletes[number] = data

            return palletes
        
        except: 
            palletes[0] = '#FFFFFF'
            return palletes






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
    



def get_palettes(color): 
    """ Gets from DB numbers of palettes for a selected color name """
    db = getattr(g, '_database', None)    
    if db is None: 
        db = g._database = sqlite3.connect('./Colors.db')
    cursor = db.cursor()
     
    query = f"SELECT palletes_number FROM palletes_has_colors WHERE colors_rgb = (SELECT rgb FROM colors WHERE name = ?);"
    cursor.execute(query, (color,))
                
    num = cursor.fetchall()
    palettes_num =[]
    for item in num:
        for i in item:
            palettes_num.append(i)

    return palettes_num
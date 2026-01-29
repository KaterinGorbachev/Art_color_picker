'''
Main Flask application module.

Provides routes for viewing, searching, and managing color palettes.
Implements caching, structured error handling, and color distance logic.

Copyright, All rights reserved, Ekaterina Gorbacheva, Valencia, 2025

'''
# =========================
# Standard library imports
# =========================
import os 
import sqlite3
import random
import math
import logging

# =========================
# Third-party imports
# =========================
from flask import Flask, session, render_template, request, g, abort
from dotenv import load_dotenv
from werkzeug.exceptions import HTTPException
from flask_caching import Cache

# =========================
# App configuration
# =========================
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

secretkey = os.getenv('FLASK_SECRET_KEY')
if not secretkey:
    raise RuntimeError("FLASK_SECRET_KEY environment variable is not set")

app.secret_key = secretkey

cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache'})

# =========================
# Custom Exceptions
# =========================
class AppError(Exception):
    '''
    Custom application-level exception.

    Used for controlled application failures.
    Carries a message and an HTTP status code.
    '''

    def __init__(self, message: str, status_code: int = 500):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


# =========================
# Error Handlers
# =========================
@app.errorhandler(HTTPException)
def handle_http_exception(error: HTTPException):
    '''
    Handles HTTP-related exceptions raised by Flask or Werkzeug.
    '''
    logger.error("Application error: %s", error.code)
    if 400 <= error.code < 500:
        return (
            render_template(
                "error.html",
                error_message=error.description,
                error_code=error.code,
                error_name=error.name,
            ),
            error.code,
        )

    return (
        render_template(
            "500.html",
            error_message="An internal server error occurred 😔",
            error_code=error.code,
            error_name=error.name,
        ),
        error.code,
    )


@app.errorhandler(AppError)
def handle_app_error(error: AppError):
    '''
    Handles custom application-level errors.
    '''
    logger.error("Application error: %s", error.message)
    return (
        render_template(
            "500.html",
            error_message=error.message,
            error_code=error.status_code,
            error_name="Application Error",
        ),
        error.status_code,
    )


# =========================
# Database helpers
# =========================

@cache.cached(timeout=3600)
def color_for_search():
    """ Gets from DB info about colors and represents it in a prescribed way """ 
    db = getattr(g, '_database', None)
    if db is None: 
        db = g._database = sqlite3.connect('./Colors.db')
    cursor = db.cursor()
    cursor.execute("SELECT rgb, name, category FROM colors;")
    rgb_name = cursor.fetchall()   
    all_data = []
    for item in rgb_name: 
        data={}
        data['rgb'] = '#{0:06X}'.format(item[0])
        data['name'] = item[1]
        data['category'] = item[2]
        all_data.append(data)
        
    return all_data


@cache.cached(timeout=3600)
def pal_colors_info(): 
    """ Gets info from DB about all palettes with colors names and rgb """
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


def get_collection(pal):
    """ Gets palettes with a specific numbers """  
    all_palettes = pal_colors_info()
    selection = {}
    for item in pal:
        selection[int(item)] = all_palettes[int(item)] 

    return selection

 
def get_palettes(color): 
    """ Gets numbers of palettes for a selected color name """
    all_palettes = pal_colors_info()
    pal_num = all_palettes.keys()
    selection = []
    for k in pal_num: 
        for i in range(len(all_palettes[k])): 
            if all_palettes[k][i]['name'] == color: 
                selection.append(k)

    return selection  
        

@app.teardown_appcontext
def close_connection(exception): 
    '''
    Closes the database connection at the end of the request.
    '''
    db = getattr(g, '_database', None)
    if db is not None: 
        db.close()


# =========================
# Color conversion utilities
# =========================

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
    """Returns 6 closest colors from DB to the input color."""
    input_lab = hex_to_lab(input_hex)
    distances = []

    for item in color_db:
        db_lab = hex_to_lab(item['rgb'])
        delta_e = delta_e_cie1976(input_lab, db_lab)
        distances.append((delta_e, item))

    distances.sort(key=lambda x: x[0])  
    return distances[:num_results]


# =========================
# Routes
# =========================

@app.route('/simulate-error')
def simulate_error():
    """ Test application errors page """
    #raise AppError("Simulated failure in the app", status_code=400)
    abort(508)


@app.route("/")
def home(): 
    """ Renders Home page """
    return render_template("home.html")

@app.route("/about")
def about(): 
    """ Renders About page """
    return render_template("about.html")

@app.route("/privacy")
def privacy(): 
    """ Renders Privacy policies page """
    return render_template("privacy.html")

@app.route("/service")
def service(): 
    """ Renders Service terms page """
    return render_template("service.html")

@app.route("/load_collection", methods=['POST'])
def load_collection(): 
    """ Receives as palettes a JSON playload with a 'collection' key from post_collection.js, that gets LocalStorage with a 'CollectionArtColorPicker' key. Saves palettes for session with 'session_collection' key """
    try:
        data = request.get_json()
        palettes = data.get('collection')       
        session['session_collection'] = palettes          
        return '', 204
        
    except HTTPException:        
        raise


@app.route("/collection")
def collection(): 
    """ Gets 'session_collection' with numbers of collected palettes. If there are no collection - returns empty dictionary.  Otherwise, converts data from pal into integers and passes them to get_collection function, finally renders a collection on a new page in the same window """
    
    pal = session.get('session_collection')
    
    if not pal:
        return render_template("collection.html", palettes={})
    
    for i in range(len(pal)): 
        pal[i] = int(pal[i])
    
    try:
        all_data = get_collection(pal)
        return render_template("collection.html", palettes=all_data)
    
    except Exception as e:
        raise AppError("Could not get collection", 500) from e

@app.route("/colors", methods=['GET','POST'])
def colors():
    """ Colors on the page works like buttons - by clicking on them 'colorId' is collected and passed to 'Palettes' page, wich opens in the same window. """
    if request.method == 'POST':
        try:
            data = request.get_json()
            color = data.get('color')
            color = color.replace('_', ' ')
                        
            session['selected_color'] = color  
            logger.info(f"Session color: {color}")
            return '', 204
        
        except HTTPException:        
            raise

    try: 
        data = color_for_search()
        return render_template("colors.html", all_data= data)
        
    except Exception as e:
        
        raise AppError("Could not get colors", 500) from e


@app.route('/palettes')
def palettes():
    """ Shows palettes for a selected color name. """
    color = session.get('selected_color') 
    logger.info(f"Session color: {color}")
    if not color:
        abort(400)
        
    try: 
        palettes_num = get_palettes(color)
        
    
        all_data = get_collection(palettes_num)
        return render_template("palettes.html", palettes=all_data)
    
    except Exception as e:
        
        raise AppError("Could not get collection", 500) from e


@app.route('/all_palettes')
def all_palettes(): 
    """ Returns in the same window all palettes from DB """
    try: 
        palettes = pal_colors_info()    
        return render_template("all_palettes.html", palettes=palettes)
    
    except Exception as e:
        
        raise AppError("Could not get collection", 500) from e



@app.route('/random')
def random_palettes(): 
    """ Returns in the same window 5 random palettes from DB """
    try: 
        palettes = pal_colors_info()  
        random_palettes_k = random.choices(list(palettes.keys()), k=5)
        data = {}
        for key in random_palettes_k: 
            data[key] = palettes[key]
        return render_template("random.html", palettes=data)
        
    except Exception as e:
        
        raise AppError("Could not get palettes", 500) from e


@app.route('/check_color', methods=['POST'])
def check_color(): 
    """ Gets from search_color.js a user input (input was verified on a front)"""
    try:
        data = request.get_json()
        input_color = data.get('input_color')       
        session['session_colorinput'] = input_color  
        logger.info(f"User color: {input_color}")
        return '', 204
        
    except HTTPException:        
        raise


@app.route('/search_color')
def search_color(): 
    """ From session gets 'session_colorinput' """
    color = session.get("session_colorinput")
    logger.info(f"Session color: {color}")
    if not color:
        abort(400)
    
    
    try: 
        db_colors = color_for_search()
        if color[0] == '#':
            """ Checks for 6 similar colors if was hex color number given """
            data = find_closest_colors(color, db_colors, num_results=6)
            clean_data = [item[1] for item in data]
        else:
            """ Checks for colors that contain given word"""
            clean_data = []
            for i in db_colors: 
                if color.lower() in i['name'].lower(): 
                    clean_data.append(i)

                
        return render_template("search_color.html", all_data=clean_data)

    except Exception as e:
        
        raise AppError("Could not find such colors", 500) from e

@app.route('/healthz')
def healthz(): 
    return 'OK', 200


if __name__ == "__main__":
    app.run(debug=True)
    

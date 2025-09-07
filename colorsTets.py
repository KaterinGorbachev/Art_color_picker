
import sqlite3
import random


def get_db(): 



    
    db =  sqlite3.connect('./Colors.db')
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
            
        data['name'] = item[1]
        all_data.append(data)
        data={}
        
        
       
         


    return all_data


""" palletes = []
for i in range(1, 349): 
    n = (i,)
    palletes.append(n)

print(palletes) """



def get_all_palettes(): 
    

     
    db  = sqlite3.connect('./Colors.db')
    cursor = db.cursor()
    try: 
        query = f"SELECT * FROM palletes_has_colors;"
        cursor.execute(query)
                
        palettes = cursor.fetchall()
        palettes_has_colors = {}

        for item in palettes: 
            num = item[1]
            color=item[0]

            if item[1] in palettes_has_colors.keys(): 
                palettes_has_colors[item[1]].append(color)

            else: 
                palettes_has_colors[item[1]] = [color]

            

            
            
            
            
            
                
        return palettes_has_colors
        
    except: 
        
        return 'error'

##print(random.choices(list(get_all_palettes().keys()), k=5))

""" palettes = get_all_palettes()   
random_palettes_k = random.choices(list(palettes.keys()), k=5)
data = {}
    
for key in random_palettes_k: 
    data[key] = palettes[key]

print(data) """


def pal_colors_info(): 


    db =  sqlite3.connect('./Colors.db')
    cursor = db.cursor()


    cursor.execute("SELECT palletes_has_colors.palletes_number, palletes_has_colors.colors_rgb, colors.name, colors.cmyk, colors.category FROM palletes_has_colors LEFT JOIN colors ON palletes_has_colors.colors_rgb = colors.rgb;")
    all_info = cursor.fetchall() 
    #print(all_info)

    
    palettes_info = {}

    for item in all_info:
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


   
#pal_colors_info()

def random_palettes(): 
    palettes = pal_colors_info()   
    random_palettes_k = random.choices(list(palettes.keys()), k=5)
    data = {}
    
    for key in random_palettes_k: 
        data[key] = palettes[key]
        


    print(data) 

        
#random_palettes()    


def get_collection(pal): 
    db =  sqlite3.connect('./Colors.db')
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


""" pal = [46, 2, 3]
get_collection(pal) """


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

print(get_palettes('Vinaceous Tawny'))

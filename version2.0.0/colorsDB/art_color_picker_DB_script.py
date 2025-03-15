import sqlite3

my_con = sqlite3.connect('art_color_picker_BD_1')

my_pointer = my_con.cursor()

print('Conectado a la base de datos art_color_picker_BD_1')










#query = 'CREATE TABLE colors( rgb INTEGER UNSIGNED NOT NULL PRIMARY KEY, name VARCHAR(100) NOT NULL, cmyk TEXT)'
#my_pointer.execute(query)
#print("Creada nueva tabla")
#query = 'ALTER TABLE colors ADD COLUMN category VARCHAR(100)'
#my_pointer.execute(query)

###Update a specific column 
#query = "UPDATE colors SET category = 'red-violet' WHERE rgb = 16757744"    
#my_pointer.execute(query)
#my_con.commit()

'''
colors = [(0xFBE6A0, "Naples Yellow", "{'C':2, 'M':7, 'Y':44, 'K':0}" ), 
          (0xF15A30, "Peach Red", "{'C':0, 'M':80, 'Y':90, 'K':0}"),
          (0x112F2C, "Deep Slate Green", "{'C':80, 'M':50, 'Y':60, 'K':70}", ), 
          (0xE2B540, "Yellow Ocher", "{'C':12, 'M':28, 'Y':88, 'K':0}" ) ]     

query = "INSERT INTO colors VALUES(?, ?, ?, NULL)" 
my_pointer.executemany(query, colors)
my_con.commit()


'''



####(0x, "", "{'C':, 'M':, 'Y':, 'K':}", "" ),

'''
try:

    ###### red-violet colors

    #colors = [(0xFFB3F0, 'Hermosa Pink', "{'C':0, 'M':30, 'Y':6, 'K':0}" )]
    colors = [(0xFFA6D9, 'Corinthian Pink', "{'C':0, 'M':35, 'Y':15, 'K':0}", 'red-violet' ), 
              (0xE6ADCF, 'Cameo Pink', "{'C':10, 'M':32, 'Y':19, 'K':0}", 'red-violet' ),
              (0xD1B0B3, 'Fawn', "{'C':18, 'M':31, 'Y':30, 'K':0}", 'red-violet' ),
              (0xB08699, 'Light Brown Drab', "{'C':8, 'M':30, 'Y':20, 'K':25}", 'red-violet' ),
              (0xFF7399, 'Coral Red', "{'C':0, 'M':55, 'Y':40, 'K':0}", 'red-violet' ),
              (0xFF788C, 'Fresh Color', "{'C':0, 'M':53, 'Y':45, 'K':0}", 'red-violet' ),
              (0xFF616B, 'Grenadine Pink', "{'C':0, 'M':62, 'Y':58, 'K':0}", 'red-violet' ),
              (0xFF5EC4, 'Eosine Pink', "{'C':0, 'M':63, 'Y':23, 'K':0}", 'red-violet' ),
              (0xFF4DC9, 'Spinel Red', "{'C':0, 'M':70, 'Y':21, 'K':0}", 'red-violet' ),
              (0xD94D99, 'Old Rose', "{'C':15, 'M':70, 'Y':40, 'K':0}", 'red-violet' ),
              (0xD15E00, 'Eugenia Red', "{'C':7, 'M':76, 'Y':60, 'K':0}", 'red-violet' ),
              (0xB85E00, 'Raw Sienna', "{'C':18, 'M':58, 'Y':100, 'K':12}", 'red-violet' ),
              (0xC74300, 'Vinaceous Tawny', "{'C':17, 'M':72, 'Y':100, 'K':6}", 'red-violet' ),
              (0xFA2B00, 'Jasper Red', "{'C':2, 'M':83, 'Y':100, 'K':0}", 'red-violet' ),
              (0xF20000, 'Spectrum Red', "{'C':5, 'M':100, 'Y':100, 'K':0}", 'red-violet' ),
              (0xE81900, 'Red Orange', "{'C':9, 'M':90, 'Y':100, 'K':0}", 'red-violet' ),
              (0xC9303E, 'Etruscan Red', "{'C':16, 'M':80, 'Y':74, 'K':6}", 'red-violet' ),
              (0xA93400, 'Burnt Sienna', "{'C':22, 'M':76, 'Y':100, 'K':15}", 'red-violet' ),
              (0xA7374B, 'Ocher Red', "{'C':18, 'M':73, 'Y':63, 'K':20}", 'red-violet' ),
              (0xD50C42, 'Scarlet', "{'C':10, 'M':95, 'Y':72, 'K':7}", 'red-violet' ),
              (0xD60036, 'Carmine', "{'C':0, 'M':100, 'Y':75, 'K':16}", 'red-violet' ),
              (0xCC1A97, 'Indian Lake', "{'C':12, 'M':89, 'Y':35, 'K':9}", 'red-violet' ),
              (0xB319AB, 'Rosolanc Purple', "{'C':30, 'M':90, 'Y':33, 'K':0}", 'red-violet' ),
              (0xB90078, 'Pomegranate Purple', "{'C':23, 'M':100, 'Y':50, 'K':6}", 'red-violet' ),
              (0x9E194D, 'Hydrangea Red', "{'C':38, 'M':90, 'Y':70, 'K':0}", 'red-violet' ),
              (0xA32100, 'Brick Red', "{'C':22, 'M':84, 'Y':100, 'K':18}", 'red-violet' ),
              (0xA10B2B, 'Carmine Red', "{'C':25, 'M':95, 'Y':80, 'K':16}", 'red-violet' ),
              (0xA90636, 'Pompeian Red', "{'C':18, 'M':97, 'Y':74, 'K':19}", 'red-violet' ),
              (0xA10045, 'Red', "{'C':30, 'M':100, 'Y':70, 'K':10}", 'red-violet' ),
              (0x6C2B11, 'Brown', "{'C':35, 'M':74, 'Y':90, 'K':35}", 'red-violet' ),
              (0x681916, "Hay's Russet", "{'C':37, 'M':85, 'Y':87, 'K':35}", 'red-violet' ),
              (0x740909, 'Vandyke Red', "{'C':32, 'M':95, 'Y':95, 'K':33}", 'red-violet' ),
              (0x6F0043, 'Pansy Purple', "{'C':34, 'M':100, 'Y':60, 'K':34}", 'red-violet' ),
              (0x730F1F, 'Pale Burnt Lake', "{'C':25, 'M':90, 'Y':80, 'K':40}", 'red-violet' ),
              (0x3D0079, 'Violet Red', "{'C':75, 'M':100, 'Y':50, 'K':5}", 'red-violet' ),
              (0x5C2C45, 'Vistoris lake', "{'C':40, 'M':71, 'Y':55, 'K':40}", 'red-violet' ),
              

              
              
              
              ]
    query = "INSERT INTO colors VALUES(?, ?, ?,?)"    
    my_pointer.executemany(query, colors)
    my_con.commit()


except sqlite3.IntegrityError:
    print("Clave duplicada")

'''



#query = 'CREATE TABLE palletes( number INTEGER UNSIGNED NOT NULL PRIMARY KEY)'
#my_pointer.execute(query)
#print("Creada nueva tabla")
'''
try: 
    palletes = [(14,),(115,),(166,),(325,)]
    query = 'INSERT INTO palletes VALUES(?)'
    my_pointer.executemany(query, palletes)
    my_con.commit()
    print("Palleta añadida")

except sqlite3.IntegrityError:
    print("Clave duplicada")   



'''

#query = 'CREATE TABLE palletes_has_colors( colors_rgb INTEGER UNSIGNED NOT NULL, palletes_number INTEGER UNSIGNED NOT NULL, position SMALLINT UNSIGNED NOT NULL, FOREIGN KEY (palletes_number) REFERENCES palletes(number), FOREIGN KEY (colors_rgb) REFERENCES colors(rgb))'
#my_pointer.execute(query)
#print("Creada nueva tabla")

'''
palletes_has_colors = [(0xFF4DC9, 14, 1), (0xFBE6A0, 14, 2), 
                       (0xFBE6A0, 115, 1), (0xF15A30, 115, 2), 
                       (0xFF616B, 166, 1), (0xFBE6A0, 166, 2), (0x112F2C, 166, 3), 
                       (0xD15E00, 325, 1), (0xFBE6A0, 325, 2), (0x112F2C, 325, 4), (0xE2B540, 325, 3) ]
    
query = "INSERT INTO palletes_has_colors VALUES(?,?,?)"
my_pointer.executemany(query, palletes_has_colors)
my_con.commit()

'''


#query = 'CREATE TABLE user( id_user INTEGER PRIMARY KEY AUTOINCREMENT)'
#my_pointer.execute(query)
#print("Creada nueva tabla")
#query = 'ALTER TABLE user ADD COLUMN name VARCHAR(25)'
#query = "INSERT INTO user(id_user) VALUES(NULL)"
#query = "UPDATE user SET name = 'test'" 
#my_pointer.execute(query)
#my_con.commit()




#query = 'CREATE TABLE collection( palletes_number INTEGER UNSIGNED NOT NULL, user_id_user INT UNSIGNED NOT NULL, PRIMARY KEY (palletes_number, user_id_user), FOREIGN KEY (palletes_number) REFERENCES palletes (number), FOREIGN KEY (user_id_user) REFERENCES user (id_user))'
#my_pointer.execute(query)
#print("Creada nueva tabla")

#collection = [(115, 1), (14,2)]

#query = "INSERT INTO collection VALUES(?,?)" 
#my_pointer.executemany(query, collection)
#my_con.commit()






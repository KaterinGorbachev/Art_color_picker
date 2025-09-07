import sqlite3

bd_name = 'Colors.db'

my_con = sqlite3.connect(bd_name)

my_pointer = my_con.cursor()

print(f'Conectado a la base de datos {bd_name}')


query = 'CREATE TABLE category( id INTEGER UNSIGNED PRIMARY KEY NOT NULL, name VARCHAR(100) NOT NULL);'
my_pointer.execute(query)
my_con.commit()
print("Creada nueva tabla")
 #####create a table with colors

categories = [
    (1, "red-violet"), (2, "yellow-red"), (3, "yellow-green"), (4, "blue-green"), (5, "blue-violet"), (6, "white-black")
]
query = "INSERT INTO category VALUES(?, ?)"    
my_pointer.executemany(query, categories)
my_con.commit()
print('Insertado correcto')


query = 'CREATE TABLE colors( rgb INTEGER UNSIGNED PRIMARY KEY NOT NULL, name VARCHAR(100) NOT NULL, cmyk TEXT, category INTEGER UNSIGNED, FOREIGN KEY (category) REFERENCES category(id));'
my_pointer.execute(query)
my_con.commit()
print("Creada nueva tabla")

###### red-violet colors  =1
try:

       
    colors = [(0xFFB3F0, 'Hermosa Pink', "{'C':0, 'M':30, 'Y':6, 'K':0}", 1),
              (0xFFA6D9, 'Corinthian Pink', "{'C':0, 'M':35, 'Y':15, 'K':0}", 1 ), 
              (0xE6ADCF, 'Cameo Pink', "{'C':10, 'M':32, 'Y':19, 'K':0}", 1 ),
              (0xD1B0B3, 'Fawn', "{'C':18, 'M':31, 'Y':30, 'K':0}", 1 ),
              (0xB08699, 'Light Brown Drab', "{'C':8, 'M':30, 'Y':20, 'K':25}", 1 ),
              (0xFF7399, 'Coral Red', "{'C':0, 'M':55, 'Y':40, 'K':0}", 1 ),
              (0xFF788C, 'Fresh Color', "{'C':0, 'M':53, 'Y':45, 'K':0}", 1 ),
              (0xFF616B, 'Grenadine Pink', "{'C':0, 'M':62, 'Y':58, 'K':0}", 1 ),
              (0xFF5EC4, 'Eosine Pink', "{'C':0, 'M':63, 'Y':23, 'K':0}", 1 ),
              (0xFF4DC9, 'Spinel Red', "{'C':0, 'M':70, 'Y':21, 'K':0}", 1 ),
              (0xD94D99, 'Old Rose', "{'C':15, 'M':70, 'Y':40, 'K':0}", 1 ),
              (0xD15E00, 'Eugenia Red', "{'C':7, 'M':76, 'Y':60, 'K':0}", 1 ),
              (0xB85E00, 'Raw Sienna', "{'C':18, 'M':58, 'Y':100, 'K':12}", 1 ),
              (0xC74300, 'Vinaceous Tawny', "{'C':17, 'M':72, 'Y':100, 'K':6}", 1 ),
              (0xFA2B00, 'Jasper Red', "{'C':2, 'M':83, 'Y':100, 'K':0}", 1),
              (0xF20000, 'Spectrum Red', "{'C':5, 'M':100, 'Y':100, 'K':0}", 1 ),
              (0xE81900, 'Red Orange', "{'C':9, 'M':90, 'Y':100, 'K':0}", 1 ),
              (0xC9303E, 'Etruscan Red', "{'C':16, 'M':80, 'Y':74, 'K':6}", 1 ),
              (0xA93400, 'Burnt Sienna', "{'C':22, 'M':76, 'Y':100, 'K':15}", 1 ),
              (0xA7374B, 'Ocher Red', "{'C':18, 'M':73, 'Y':63, 'K':20}", 1 ),
              (0xD50C42, 'Scarlet', "{'C':10, 'M':95, 'Y':72, 'K':7}", 1 ),
              (0xD60036, 'Carmine', "{'C':0, 'M':100, 'Y':75, 'K':16}", 1 ),
              (0xCC1A97, 'Indian Lake', "{'C':12, 'M':89, 'Y':35, 'K':9}", 1 ),
              (0xB319AB, 'Rosolanc Purple', "{'C':30, 'M':90, 'Y':33, 'K':0}", 1 ),
              (0xB90078, 'Pomegranate Purple', "{'C':23, 'M':100, 'Y':50, 'K':6}", 1 ),
              (0x9E194D, 'Hydrangea Red', "{'C':38, 'M':90, 'Y':70, 'K':0}", 1 ),
              (0xA32100, 'Brick Red', "{'C':22, 'M':84, 'Y':100, 'K':18}", 1 ),
              (0xA10B2B, 'Carmine Red', "{'C':25, 'M':95, 'Y':80, 'K':16}", 1 ),
              (0xA90636, 'Pompeian Red', "{'C':18, 'M':97, 'Y':74, 'K':19}", 1 ),
              (0xA10045, 'Red', "{'C':30, 'M':100, 'Y':70, 'K':10}", 1 ),
              (0x6C2B11, 'Brown', "{'C':35, 'M':74, 'Y':90, 'K':35}", 1 ),
              (0x681916, "Hay's Russet", "{'C':37, 'M':85, 'Y':87, 'K':35}", 1 ),
              (0x740909, 'Vandyke Red', "{'C':32, 'M':95, 'Y':95, 'K':33}", 1 ),
              (0x6F0043, 'Pansy Purple', "{'C':34, 'M':100, 'Y':60, 'K':34}", 1 ),
              (0x730F1F, 'Pale Burnt Lake', "{'C':25, 'M':90, 'Y':80, 'K':40}", 1 ),
              (0x3D0079, 'Violet Red', "{'C':75, 'M':100, 'Y':50, 'K':5}", 1 ),
              (0x5C2C45, 'Vistoris Lake', "{'C':40, 'M':71, 'Y':55, 'K':40}", 1 ),
                                    
              
              ]
    query = "INSERT INTO colors VALUES(?, ?, ?,?)"    
    my_pointer.executemany(query, colors)
    my_con.commit()


except sqlite3.IntegrityError:
    print("Clave duplicada")


###### yellow-red colors  2
try:

       
    colors = [(0xF5F5B8, 'Sulphur Yellow', "{'C':4, 'M':4, 'Y':28, 'K':0}", 2),
              (0xFFF59E, 'Pale Lemon Yellow', "{'C':0, 'M':4, 'Y':38, 'K':0}", 2 ),
              (0xFAED8F, "Naples Yellow", "{'C':2, 'M':7, 'Y':44, 'K':0}", 2 ),
              (0xEBD999, "Ivory Buff", "{'C':8, 'M':15, 'Y':40, 'K':0}", 2 ),
              (0xFFCFC4, "Seashell Pink", "{'C':0, 'M':19, 'Y':23, 'K':0}", 2 ),
              (0xFFBF99, "Light Pinkish Cinnamon", "{'C':0, 'M':25, 'Y':40, 'K':0}", 2 ),
              (0xF2AD78, "Pinkish Cinnamon", "{'C':5, 'M':32, 'Y':53, 'K':0}", 2 ),
              (0xFFBF6E, "Cinnamon Buff", "{'C':0, 'M':25, 'Y':57, 'K':0}", 2 ),
              (0xFFB852, "Cream Yellow", "{'C':0, 'M':28, 'Y':68, 'K':0}", 2 ),
              (0xFA9442, "Golden Yellow", "{'C':2, 'M':42, 'Y':74, 'K':0}", 2 ),
              (0xF59994, "Vinaceous Cinnamon", "{'C':4, 'M':40, 'Y':42, 'K':0}", 2 ),
              (0xD99E73, "Ochraceous Salmon", "{'C':15, 'M':38, 'Y':55, 'K':0}", 2 ),
              (0xC3A55C, "Isabella Color", "{'C':15, 'M':28, 'Y':60, 'K':10}", 2 ),
              (0xC2975A, "Maple", "{'C':5, 'M':26, 'Y':56, 'K':20}", 2 ),
              (0xBCD382, "Olive Buff", "{'C':16, 'M':6, 'Y':42, 'K':12}", 2 ),
              (0xC0B490, "Ecru", "{'C':20, 'M':25, 'Y':40, 'K':6}", 2 ),
              (0xFFFF00, "Yellow", "{'C':0, 'M':0, 'Y':100, 'K':0}", 2 ),
              (0xF2FF26, "Lemon Yellow", "{'C':5, 'M':0, 'Y':85, 'K':0}", 2 ),
              (0xFFE600, "Apricot Yellow", "{'C':0, 'M':10, 'Y':100, 'K':0}", 2 ),
              (0xC4BF33, "Pyrite Yellow", "{'C':23, 'M':25, 'Y':80, 'K':0}", 2 ),
              (0xD1BD19, "Olive Ocher", "{'C':18, 'M':26, 'Y':90, 'K':0}", 2 ),
              (0xE0B81F, "Yellow Ocher", "{'C':12, 'M':28, 'Y':88, 'K':0}", 2 ),
              (0xFFAB00, "Orange Yellow", "{'C':0, 'M':33, 'Y':100, 'K':0}", 2 ),
              (0xFF8C00, "Yellow Orange", "{'C':0, 'M':45, 'Y':100, 'K':0}", 2 ),
              (0xFF7340, "Apricot Orange", "{'C':0, 'M':55, 'Y':75, 'K':0}", 2 ),
              (0xFF5200, "Orange", "{'C':0, 'M':68, 'Y':100, 'K':0}", 2 ),
              (0xFF3319, "Peach Red", "{'C':0, 'M':80, 'Y':90, 'K':0}", 2 ),
              (0xDE4500, "English Red", "{'C':13, 'M':73, 'Y':100, 'K':0}", 2 ),
              (0xC2612C, "Cinnamon Rufous", "{'C':20, 'M':60, 'Y':82, 'K':5}", 2 ),
              (0xC05200, "Orange Rufous", "{'C':18, 'M':65, 'Y':100, 'K':8}", 2 ),
              (0xBAA600, "Sulphine Yellow", "{'C':24, 'M':32, 'Y':100, 'K':4}", 2 ),
              (0xB68400, "Khaki", "{'C':24, 'M':45, 'Y':100, 'K':6}", 2 ),
              (0xA6D40D, "Citron Yellow", "{'C':35, 'M':17, 'Y':95, 'K':0}", 2 ),
              (0x98A100, "Citrine", "{'C':36, 'M':32, 'Y':100, 'K':7}", 2 ),
              (0x888D2A, "Buffy Citrine", "{'C':42, 'M':40, 'Y':82, 'K':8}", 2 ),
              (0x7E8743, "Dark Citrine", "{'C':38, 'M':34, 'Y':67, 'K':20}", 2 ),
              (0x76844E, "Light Grayish Olive", "{'C':43, 'M':36, 'Y':62, 'K':19}", 2 ),
              (0x759243, "Kronbergs Green", "{'C':48, 'M':35, 'Y':70, 'K':12}", 2 ),
              (0x718600, "Olive", "{'C':48, 'M':38, 'Y':100, 'K':15}", 2 ),
              (0x8C6510, "Orange Citrine", "{'C':28, 'M':48, 'Y':92, 'K':24}", 2 ),
              (0x9B5348, "Sudan Brown", "{'C':25, 'M':60, 'Y':65, 'K':19}", 2 ),
              (0x58771E, "Olive Green", "{'C':56, 'M':40, 'Y':85, 'K':22}", 2 ),
              (0x706934, "Light Brownish Olive", "{'C':42, 'M':46, 'Y':73, 'K':24}", 2 ),
              (0x505423, "Deep Grayish Olive", "{'C':50, 'M':48, 'Y':78, 'K':37}", 2 ),
              (0x5E4017, "Pale Raw Umber", "{'C':46, 'M':63, 'Y':87, 'K':32}", 2 ),
              (0x503D00, "Sepia", "{'C':48, 'M':60, 'Y':100, 'K':40}", 2 ),
              (0x651300, "Madder Brown", "{'C':36, 'M':88, 'Y':100, 'K':38}", 2 ),
              (0x522000, "Mars Brown/ Tobacco", "{'C':39, 'M':76, 'Y':100, 'K':47}", 2 ),
              (0x362304, "Vandyke Brown", "{'C':56, 'M':71, 'Y':97, 'K':52}", 2 ),
            
            
            
                                    
              
              ]
    query = "INSERT INTO colors VALUES(?, ?, ?,?)"    
    my_pointer.executemany(query, colors)
    my_con.commit()


except sqlite3.IntegrityError:
    print("Clave duplicada")

###### yellow-green colors  3
try:

       
    colors = [(0xB5FFC2, "Turquoise Green", "{'C':29, 'M':0, 'Y':24, 'K':0}", 3 ),
              (0xB3E8C2, "Glaucous Green", "{'C':30, 'M':9, 'Y':24, 'K':0}", 3 ),
              (0xB3D9A3, "Dark Greenish Glaucous", "{'C':30, 'M':15, 'Y':36, 'K':0}", 3 ),
              (0xA6FF47, "Yellow Green", "{'C':35, 'M':0, 'Y':72, 'K':0}", 3 ),
              (0xBDF226, "Light Green Yellow", "{'C':26, 'M':5, 'Y':85, 'K':0}", 3 ),
              (0x7AFF00, "Night Green", "{'C':52, 'M':0, 'Y':100, 'K':0}", 3 ),
              (0x99B333, "Olive Yellow", "{'C':40, 'M':30, 'Y':80, 'K':0}", 3 ),
              (0x65A98F, "Artemisia Green", "{'C':57, 'M':28, 'Y':39, 'K':8}", 3 ),
              (0x5C8A73, "Andover Green", "{'C':60, 'M':40, 'Y':50, 'K':10}", 3 ),
              (0x6A9346, "Rainette Green", "{'C':42, 'M':20, 'Y':62, 'K':28}", 3 ),
              (0x66AB56, "Chromium Green", "{'C':50, 'M':16, 'Y':58, 'K':20}", 3 ),
              (0x56AA69, "Pistachio Green", "{'C':64, 'M':29, 'Y':56, 'K':6}", 3 ),
              (0x33FF7D, "Sea Green", "{'C':80, 'M':0, 'Y':51, 'K':0}", 3 ),
              (0x00D973, "Benzol Green", "{'C':100, 'M':15, 'Y':55, 'K':0}", 3 ),
              (0x23C17C, "Light Porcelain Green", "{'C':86, 'M':22, 'Y':50, 'K':3}", 3 ),
              (0x40C945, "Green", "{'C':75, 'M':21, 'Y':73, 'K':0}", 3 ),
              (0x19CC33, "Dull Viridian Green", "{'C':90, 'M':20, 'Y':80, 'K':0}", 3 ),
              (0x6EA900, "Oil Green", "{'C':53, 'M':28, 'Y':100, 'K':8}", 3 ),
              (0x1EB800, "Diamine Green", "{'C':87, 'M':20, 'Y':100, 'K':10}", 3 ),
              (0x328E13, "Cossack Green", "{'C':76, 'M':32, 'Y':91, 'K':18}", 3 ),
              (0x405416, "Lincoln Green", "{'C':60, 'M':48, 'Y':86, 'K':37}", 3 ),
              (0x324E2A, "Blackish Olive", "{'C':56, 'M':32, 'Y':63, 'K':55}", 3 ),
              (0x172713, "Deep Slate Olive", "{'C':76, 'M':60, 'Y':80, 'K':62}", 3 )
    
              ]
    query = "INSERT INTO colors VALUES(?, ?, ?,?)"    
    my_pointer.executemany(query, colors)
    my_con.commit()


except sqlite3.IntegrityError:
    print("Clave duplicada")


###### blue-green colors  4
try:

       
    colors = [ (0xBFFFE6, "Nile Blue", "{'C':25, 'M':0, 'Y':10, 'K':0}", 4 ),
               (0xABF5ED, "Pale King's Blue", "{'C':33, 'M':4, 'Y':7, 'K':0}", 4 ),
               (0xA6E6DB, "Light Glaucous Blue", "{'C':35, 'M':10, 'Y':14, 'K':0}", 4 ),
               (0x96BFE6, "Salvia Blue", "{'C':41, 'M':25, 'Y':10, 'K':0}", 4 ),
               (0x94FF94, "Cobalt Green", "{'C':42, 'M':0, 'Y':42, 'K':0}", 4 ),
               (0x80FFCC, "Calamine Blue", "{'C':50, 'M':0, 'Y':20, 'K':0}", 4 ),
               (0x6BFFB3, "Venice Green", "{'C':58, 'M':0, 'Y':30, 'K':0}", 4 ),
               (0x29BDAD, "Cerulian Blue", "{'C':84, 'M':26, 'Y':32, 'K':0}", 4 ),
               (0x00CF91, "Peacock Blue", "{'C':100, 'M':19, 'Y':43, 'K':0}", 4 ),
               (0x2DBC94, "Green Blue", "{'C':82, 'M':24, 'Y':40, 'K':3}", 4 ),
               (0x4F8FE6, "Olympic Blue", "{'C':69, 'M':44, 'Y':10, 'K':0}", 4 ),
               (0x0D75FF, "Blue", "{'C':95, 'M':54, 'Y':0, 'K':0}", 4 ),
               (0x008AA1, "Antwarp Blue", "{'C':, 'M':, 'Y':, 'K':}", 4 ),
               (0x0057BA, "Helvetia Blue", "{'C':100, 'M':62, 'Y':19, 'K':10}", 4 ),
               (0x417777, "Dark Medici Blue", "{'C':70, 'M':45, 'Y':45, 'K':15}", 4 ),
               (0x00592E, "Dusky Green", "{'C':100, 'M':30, 'Y':64, 'K':50}", 4 ),
               (0x0024CC, "Deep Lyons Blue", "{'C':100, 'M':85, 'Y':15, 'K':6}", 4 ),
               (0x202D85, "Violet Blue", "{'C':85, 'M':79, 'Y':38, 'K':16}", 4 ),
               (0x003E83, "Vandar Poel's Blue", "{'C':100, 'M':73, 'Y':43, 'K':10}", 4 ),
               (0x0D2B52, "Dark Tyrian Blue", "{'C':90, 'M':66, 'Y':36, 'K':50}", 4 ),
               (0x000D4F, "Dull Violet Black", "{'C':100, 'M':90, 'Y':38, 'K':50}", 4 ),
               (0x000831, "Deep Indigo", "{'C':100, 'M':92, 'Y':52, 'K':60}", 4 ),
               (0x0F261F, "Deep Slate Green", "{'C':80, 'M':50, 'Y':60, 'K':70}", 4 ),
                   
              ]

    query = "INSERT INTO colors VALUES(?, ?, ?,?)"    
    my_pointer.executemany(query, colors)
    my_con.commit()


except sqlite3.IntegrityError:
    print("Clave duplicada")


###### blue-violet colors  5
try:

       
    colors = [ (0xB8B8FF, "Grayish Lavender", "{'C':28, 'M':28, 'Y':0, 'K':0}", 5 ),
                (0xBFABCC, "Grayish Lavender", "{'C':25, 'M':33, 'Y':20, 'K':0}", 5 ),
                (0xCC85D1, "Laelia Pink", "{'C':20, 'M':48, 'Y':18, 'K':0}", 5 ),
                (0xB875EB, "Lilac", "{'C':28, 'M':54, 'Y':8, 'K':0}", 5 ),
                (0xBF36E0, "Eupatorium Purple", "{'C':25, 'M':79, 'Y':12, 'K':0}", 5 ),
                (0x9161F2, "Light Mauve", "{'C':43, 'M':62, 'Y':5, 'K':0}", 5 ),
                (0x9C52F2, "Aconite Violet", "{'C':39, 'M':68, 'Y':5, 'K':0}", 5 ),
                (0x6E66D4, "Dull Blue Violet", "{'C':57, 'M':60, 'Y':17, 'K':0}", 5 ),
                (0x4D52DE, "Dark Soft Violet", "{'C':70, 'M':68, 'Y':13, 'K':0}", 5 ),
                (0x4733FF, "Blue Violet", "{'C':72, 'M':80, 'Y':0, 'K':0}", 5 ),
                (0x754260, "Purple Drab", "{'C':38, 'M':65, 'Y':49, 'K':26}", 5 ),
                (0x5C7287, "Deep Violet/ Plumbeous", "{'C':, 'M':, 'Y':, 'K':}", 5 ),
                (0x7E3075, "Vernonia Purple", "{'C':42, 'M':78, 'Y':46, 'K':15}", 5 ),
                (0x53225C, "Dark Slate Purple", "{'C':64, 'M':85, 'Y':60, 'K':10}", 5 ),
                (0x6B2E63, "Taupe Brown", "{'C':30, 'M':70, 'Y':35, 'K':40}", 5 ),
                (0x531745, "Violet Carmine", "{'C':64, 'M':90, 'Y':70, 'K':10}", 5 ),
                (0x2619D1, "Violet", "{'C':85, 'M':90, 'Y':18, 'K':0}", 5 ),
                (0x3400A3, "Red Violet", "{'C':76, 'M':100, 'Y':25, 'K':15}", 5 ),
                (0x340059, "Cotinga Purple", "{'C':66, 'M':100, 'Y':42, 'K':40}", 5 ),
                (0x2D0060, "Dusky Madder Violet", "{'C':75, 'M':100, 'Y':46, 'K':30}", 5 ),
                   
              ]

    query = "INSERT INTO colors VALUES(?, ?, ?,?)"    
    my_pointer.executemany(query, colors)
    my_con.commit()


except sqlite3.IntegrityError:
    print("Clave duplicada")


###### white-black colors  6
try:

       
    colors = [ (0xFFFFFF, "White", "{'C':0, 'M':0, 'Y':0, 'K':0}", 6 ), 
                (0xB5D1CC, "Neutral Gray", "{'C':29, 'M':18, 'Y':20, 'K':0}", 6 ),
                (0x9FC2B2, "Mineral Gray", "{'C':33, 'M':18, 'Y':25, 'K':7}", 6 ),
                (0x9CB29E, "Warm Gray", "{'C':37, 'M':28, 'Y':36, 'K':3}", 6 ),
                (0x1B3644, "Slate Color", "{'C':85, 'M':70, 'Y':62, 'K':30}", 6 ),
                (0x000000, "Black", "{'C':20, 'M':10, 'Y':15, 'K':100}", 6 ),
                
                   
              ]

    query = "INSERT INTO colors VALUES(?, ?, ?,?)"    
    my_pointer.executemany(query, colors)
    my_con.commit()


except sqlite3.IntegrityError:
    print("Clave duplicada")


query = 'CREATE TABLE palletes( number INTEGER UNSIGNED PRIMARY KEY NOT NULL)'
my_pointer.execute(query)
my_con.commit()
print("Creada nueva tabla")


try: 
    palletes = []
    for i in range(1, 349): 
        n = (i,)
        palletes.append(n)
    query = 'INSERT INTO palletes VALUES(?)'
    my_pointer.executemany(query, palletes)
    my_con.commit()
    print("Palleta añadida")
    """ query = 'SELECT * FROM palletes;'
    my_pointer.execute(query)
    raw = my_pointer.fetchall()
    print(raw) """

except sqlite3.IntegrityError:
    print("Clave duplicada")   



query = 'CREATE TABLE palletes_has_colors( colors_rgb INTEGER UNSIGNED NOT NULL, palletes_number INTEGER UNSIGNED NOT NULL, FOREIGN KEY (palletes_number) REFERENCES palletes(number), FOREIGN KEY (colors_rgb) REFERENCES colors(rgb))'
my_pointer.execute(query)
my_con.commit()
print("Creada nueva tabla")


palletes_has_colors = [(0xDE4500, 1), (0x29BDAD, 1), 
                        (0x0D2B52, 2), (0xFF8C00, 2), 
                        (0xFFF59E, 3), (0xB85E00, 3), 
                        (0x3400A3, 4), (0xC3A55C, 4), 
                        (0x328E13, 5), (0x003E83, 5),
                        (0x000831, 6), (0xFF616B, 6), 
                        (0xB3E8C2, 7), (0xFF5200, 7),
                        (0xC2612C, 8), (0xB8B8FF, 8), 
                        (0x6E66D4, 9), (0x3D0079, 9), 
                        (0x7E8743, 10), (0xC2612C, 10), 
                        (0x9FC2B2, 11), (0xEBD999, 11), 
                        (0x2DBC94, 12), (0xC3A55C, 12), 
                        (0xB85E00, 13), (0x7E3075, 13), 
                        (0xFF4DC9, 14), (0xFAED8F, 14), 
                        (0xB8B8FF, 15), (0x00D973, 15), 
                        (0xABF5ED, 16), (0x740909, 16), 
                        (0xD15E00, 17), (0x33FF7D, 17), 
                        (0x2D0060, 18), (0xD1B0B3, 18), 
                        (0x7AFF00, 19), (0x522000, 19), 
                        (0xCC85D1, 20), (0x80FFCC, 20), 
                        (0xFF616B, 21), (0x33FF7D, 21), 
                        (0x0024CC, 22), (0xFFFF00, 22), 
                        (0x9161F2, 23), (0xFFBF6E, 23), 
                        (0x7E3075, 24), (0x503D00, 24),
                        (0xC9303E, 25), (0xBFFFE6, 25), 
                        (0x5E4017, 26), (0xFA9442, 26), 
                        (0xFFA6D9, 27), (0x1B3644, 27), 
                        (0x000831, 28), (0x651300, 28), 
                        (0x96BFE6, 29), (0x759243, 29), 
                        (0x9FC2B2, 30), (0xA90636, 30), 
                        (0xFFF59E, 31), (0xE81900, 31), 
                        (0x7AFF00, 32), (0xD99E73, 32),
                        (0xB85E00, 33), (0x1B3644, 33), 
                        (0xFF5EC4, 34), (0xB5D1CC, 34), 
                        (0xA10B2B, 35), (0xB08699, 35), 
                        (0xBAA600, 36), (0xB5FFC2, 36), 
                        (0x3400A3, 37), (0xA32100, 37), 
                        (0x1EB800, 38), (0x0024CC, 38), 
                        (0xD60036, 39), (0x0057BA, 39), 
                        (0xC74300, 40), (0xA6D40D, 40), 
                        (0x7E8743, 41), (0x80FFCC, 41), 
                        (0x2619D1, 42), (0xE0B81F, 42), 
                        (0x9C52F2, 43), (0xFFA6D9, 43),
                        (0x4F8FE6, 44), (0x23C17C, 44), 
                        (0xFFCFC4, 45), (0xF2FF26, 45), 
                        (0xFF5200, 46), (0x000000, 46), 
                        (0xB8B8FF, 47), (0xC9303E, 47), 
                        (0xB319AB, 48), (0x0057BA, 48), 
                        (0xABF5ED, 49), (0x0D75FF, 49), 
                        (0x2D0060, 50), (0xEBD999, 50), 
                        (0x0D75FF, 51), (0xA10B2B, 51), 
                        (0x000000, 52), (0xF5F5B8, 52), 
                        (0xFF8C00, 53), (0x2D0060, 53), 
                        (0x00D973, 54), (0xA6E6DB, 54), 
                        (0xD94D99, 55), (0xFFFFFF, 55),
                        (0xB8B8FF, 56), (0x2619D1, 56), 
                        (0x6B2E63, 57), (0x1B3644, 57), 
                        (0x33FF7D, 58), (0x681916, 58), 
                        (0x98A100, 59), (0xFF5EC4, 59), 
                        (0x0D2B52, 60), (0xFFF59E, 60), 
                        (0x340059, 61), (0xBDF226, 61), 
                        (0x000000, 62), (0xFFFF00, 62), 
                        (0x5C2C45, 63), (0x29BDAD, 63), 
                        (0x9C52F2, 64), (0x4D52DE, 64), 
                        (0xBAA600, 65), (0x80FFCC, 65), 
                        (0x58771E, 66), (0xD1BD19, 66), 
                        (0x0D2B52, 67), (0x4F8FE6, 67), 
                        (0xFFFF00, 68), (0xB08699, 68), 
                        (0x000000, 69), (0x9CB29E, 69), 
                        (0x405416, 70), (0xB85E00, 70),
                        (0xD99E73, 71), (0xA90636, 71), 
                        (0xABF5ED, 72), (0xF5F5B8, 72), 
                        (0x6A9346, 73), (0x5E4017, 73), 
                        (0x2DBC94, 74), (0xB5FFC2, 74), 
                        (0xABF5ED, 75), (0x202D85, 75),
                        (0xFFF59E, 76), (0x9CB29E, 76), 
                        (0xD15E00, 77), (0x003E83, 77), 
                        (0x6BFFB3, 78), (0xF2AD78, 78), 
                        (0x2DBC94, 79), (0x651300, 79), 
                        (0xF5F5B8, 80), (0x9161F2, 80), 
                        (0xFA9442, 81), (0x9CB29E, 81), 
                        (0x681916, 82), (0x2D0060, 82), 
                        (0x202D85, 83), (0xBCD382, 83), 
                        (0xFFCFC4, 84), (0x0F261F, 84), 
                        (0x008AA1, 85), (0xC74300, 85), 
                        (0xB85E00, 86), (0x33FF7D, 86), 
                        (0xA6D40D, 87), (0xFFA6D9, 87), 
                        (0x0D75FF, 88), (0xFFCFC4, 88), 
                        (0xFF8C00, 89), (0x202D85, 89), 
                        (0x9C52F2, 90), (0xFF5EC4, 90), 
                        (0x5C2C45, 91), (0xC05200, 91), 
                        (0xFF7399, 92), (0x00D973, 92), 
                        (0xA6E6DB, 93), (0x98A100, 93), 
                        (0x00592E, 94), (0xEBD999, 94), 
                        (0x681916, 95), (0x000D4F, 95), 
                        (0x718600, 96), (0xE0B81F, 96), 
                        (0xFFA6D9, 97), (0xC9303E, 97), 
                        (0x651300, 98), (0x202D85, 98), 
                        (0xFFF59E, 99), (0x29BDAD, 99), 
                        (0x888D2A, 100), (0x6E66D4, 100), 
                        (0x0024CC, 101), (0xE6ADCF, 101), 
                        (0xEBD999, 102), (0xC05200, 102), 
                        (0x2D0060, 103), (0xC2612C, 103), 
                        (0xBAA600, 104), (0xA10B2B, 104), 
                        (0xE6ADCF, 105), (0x66AB56, 105), 
                        (0x000D4F, 106), (0x008AA1, 106), 
                        (0x76844E, 107), (0xFFE600, 107), 
                        (0xFF5EC4, 108), (0xA32100, 108), 
                        (0xFFF59E, 109), (0x324E2A, 109), 
                        (0x6C2B11, 110), (0x362304, 110), 
                        (0xFFF59E, 111), (0xA6FF47, 111),
                        (0x000000, 112), (0xFF616B, 112),
                        (0xFFCFC4, 113), (0x362304, 113), 
                        (0x008AA1, 114), (0xFFAB00, 114), 
                        (0xFAED8F, 115), (0xFF3319, 115),
                        (0x4733FF, 116), (0xE6ADCF, 116), 
                        (0xD60036, 117), (0x000000, 117), 
                        (0x362304, 118), (0xE0B81F, 118),
                        (0x0D2B52, 119), (0xA6E6DB, 119), 
                        (0xE6ADCF, 120), (0xA90636, 120),                       
                        (0x405416, 121), (0xD99E73, 121), (0x6C2B11, 121), 
                        (0x00D973, 122), (0xFFB852, 122), (0xD60036, 122),
                        (0xFF7399, 123), (0x6B2E63, 123), (0xF2FF26, 123), 
                        (0x99B333, 124), (0xE0B81F, 124), (0x730F1F, 124),
                        (0x29BDAD, 125), (0xD1B0B3, 125), (0x202D85, 125),
                        (0xE0B81F, 126), (0x0024CC, 126), (0xEBD999, 126), 
                        (0xFFBF6E, 127), (0x56AA69, 127), (0x4D52DE, 127), 
                        (0x6BFFB3, 128), (0x9161F2, 128), (0xFFA6D9, 128),
                        (0xB68400, 129), (0x96BFE6, 129), (0xFFE600, 129), 
                        (0xA10B2B, 130), (0x2619D1, 130), (0xB85E00, 130),
                        (0xDE4500, 131), (0x00CF91, 131), (0xB85E00, 131), 
                        (0x98A100, 132), (0xFA9442, 132), (0xF5F5B8, 132), 
                        (0x33FF7D, 133), (0x740909, 133), (0x98A100, 133), 
                        (0xFF5EC4, 134), (0x9161F2, 134), (0x3400A3, 134), 
                        (0x96BFE6, 135), (0xF5F5B8, 135), (0x328E13, 135), 
                        (0x3400A3, 136), (0xD50C42, 136), (0x19CC33, 136),
                        (0xC9303E, 137), (0x56AA69, 137), (0xFFBF6E, 137), 
                        (0xFA9442, 138), (0x6BFFB3, 138), (0xF2FF26, 138), 
                        (0xB5D1CC, 139), (0x000831, 139), (0x96BFE6, 139), 
                        (0xFA9442, 140), (0x1B3644, 140), (0x008AA1, 140), 
                        (0xFF5200, 141), (0x0D2B52, 141), (0xA6FF47, 141), 
                        (0x9E194D, 142), (0x96BFE6, 142), (0xBAA600, 142), 
                        (0x9CB29E, 143), (0x0D75FF, 143), (0xB875EB, 143), 
                        (0xFF5200, 144), (0x000000, 144), (0xB319AB, 144), 
                        (0x000D4F, 145), (0x6C2B11, 145), (0xA6D40D, 145), 
                        (0xB68400, 146), (0x1EB800, 146), (0x505423, 146), 
                        (0xB5FFC2, 147), (0x740909, 147), (0xFF4DC9, 147), 
                        (0xFFAB00, 148), (0x29BDAD, 148), (0xD1BD19, 148), 
                        (0x0F261F, 149), (0xFF5200, 149), (0xD1BD19, 149), 
                        (0xFFCFC4, 150), (0xA6D40D, 150), (0xB3E8C2, 150),
                        (0xFF8C00, 151), (0x003E83, 151), (0xF5F5B8, 151), 
                        (0xC9303E, 152), (0xA6E6DB, 152), (0x681916, 152), 
                        (0xFF5EC4, 153), (0xFFAB00, 153), (0xA6D40D, 153), 
                        (0xD60036, 154), (0xFFFF00, 154), (0x0D75FF, 154), 
                        (0x00D973, 155), (0xFA2B00, 155), (0x000831, 155), 
                        (0x2619D1, 156), (0xD1BD19, 156), (0x94FF94, 156),
                        (0x6F0043, 157), (0xD1BD19, 157), (0x4F8FE6, 157),
                        (0xC2612C, 158), (0x7AFF00, 158), (0xF2FF26, 158),
                        (0x80FFCC, 159), (0xB68400, 159), (0xB8B8FF, 159), 
                        (0x417777, 160), (0x5E4017, 160), (0xBAA600, 160),
                        (0xF2AD78, 161), (0x0057BA, 161), (0x6C2B11, 161),
                        (0x6A9346, 162), (0xD94D99, 162), (0xB875EB, 162), 
                        (0xB5FFC2, 163), (0x008AA1, 163), (0xFFE600, 163), 
                        (0xFFAB00, 164), (0x2619D1, 164), (0xE81900, 164), 
                        (0x5C2C45, 165), (0xFF4DC9, 165), (0xE6ADCF, 165), 
                        (0xFF616B, 166), (0xFAED8F, 166), (0x0F261F, 166), 
                        (0xABF5ED, 167), (0xC0B490, 167), (0x003E83, 167), 
                        (0x003E83, 168), (0xF2FF26, 168), (0x7E3075, 168), 
                        (0xFFA6D9, 169), (0x9CB29E, 169), (0xFFF59E, 169), 
                        (0xB319AB, 170), (0xFFAB00, 170), (0x3400A3, 170), 
                        (0xFF8C00, 171), (0xB3E8C2, 171), (0x730F1F, 171), 
                        (0x008AA1, 172), (0x3400A3, 172), (0xC2612C, 172), 
                        (0xF2FF26, 173), (0x651300, 173), (0xB5FFC2, 173), 
                        (0x6B2E63, 174), (0xB8B8FF, 174), (0xFFA6D9, 174), 
                        (0xBCD382, 175), (0xF2AD78, 175), (0x4733FF, 175), 
                        (0x80FFCC, 176), (0xFFB3F0, 176), (0xFFCFC4, 176), 
                        (0x888D2A, 177), (0x730F1F, 177), (0xB8B8FF, 177), 
                        (0xA6E6DB, 178), (0xEBD999, 178), (0x2DBC94, 178), 
                        (0xE81900, 179), (0x0024CC, 179), (0xFA9442, 179), 
                        (0x9161F2, 180), (0xB5D1CC, 180), (0xFFBF6E, 180),
                        (0x340059, 181), (0x2619D1, 181), (0xA10B2B, 181), 
                        (0x362304, 182), (0xB85E00, 182), (0x000831, 182), 
                        (0x7E3075, 183), (0x3400A3, 183), (0x5C7287, 183), 
                        (0x76844E, 184), (0xEBD999, 184), (0xFF4DC9, 184), 
                        (0xFFF59E, 185), (0xB08699, 185), (0xC9303E, 185), 
                        (0x681916, 186), (0x0D75FF, 186), (0xD99E73, 186), 
                        (0xB8B8FF, 187), (0x0057BA, 187), (0x9C52F2, 187), 
                        (0x94FF94, 188), (0x6A9346, 188), (0x96BFE6, 188), 
                        (0x6BFFB3, 189), (0xF2FF26, 189), (0x172713, 189), 
                        (0x000000, 190), (0xDE4500, 190), (0xEBD999, 190), 
                        (0x0D75FF, 191), (0xB08699, 191), (0xE0B81F, 191), 
                        (0xFFB852, 192), (0x5C7287, 192), (0x362304, 192), 
                        (0x23C17C, 193), (0xFAED8F, 193), (0xFF616B, 193), 
                        (0xFA2B00, 194), (0x4F8FE6, 194), (0xFFCFC4, 194), 
                        (0xFF4DC9, 195), (0xFFF59E, 195), (0xB5D1CC, 195), 
                        (0xA6D40D, 196), (0x4733FF, 196), (0xABF5ED, 196), 
                        (0x4D52DE, 197), (0xFF5EC4, 197), (0xB5D1CC, 197), 
                        (0x40C945, 198), (0xFFE600, 198), (0xA93400, 198), 
                        (0x0024CC, 199), (0xA7374B, 199), (0x706934, 199), 
                        (0xBCD382, 200), (0xA10B2B, 200), (0x66AB56, 200), 
                        (0x718600, 201), (0xFF616B, 201), (0x94FF94, 201), 
                        (0x94FF94, 202), (0x1B3644, 202), (0xB5FFC2, 202), 
                        (0xF59994, 203), (0x405416, 203), (0xFFF59E, 203), 
                        (0xB319AB, 204), (0xA6E6DB, 204), (0xC2612C, 204), 
                        (0xF59994, 205), (0x730F1F, 205), (0x2619D1, 205), 
                        (0xFFA6D9, 206), (0xC2612C, 206), (0xFA9442, 206), 
                        (0x000000, 207), (0xB3E8C2, 207), (0x9B5348, 207), 
                        (0x2DBC94, 208), (0xF5F5B8, 208), (0x008AA1, 208),
                        (0xFF8C00, 209), (0x96BFE6, 209), (0xEBD999, 209), 
                        (0xF2FF26, 210), (0x405416, 210), (0xFFBF6E, 210),
                        (0x000831, 211), (0xFF7340, 211), (0x99B333, 211), 
                        (0x8C6510, 212), (0x96BFE6, 212), (0xA90636, 212), 
                        (0xFFE600, 213), (0xABF5ED, 213), (0xF59994, 213), 
                        (0x9B5348, 214), (0xEBD999, 214), (0x2619D1, 214), 
                        (0xBF36E0, 215), (0xFFB852, 215), (0x0D75FF, 215), 
                        (0xFA2B00, 216), (0x000000, 216), (0x40C945, 216), 
                        (0x730F1F, 217), (0xD99E73, 217), (0x1EB800, 217), 
                        (0x5C7287, 218), (0xB8B8FF, 218), (0x0057BA, 218), 
                        (0xFA2B00, 219), (0x00592E, 219), (0x66AB56, 219), 
                        (0x9C52F2, 220), (0xB90078, 220), (0xD99E73, 220), 
                        (0x000000, 221), (0xA10B2B, 221), (0xB5D1CC, 221), 
                        (0xFF8C00, 222), (0xE0B81F, 222), (0xC05200, 222), 
                        (0xB08699, 223), (0xD99E73, 223), (0xB5FFC2, 223), 
                        (0x417777, 224), (0xFF4DC9, 224), (0x6B2E63, 224), 
                        (0x53225C, 225), (0x00592E, 225), (0xD60036, 225),
                        (0x2619D1, 226), (0xFFB852, 226), (0x5C2C45, 226), 
                        (0x29BDAD, 227), (0xA6E6DB, 227), (0xFFB3F0, 227), 
                        (0xA10B2B, 228), (0xB5D1CC, 228), (0xFFF59E, 228), 
                        (0xB5D1CC, 229), (0x172713, 229), (0xFA9442, 229), 
                        (0xFF616B, 230), (0xB5FFC2, 230), (0x94FF94, 230), 
                        (0x681916, 231), (0xE6ADCF, 231), (0x4F8FE6, 231), 
                        (0x000831, 232), (0xD60036, 232), (0xF2AD78, 232), 
                        (0x202D85, 233), (0xA10B2B, 233), (0x888D2A, 233), 
                        (0xABF5ED, 234), (0x5E4017, 234), (0xFFBF6E, 234), 
                        (0xFF8C00, 235), (0xEBD999, 235), (0xBFABCC, 235), 
                        (0x754260, 236), (0x0024CC, 236), (0xB68400, 236), 
                        (0xA10B2B, 237), (0x96BFE6, 237), (0x651300, 237), 
                        (0x9CB29E, 238), (0x340059, 238), (0xD99E73, 238),
                        (0xB08699, 239), (0xB3E8C2, 239), (0xC4BF33, 239),
                        (0xFF788C, 240), (0x29BDAD, 240), (0xFFFF00, 240),
                        (0xE81900, 241), (0x417777, 241), (0xFFF59E, 241), (0xC3A55C, 241), 
                        (0xFF5EC4, 242), (0x1EB800, 242), (0xA93400, 242), (0x000000, 242), 
                        (0xB85E00, 243), (0x58771E, 243), (0xEBD999, 243), (0x1B3644, 243), 
                        (0xB08699, 244), (0x008AA1, 244), (0xC74300, 244), (0x5C8A73, 244), 
                        (0x6EA900, 245), (0x1B3644, 245), (0x0D2B52, 245), (0xA10B2B, 245), 
                        (0xA32100, 246), (0xFFA6D9, 246), (0xF5F5B8, 246), (0xFFBF6E, 246),
                        (0xB85E00, 247), (0x00D973, 247), (0x0024CC, 247), (0xFFE600, 247), 
                        (0xB8B8FF, 248), (0xB68400, 248), (0xFF5EC4, 248), (0x53225C, 248), 
                        (0xD1BD19, 249), (0x417777, 249), (0x681916, 249), (0xC0B490, 249),
                        (0xC4BF33, 250), (0xFF3319, 250), (0x33FF7D, 250), (0xBFFFE6, 250), 
                        (0xA10045, 251), (0x1EB800, 251), (0x1B3644, 251), (0xFFFF00, 251),
                        (0xD15E00, 252), (0xBAA600, 252), (0x2DBC94, 252), (0xB85E00, 252), 
                        (0xFF7340, 253), (0xF2FF26, 253), (0x340059, 253), (0x1B3644, 253), 
                        (0xCC85D1, 254), (0x718600, 254), (0xF5F5B8, 254), (0xFFA6D9, 254), 
                        (0x80FFCC, 255), (0x000000, 255), (0xC4BF33, 255), (0xB85E00, 255), 
                        (0x000000, 256), (0xFF5200, 256), (0xF59994, 256), (0x19CC33, 256), 
                        (0x0D75FF, 257), (0xF20000, 257), (0x9C52F2, 257), (0xFFAB00,257),
                        (0xF2AD78, 258), (0x718600, 258), (0x730F1F, 258), (0x008AA1, 258), 
                        (0x2DBC94, 259), (0x9CB29E, 259), (0xF2FF26, 259), (0x0057BA, 259), 
                        (0xD94D99, 260), (0x33FF7D, 260), (0xB3E8C2, 260), (0xF59994, 260), 
                        (0x9CB29E, 261), (0xA10045, 261), (0xFFF59E, 261), (0x80FFCC, 261), 
                        (0xEBD999, 262), (0xD15E00, 262), (0x328E13, 262), (0x98A100, 262), 
                        (0xF2AD78, 263), (0x1B3644, 263), (0xA93400, 263), (0xB5FFC2, 263), 
                        (0xFFA6D9, 264), (0x29BDAD, 264), (0xE81900, 264), (0xB3D9A3, 264), 
                        (0x99B333, 265), (0xD94D99, 265), (0x000D4F, 265), (0xFFE600, 265), 
                        (0xF20000, 266), (0xEBD999, 266), (0x6A9346, 266), (0x00D973, 266), 
                        (0x0D75FF, 267), (0xFF8C00, 267), (0x00D973, 267), (0xFFB852, 267), 
                        (0x172713, 268), (0xB08699, 268), (0xBFFFE6, 268), (0xB85E00, 268), 
                        (0x9C52F2, 269), (0x730F1F, 269), (0xB85E00, 269), (0x000000, 269), 
                        (0xF5F5B8, 270), (0xD15E00, 270), (0x58771E, 270), (0x328E13, 270), 
                        (0x94FF94, 271), (0x0F261F, 271), (0xB90078, 271), (0x2DBC94, 271), 
                        (0x96BFE6, 272), (0xB5FFC2, 272), (0xFF5200, 272), (0xFFF59E, 272), 
                        (0x6F0043, 273), (0xB5D1CC, 273), (0xFFB3F0, 273), (0x9B5348, 273),
                        (0x7E8743, 274), (0x9161F2, 274), (0xFF3319, 274), (0x4F8FE6, 274), 
                        (0xC9303E, 275), (0xC0B490, 275), (0x651300, 275), (0x6B2E63, 275), 
                        (0xFFCFC4, 276), (0x000000, 276), (0xFF5EC4, 276), (0xA6FF47, 276), 
                        (0xFF4DC9, 277), (0x000D4F, 277), (0x718600, 277), (0xB319AB, 277), 
                        (0xD1BD19, 278), (0x00592E, 278), (0x328E13, 278), (0xFFB852, 278), 
                        (0xB85E00, 279), (0x0D2B52, 279), (0xF59994, 279), (0xC0B490, 279), 
                        (0x405416, 280), (0x6B2E63, 280), (0xD15E00, 280), (0xCC85D1, 280), 
                        (0x008AA1, 281), (0x00D973, 281), (0xFFF59E, 281), (0x94FF94, 281),
                        (0xB875EB, 282), (0xC2975A, 282), (0x94FF94, 282), (0x94FF94, 282),
                        (0x730F1F, 283), (0x66AB56, 283), (0x6BFFB3, 283), (0xA7374B, 283),
                        (0xD15E00, 284), (0x33FF7D, 284), (0xFFE600, 284), (0x00592E, 284), 
                        (0xB08699, 285), (0xFF3319, 285), (0xA93400, 285), (0xB5FFC2, 285), 
                        (0xFFAB00, 286), (0x00CF91, 286), (0xA93400, 286), (0x202D85, 286), 
                        (0xABF5ED, 287), (0xFF5EC4, 287), (0xC4BF33, 287), (0x80FFCC, 287), 
                        (0xFF8C00, 288), (0x6B2E63, 288), (0x503D00, 288), (0x000000, 288), 
                        (0x000D4F, 289), (0xF2FF26, 289), (0x202D85, 289), (0xBDF226, 289), 
                        (0x405416, 290), (0x5C2C45, 290), (0xFFF59E, 290), (0x94FF94, 290), 
                        (0x80FFCC, 291), (0x94FF94, 291), (0x33FF7D, 291), (0xBDF226, 291),
                        (0xFFF59E, 292), (0xC0B490, 292), (0xF2AD78, 292), (0xC3A55C, 292), 
                        (0xB85E00, 293), (0xB5FFC2, 293), (0x65A98F, 293), (0x40C945, 293), 
                        (0x328E13, 294), (0xFFB852, 294), (0x96BFE6, 294), (0xF5F5B8, 294), 
                        (0xFFB852, 295), (0xFFFF00, 295), (0x000D4F, 295), (0x0D75FF, 295), 
                        (0x5E4017, 296), (0xD99E73, 296), (0xF5F5B8, 296), (0x1B3644, 296), 
                        (0xA93400, 297), (0xFF8C00, 297), (0x202D85, 297), (0x202D85, 297), 
                        (0xF2FF26, 298), (0xFF3319, 298), (0xB85E00, 298), (0x000000, 298), 
                        (0x6EA900, 299), (0xF59994, 299), (0x008AA1, 299), (0xCC1A97, 299), 
                        (0x80FFCC, 300), (0xFFB852, 300), (0xFF616B, 300), (0xB5FFC2, 300), 
                        (0xF20000, 301), (0xEBD999, 301), (0x9C52F2, 301), (0x6A9346, 301), 
                        (0xFFB852, 302), (0xC0B490, 302), (0x008AA1, 302), (0xBFFFE6, 302), 
                        (0xFAED8F, 303), (0xFF3319, 303), (0xB5D1CC, 303), (0x172713, 303), 
                        (0x00D973, 304), (0xFFB852, 304), (0x7E8743, 304), (0x681916, 304), 
                        (0xF2AD78, 305), (0xFFE600, 305), (0xB5FFC2, 305), (0xA6D40D, 305), 
                        (0x19CC33, 306), (0xBFFFE6, 306), (0x00D973, 306), (0xF2FF26, 306), 
                        (0x340059, 307), (0xB8B8FF, 307), (0xD60036, 307), (0x9C52F2, 307), 
                        (0xDE4500, 308), (0xD1B0B3, 308), (0x94FF94, 308), (0xD50C42, 308), 
                        (0xFA9442, 309), (0xFF7340, 309), (0x003E83, 309), (0x202D85, 309), 
                        (0x718600, 310), (0xF2AD78, 310), (0x172713, 310), (0xF5F5B8, 310), 
                        (0xA90636, 311), (0xB3D9A3, 311), (0xFFB852, 311), (0xBDF226, 311), 
                        (0xA93400, 312), (0x65A98F, 312), (0x0057BA, 312), (0xFF8C00, 312), 
                        (0xD60036, 313), (0x000000, 313), (0x1EB800, 313), (0xFFFF00, 313),
                        (0x2D0060, 314), (0x0024CC, 314), (0xFF5EC4, 314), (0x681916, 314), 
                        (0xFA9442, 315), (0xBF36E0, 315), (0xF5F5B8, 315), (0xFF616B, 315), 
                        (0x3400A3, 316), (0x740909, 316), (0x19CC33, 316), (0x2619D1, 316), 
                        (0xB5FFC2, 317), (0xFFBF99, 317), (0xF2FF26, 317), (0xC0B490, 317), 
                        (0x706934, 318), (0x0F261F, 318), (0x00592E, 318), (0x324E2A, 318), 
                        (0xFFE600, 319), (0xFF8C00, 319), (0xB85E00, 319), (0x328E13, 319), 
                        (0x6EA900, 320), (0xFF7399, 320), (0xA6E6DB, 320), (0xF5F5B8, 320),
                        (0xF5F5B8, 321), (0x96BFE6, 321), (0xB08699, 321), (0x172713, 321), 
                        (0x4733FF, 322), (0xBF36E0, 322), (0xA32100, 322), (0xF20000, 322),
                        (0xFFBF6E, 323), (0xA6D40D, 323), (0x000000, 323), (0x651300, 323),
                        (0xA90636, 324), (0x9C52F2, 324), (0x4F8FE6, 324), (0xB5D1CC, 324), 
                        (0x0F261F, 325), (0xFAED8F, 325), (0xD15E00, 325), (0xE0B81F, 325), 
                        (0x7AFF00, 326), (0xF5F5B8, 326), (0xFF3319, 326), (0xA6FF47, 326), 
                        (0xC0B490, 327), (0xFF5EC4, 327), (0xBFABCC, 327), (0xB85E00, 327), 
                        (0xA32100, 328), (0x23C17C, 328), (0xFF7340, 328), (0x362304, 328), 
                        (0x1B3644, 329), (0xFFB852, 329), (0xBFABCC, 329), (0x340059, 329), 
                        (0xBFFFE6, 330), (0x96BFE6, 330), (0xBCD382, 330), (0x2DBC94, 330), 
                        (0x9161F2, 331), (0x2619D1, 331), (0xCC1A97, 331), (0x000D4F, 331), 
                        (0x172713, 332), (0x00592E, 332), (0xFF7399, 332), (0xD50C42, 332), 
                        (0x94FF94, 333), (0xF2FF26, 333), (0xA93400, 333), (0x0D75FF, 333),
                        (0x718600, 334), (0x008AA1, 334), (0xA6FF47, 334), (0xFFCFC4, 334), 
                        (0x740909, 335), (0x1B3644, 335), (0xFF8C00, 335), (0x2619D1, 335), 
                        (0x681916, 336), (0xFF5EC4, 336), (0xFFF59E, 336), (0x324E2A, 336), 
                        (0x5C2C45, 337), (0x531745, 337), (0x000000, 337), (0xCC85D1, 337),
                        (0xFFAB00, 338), (0xBFABCC, 338), (0x00592E, 338), (0xA10B2B, 338),
                        (0xDE4500, 339), (0xD99E73, 339), (0x202D85, 339), (0xA6E6DB, 339), 
                        (0xFF3319, 340), (0x33FF7D, 340), (0x000000, 340), (0xB5D1CC, 340), 
                        (0x328E13, 341), (0xA6E6DB, 341), (0x172713, 341), (0xFF616B, 341), 
                        (0x172713, 342), (0xFFB852, 342), (0xFFA6D9, 342), (0x8C6510, 342), 
                        (0xEBD999, 343), (0x505423, 343), (0x003E83, 343), (0xA93400, 343), 
                        (0x9C52F2, 344), (0xFFBF6E, 344), (0x000000, 344), (0x0024CC, 344), 
                        (0x4733FF, 345), (0x681916, 345), (0xBFFFE6, 345), (0x6BFFB3, 345), 
                        (0xBDF226, 346), (0xB319AB, 346), (0x5C8A73, 346), (0xB5FFC2, 346), 
                        (0x33FF7D, 347), (0x0057BA, 347), (0xB875EB, 347), (0x99B333, 347), 
                        (0x340059, 348), (0x328E13, 348), (0x172713, 348), (0xBCD382, 348)]
    
query = "INSERT INTO palletes_has_colors VALUES(?,?)"
my_pointer.executemany(query, palletes_has_colors)
my_con.commit()
print('Data inserted correctly')


my_con.close()






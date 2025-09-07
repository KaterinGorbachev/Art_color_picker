import sqlite3

bd_name = 'Colors.db'

my_con = sqlite3.connect(bd_name)

my_pointer = my_con.cursor()

print(f'Conectado a la base de datos {bd_name}')

'''
query = 'CREATE TABLE category( id INTEGER UNSIGNED PRIMARY KEY NOT NULL, name VARCHAR(100) NOT NULL);'
my_pointer.execute(query)
my_con.commit()
print("Creada nueva tabla")
 #####create a table with colors
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
              (0x5C2C45, 'Vistoris lake', "{'C':40, 'M':71, 'Y':55, 'K':40}", 1 ),
                                    
              
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
              (0x522000, "Mars Brown/Tobacco", "{'C':39, 'M':76, 'Y':100, 'K':47}", 2 ),
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
                (0x5C7287, "Deep Violet/Plumbeous", "{'C':, 'M':, 'Y':, 'K':}", 5 ),
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




####(0x, "", "{'C':, 'M':, 'Y':, 'K':}", 0 ),



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
                        (0xFF4DC9, 14), (0xFBE6A0, 14), 
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
                        (0x00D973, 54), (0xA6E6DB, 54), ]
'''

                    #     
                    #    (0xFF616B, 166), (0xFBE6A0, 166), (0x112F2C, 166), 
                    #    (0xD15E00, 325), (0xFBE6A0, 325), (0x112F2C, 325), (0xE2B540, 325) ]


palletes_has_colors = [(0xD94D99, 55), (0xFFFFFF, 55),
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
                       (0xBAA600, 104), (0xA10B2B, 105), 
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
                       (0xFBE6A0, 115), (0xF15A30, 115),
                       (0x4733FF, 116), (0xE6ADCF, 116), 
                       (0xD60036, 117), (0x000000, 117), 
                       (0x362304, 118), (0xE0B81F, 118),
                       (0x0D2B52, 119), (0xA6E6DB, 119), 
                       (0xE6ADCF, 120), (0xA90636, 120) 
        

                    ]
    
query = "INSERT INTO palletes_has_colors VALUES(?,?)"
my_pointer.executemany(query, palletes_has_colors)
my_con.commit()
print('Data inserted correctly')



''' 
query = 'CREATE TABLE user( id_user INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name VARCHAR(25) DEFAULT "Anonime")'
my_pointer.execute(query)
my_con.commit()
print("Creada nueva tabla")


query = "INSERT INTO user(id_user) VALUES(NULL)"
my_pointer.execute(query)
my_con.commit()




query = 'CREATE TABLE collection( palletes_number INTEGER UNSIGNED NOT NULL, user_id_user INT UNSIGNED NOT NULL, PRIMARY KEY (palletes_number, user_id_user), FOREIGN KEY (palletes_number) REFERENCES palletes (number), FOREIGN KEY (user_id_user) REFERENCES user (id_user))'
my_pointer.execute(query)
my_con.commit()
print("Creada nueva tabla")

#collection = [(115, 1), (14,2)]

#query = "INSERT INTO collection VALUES(?,?)" 
#my_pointer.executemany(query, collection)
#my_con.commit()

'''

my_con.close()






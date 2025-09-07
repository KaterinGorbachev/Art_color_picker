#print(len(hex(55667).lstrip('0x')))



            
""" rgb_name=[55667, 882175, 53137, 35489, 863058]

for item in rgb_name: 
            prefix='#'
            if len(hex(item).lstrip('0x'))<7:
                while  len(prefix+hex(item).lstrip('0x'))<7: 
                        prefix += '0'


                print(prefix,hex(item).lstrip('0x'), sep='')
                     """

import sqlite3
db = sqlite3.connect('./Colors.db')
cursor = db.cursor()
query = f"SELECT palletes_number FROM palletes_has_colors WHERE colors_rgb = (SELECT rgb FROM colors WHERE name = ?);"
cursor.execute(query, ('Black',))
palletes = {}
data = []

palletes_num = cursor.fetchall()

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
    
    
    
print(palletes)
    
    


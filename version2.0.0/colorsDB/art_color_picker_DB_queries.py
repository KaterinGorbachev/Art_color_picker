import sqlite3

def main():

    name_DB = 'art_color_picker_BD_1'
    my_con = sqlite3.connect(name_DB)

    my_pointer = my_con.cursor()

    print(f'Conectado a la base de datos {name_DB}')

    #print(show_palletes_for_color(my_pointer, my_con))
    print(show_colors_in_pallete(my_pointer, my_con))

    



def show_palletes_for_color(my_pointer, my_con): 
    query_palletes = 'SELECT * FROM palletes_has_colors;'

    my_pointer.execute(query_palletes)

    pallete = my_pointer.fetchone()
    palletes_list = []
    while pallete != None: 
        if pallete[0] == 0xFBE6A0:    #change to user input 
            palletes_list.append(pallete[1]) 
        
        pallete = my_pointer.fetchone()

    return palletes_list


def show_colors_in_pallete(my_pointer, my_con): 
    query_palletes = 'SELECT * FROM palletes_has_colors;'
    my_pointer.execute(query_palletes)

    pallete = my_pointer.fetchone()
    pallete_colors = {}
    while pallete != None: 
        if pallete[1] == 0:    #change for user input
            
            pallete_colors[pallete[2]] = pallete[0]

        pallete = my_pointer.fetchone()

    if len(pallete_colors)>0: 
        return pallete_colors
    else: 
        return "No tiene pallete con ese numero"



main()



import curses,random,time
import DnD_functions
#from DnD_functions import player

def main(stdscr):
    curses.curs_set(0)  
    stdscr.nodelay(True)  
    stdscr.timeout(100)  

    user =DnD_functions.player()
    
    mapPosition = {'row': random.randrange(0, 8), 'column': random.randrange(0, 8)}
    
    # شرط برای چک کردن موقعیت اژدها که توی خونه شروع 0و0 قرار نگیره 
    randomRow=random.randrange(0, 8); randomcolumn=random.randrange(0, 8)
    while randomcolumn+randomRow == 0:
        randomRow=random.randrange(0, 8); randomcolumn=random.randrange(0, 8)
    dragonFury=DnD_functions.dragon({'row': randomRow, 'column': randomcolumn})

    # شرط برای چک کردن موقعیت دانجن که با موقعیت اژدها یکی نباشه
    dungenPosition = {'row': random.randrange(0, 8), 'column': random.randrange(0, 8)}
    while dragonFury.dragonPosition == dungenPosition:
        dungenPosition = {'row': random.randrange(0, 8), 'column': random.randrange(0, 8)}

    DnD_functions.showMap(stdscr, user.userPosition, dragonFury.dragonPosition, dungenPosition, mapPosition)

    while True:
        
        # برای پیدا کردن جهتی که بازیکن نسبت به اژدها قرار دارد، شمالغرب/شمالشرق/جنوبغرب/جنوبشرق
        if user.userPosition['row']-dragonFury.dragonPosition['row']<0:    
            directOnRow='N'
        else:
            directOnRow='S'
        if  user.userPosition['column']-dragonFury.dragonPosition['column']<0:
            directOnColumn='W'
        else:
            directOnColumn='E'
        directToGo=directOnRow+directOnColumn

        # گرفتن کلید فرمان حرکت از بازیکن
        key = stdscr.getch()
        movement = ''
        if key == curses.KEY_UP:
            movement = 'up'
        elif key == curses.KEY_DOWN:
            movement = 'down'
        elif key == curses.KEY_LEFT:
            movement = 'left'
        elif key == curses.KEY_RIGHT:
            movement = 'right'

        if movement != '':
            user.get_direction(movement)
            dragonFury.find_accessable_blocks(dungenPosition)
            dragonFury.move_dragon(user.userPosition,directToGo)
            DnD_functions.showMap(stdscr, user.userPosition, dragonFury.dragonPosition, dungenPosition, mapPosition)
        gameover, result = DnD_functions.isGameover(user.userPosition, dungenPosition, dragonFury.dragonPosition)
        if gameover:
            stdscr.addstr(result)
            stdscr.refresh()
            time.sleep(3)
            break
        time.sleep(0.1)

curses.wrapper(main)
import curses
import random,time

def getDirection(movement='', userPosition={'row':0, 'column':0}):
    if movement == 'up':
        if userPosition['row'] != 0:
            userPosition['row'] -= 1
            return userPosition
        else:
            return userPosition
    elif movement== 'down':
        if userPosition['row'] != 4:
            userPosition['row'] += 1
            return userPosition
        else:
            return userPosition
    elif movement == 'right':
        if userPosition['column'] != 4:
            userPosition['column'] += 1
            return userPosition 
        else:
            return userPosition
    elif movement == 'left':
        if userPosition['column'] != 0:
            userPosition['column'] -= 1
            return userPosition
        else:
            return userPosition
    else:
        return userPosition


def showMap(stdscr, userPosition,dragonPosition):
    stdscr.clear()
    stdscr.addstr('  Do your move (using cursor keys)\n')
    stdscr.addstr(' _ _ _ _ _\n')
    mapLine = '_'
    for row in range(0, 5):
        stdscr.addstr('|')
        for column in range(0, 5):
            if userPosition['row'] == row and userPosition['column'] == column:
                stdscr.addstr('X')
            elif dragonPosition['row'] == row and dragonPosition['column'] == column:
                stdscr.addstr('D')
            else:
                stdscr.addstr(mapLine)
            
            stdscr.addstr('|')
        stdscr.addstr('\n')
    stdscr.refresh()

def moveDragon(userPosition,dragonPosition,dungenPosition):
    if userPosition['row']>dragonPosition['row'] and userPosition['row']-dragonPosition['row']>=2:
        dragonPosition['row']+=1
        if dragonPosition == dungenPosition:
            dragonPosition['row']-=1
            if userPosition['column']>dragonPosition['column'] and userPosition['column']-dragonPosition['column']>=2:
                dragonPosition['column']+=1
                return dragonPosition
            elif userPosition['column']<dragonPosition['column'] and dragonPosition['column']-userPosition['column']>=2:
                dragonPosition['column']-=1
                return dragonPosition
            else:
                return dragonPosition
        else:
            return dragonPosition


def isGameover(userPosition, dungenPosition, dragonPosition):
    if userPosition == dungenPosition:
        return True, 'You win'
    elif userPosition == dragonPosition:
        return True, 'You lose'
    else:
        return False, ''


def main(stdscr):
    curses.curs_set(0)  
    stdscr.nodelay(True)  
    stdscr.timeout(100)  
    
    userPosition = {'row': 0, 'column': 0}
    dragonPosition = {'row': random.randrange(0, 5), 'column': random.randrange(0, 5)}
    dungenPosition = {'row': random.randrange(0, 5), 'column': random.randrange(0, 5)}
    while dragonPosition == dungenPosition:
        dragonPosition = {'row': random.randrange(0, 5), 'column': random.randrange(0, 5)}
    
    while True:
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

        userPosition = getDirection(movement, userPosition)
        showMap(stdscr, userPosition,dragonPosition)
        #dragonPosition=moveDragon(userPosition,dragonPosition,dungenPosition)
        gameover, result = isGameover(userPosition, dungenPosition, dragonPosition)
        if gameover:
            stdscr.addstr(result)
            stdscr.refresh()
            time.sleep(3)
            break



curses.wrapper(main)

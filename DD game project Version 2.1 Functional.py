import curses,random,time

def getDirection(movement='', userPosition={'row':0, 'column':0}):
    if movement == 'up':
        if userPosition['row'] != 0:
            userPosition['row'] -= 1
            return userPosition
        else:
            return userPosition
    elif movement== 'down':
        if userPosition['row'] != 7:
            userPosition['row'] += 1
            return userPosition
        else:
            return userPosition
    elif movement == 'right':
        if userPosition['column'] != 7:
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


def moveDragon(userPosition,dragonPosition,dungenPosition):
    NW=[]
    NE=[]
    SW=[]
    SE=[]
    NEWS=[]
    counter=0
    chance=random.randrange(0,100)
    for row in range (dragonPosition['row']-1,dragonPosition['row']+2):
        for column in range (dragonPosition['column']-1,dragonPosition['column']+2):
            counter+=1
            if counter%2!=0:
                continue   
            if 0<= row<8 and 0<=column <8:
                hearingBlock={'row':row,'column':column}
                if hearingBlock==dragonPosition or hearingBlock==dungenPosition:
                    continue
                
                if row<=dragonPosition['row'] and column<=dragonPosition['column']:
                    NW.append(hearingBlock)
                if row<=dragonPosition['row'] and column>=dragonPosition['column']:
                    NE.append(hearingBlock)
                if row>=dragonPosition['row'] and column<=dragonPosition['column']:
                    SW.append(hearingBlock)
                if row>=dragonPosition['row'] and column>=dragonPosition['column']:
                    SE.append(hearingBlock)

    if userPosition['row']-dragonPosition['row']<0:    
        directOnRow='N'
    else:
        directOnRow='S'
    if  userPosition['column']-dragonPosition['column']<0:
        directOnColumn='W'
    else:
        directOnColumn='E'
    directToGo=directOnRow+directOnColumn

    if abs(userPosition['row']-dragonPosition['row'])<=1 and abs(userPosition['column']-dragonPosition['column'])<=1:        
        if directToGo=='NW':
            if chance>=10 and len(NW)>0:
                bichance=random.randrange(0,len(NW))
                dragonPosition['row']=NW[bichance]['row']
                dragonPosition['column']=NW[bichance]['column']
                return dragonPosition
            else:
                NEWS.extend(NE)
                NEWS.extend(SW)
                NEWS.extend(SE)
                bichance=random.randrange(0,len(NEWS))
                dragonPosition['row']=NEWS[bichance]['row']
                dragonPosition['column']=NEWS[bichance]['column']
                return dragonPosition

        elif directToGo=='NE':
            if chance>=10 and len(NE)>0:
                bichance=random.randrange(0,len(NE))
                dragonPosition['row']=NE[bichance]['row']
                dragonPosition['column']=NE[bichance]['column']
                return dragonPosition
            else:
                NEWS.extend(NW)
                NEWS.extend(SW)
                NEWS.extend(SE)
                bichance=random.randrange(0,len(NEWS))
                dragonPosition['row']=NEWS[bichance]['row']
                dragonPosition['column']=NEWS[bichance]['column']
                return dragonPosition
        
        elif directToGo=='SW':
            if chance>=10 and len(SW)>0:
                bichance=random.randrange(0,len(SW))
                dragonPosition['row']=SW[bichance]['row']
                dragonPosition['column']=SW[bichance]['column']
                return dragonPosition
            else:
                NEWS.extend(NE)
                NEWS.extend(NW)
                NEWS.extend(SE)
                bichance=random.randrange(0,len(NEWS))
                dragonPosition['row']=NEWS[bichance]['row']
                dragonPosition['column']=NEWS[bichance]['column']
                return dragonPosition

        elif directToGo=='SE':
            if chance>=10 and len(SE)>0:
                bichance=random.randrange(0,len(SE))
                dragonPosition['row']=SE[bichance]['row']
                dragonPosition['column']=SE[bichance]['column']
                return dragonPosition
            else:
                NEWS.extend(NE)
                NEWS.extend(SW)
                NEWS.extend(NW)
                bichance=random.randrange(0,len(NEWS))
                dragonPosition['row']=NEWS[bichance]['row']
                dragonPosition['column']=NEWS[bichance]['column']
                return dragonPosition    

    elif abs(userPosition['row']-dragonPosition['row'])<=3 and abs(userPosition['column']-dragonPosition['column'])<=3:      
        if directToGo=='NW':
            if chance>=70 and len(NW)>0:
                bichance=random.randrange(0,len(NW))
                dragonPosition['row']=NW[bichance]['row']
                dragonPosition['column']=NW[bichance]['column']
                return dragonPosition
            else:
                NEWS.extend(NE)
                NEWS.extend(SW)
                NEWS.extend(SE)
                bichance=random.randrange(0,len(NEWS))
                dragonPosition['row']=NEWS[bichance]['row']
                dragonPosition['column']=NEWS[bichance]['column']
                return dragonPosition

        elif directToGo=='NE':
            if chance>=70 and len(NE)>0:
                bichance=random.randrange(0,len(NE))
                dragonPosition['row']=NE[bichance]['row']
                dragonPosition['column']=NE[bichance]['column']
                return dragonPosition
            else:
                NEWS.extend(NW)
                NEWS.extend(SW)
                NEWS.extend(SE)
                bichance=random.randrange(0,len(NEWS))
                dragonPosition['row']=NEWS[bichance]['row']
                dragonPosition['column']=NEWS[bichance]['column']
                return dragonPosition
        
        elif directToGo=='SW':
            if chance>=70 and len(SW)>0:
                bichance=random.randrange(0,len(SW))
                dragonPosition['row']=SW[bichance]['row']
                dragonPosition['column']=SW[bichance]['column']
                return dragonPosition
            else:
                NEWS.extend(NE)
                NEWS.extend(NW)
                NEWS.extend(SE)
                bichance=random.randrange(0,len(NEWS))
                dragonPosition['row']=NEWS[bichance]['row']
                dragonPosition['column']=NEWS[bichance]['column']
                return dragonPosition

        elif directToGo=='SE':
            if chance>=70 and len(SE)>0:
                bichance=random.randrange(0,len(SE))
                dragonPosition['row']=SE[bichance]['row']
                dragonPosition['column']=SE[bichance]['column']
                return dragonPosition
            else:
                NEWS.extend(NE)
                NEWS.extend(SW)
                NEWS.extend(NW)
                bichance=random.randrange(0,len(NEWS))
                dragonPosition['row']=NEWS[bichance]['row']
                dragonPosition['column']=NEWS[bichance]['column']
                return dragonPosition
        
    else: 
        return dragonPosition

def guideMap(mapPosition,dungenPosition):
    
    if dungenPosition['row']-mapPosition['row']<0:    
        directOnRow='N'
    else:
        directOnRow='S'
    if  dungenPosition['column']-mapPosition['column']<0:
        directOnColumn='W'
    else:
        directOnColumn='E'
    directToGo=directOnRow+directOnColumn    

    if directToGo=='NW':
        return 'NW'
    elif directToGo=='NE':
        return 'NE'
    elif directToGo=='SW':
        return 'SW'
    else:
        return 'SE'


def showMap(stdscr, userPosition,dragonPosition,dungenPosition,mapPosition):
    stdscr.clear()
    stdscr.addstr('  Do your move (using cursor keys)\n')
    mapLine = '_'
    dragonAppear=False
    if abs(userPosition['row']-dragonPosition['row'])<=1 and abs(userPosition['column']-dragonPosition['column'])<=1:
        dragonAppear=True
    elif abs(userPosition['row']-dragonPosition['row'])<=2 and abs(userPosition['column']-dragonPosition['column'])<=2:
        stdscr.addstr('!*!*! Be careful!!! Dragon is too near !*!*!')
    
    stdscr.addstr('\n _ _ _ _ _ _ _ _\n')
    for row in range(0, 8):
        stdscr.addstr('|')
        for column in range(0, 8):
            if userPosition['row'] == row and userPosition['column'] == column:
                stdscr.addstr('X')
            elif dragonPosition['row'] == row and dragonPosition['column'] == column and dragonAppear==True:
                stdscr.addstr('D')
            elif mapPosition['row'] == row and mapPosition['column'] == column:
                stdscr.addstr('#')
            else:
                stdscr.addstr(mapLine)
            
            stdscr.addstr('|')
        stdscr.addstr('\n')  

    if userPosition['row']==mapPosition['row'] and userPosition['column']==mapPosition['column']:
        mapMessage=guideMap(mapPosition,dungenPosition)
        if mapMessage=='NW':
            stdscr.addstr('# Guide Map Message: Head to the Pole star find Where the sunflowers go to sleep! #')
        if mapMessage=='NE':
            stdscr.addstr('# Guide Map Message: Seek the UpWorld where the bride rises Thoroughly naked to shine like a star! #') 
        if mapMessage=='SW':
            stdscr.addstr('# Guide Map Message: look back on your shoulder where the devil is resting! #')
        if mapMessage=='SE':
            stdscr.addstr('# Guide Map Message: A hidden path lies to the UnderWorld where the light conquers the darkness! #')

    stdscr.refresh()


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
    mapPosition = {'row': random.randrange(0, 8), 'column': random.randrange(0, 8)}
    dragonPosition = {'row': random.randrange(0, 8), 'column': random.randrange(0, 8)}
    dungenPosition = {'row': random.randrange(0, 8), 'column': random.randrange(0, 8)}
    while dragonPosition == dungenPosition:
        dragonPosition = {'row': random.randrange(0, 8), 'column': random.randrange(0, 8)}
    showMap(stdscr, userPosition,dragonPosition,dungenPosition,mapPosition)
    
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
        if movement != '':
            userPosition = getDirection(movement, userPosition)
            dragonPosition=moveDragon(userPosition,dragonPosition,dungenPosition)
            showMap(stdscr, userPosition,dragonPosition,dungenPosition,mapPosition)
        gameover, result = isGameover(userPosition, dungenPosition, dragonPosition)
        if gameover:
            stdscr.addstr(result)
            stdscr.refresh()
            time.sleep(3)
            break
        time.sleep(0.1)

curses.wrapper(main)
import curses,random,time

class dragon():
    def __init__(self,position,accessableBlocks=[],olfactory=3,hearing=1,sight=False) -> None:
        self.dragonPosition=position
        self.olfactory=olfactory
        self.hearing=hearing
        self.sight=sight
        self.accessableBlocks=accessableBlocks
        self.northwest=[]
        self.northeast=[]
        self.southwest=[]
        self.southeast=[]

    def find_accessable_blocks(self,dungenPosition):
        self.northwest=[]; self.northeast=[]; self.southwest=[]; self.southeast=[]
        counter=0
        for row in range (self.dragonPosition['row']-self.hearing,self.dragonPosition['row']+self.hearing+1):
            for column in range (self.dragonPosition['column']-self.hearing,self.dragonPosition['column']+self.hearing+1):
                counter+=1
                if counter%2!=0:
                    continue   
                if 0<= row<8 and 0<=column <8:
                    hearingBlock={'row':row,'column':column}
                    if hearingBlock==self.dragonPosition or hearingBlock==dungenPosition:
                        continue                
                    if row<=self.dragonPosition['row'] and column<=self.dragonPosition['column']:
                        self.northwest.append(hearingBlock)
                    if row<=self.dragonPosition['row'] and column>=self.dragonPosition['column']:
                        self.northeast.append(hearingBlock)
                    if row>=self.dragonPosition['row'] and column<=self.dragonPosition['column']:
                        self.southwest.append(hearingBlock)
                    if row>=self.dragonPosition['row'] and column>=self.dragonPosition['column']:
                        self.southeast.append(hearingBlock)    
    
    def move_dragon(self,userPosition,directToGo):
        chance=random.randrange(0,100)
        NEWS=[]
        if abs(userPosition['row']-self.dragonPosition['row'])<=self.hearing and abs(userPosition['column']-self.dragonPosition['column'])<=self.hearing:
            accuracyOfSense=90
        elif abs(userPosition['row']-self.dragonPosition['row'])<=self.olfactory and abs(userPosition['column']-self.dragonPosition['column'])<=self.olfactory:
            accuracyOfSense=30
        else:
            accuracyOfSense=-1

        if directToGo=='NW' and accuracyOfSense!=-1 :
            if chance<accuracyOfSense and len(self.northwest)>0:
                bichance=random.randrange(0,len(self.northwest))
                self.dragonPosition['row']=self.northwest[bichance]['row']
                self.dragonPosition['column']=self.northwest[bichance]['column']
            else:
                NEWS.extend(self.northeast)
                NEWS.extend(self.southwest)
                NEWS.extend(self.southeast)
                bichance=random.randrange(0,len(NEWS))
                self.dragonPosition['row']=NEWS[bichance]['row']
                self.dragonPosition['column']=NEWS[bichance]['column']

        elif directToGo=='NE' and accuracyOfSense!=-1:
            if chance<accuracyOfSense and len(self.northeast)>0:
                bichance=random.randrange(0,len(self.northeast))
                self.dragonPosition['row']=self.northeast[bichance]['row']
                self.dragonPosition['column']=self.northeast[bichance]['column']
            
            else:
                NEWS.extend(self.northwest)
                NEWS.extend(self.southwest)
                NEWS.extend(self.southeast)
                bichance=random.randrange(0,len(NEWS))
                self.dragonPosition['row']=NEWS[bichance]['row']
                self.dragonPosition['column']=NEWS[bichance]['column']
        
        elif directToGo=='SW' and accuracyOfSense!=-1:
            if chance<accuracyOfSense and len(self.southwest)>0:
                bichance=random.randrange(0,len(self.southwest))
                self.dragonPosition['row']=self.southwest[bichance]['row']
                self.dragonPosition['column']=self.southwest[bichance]['column']

            else:
                NEWS.extend(self.northeast)
                NEWS.extend(self.northwest)
                NEWS.extend(self.southeast)
                bichance=random.randrange(0,len(NEWS))
                self.dragonPosition['row']=NEWS[bichance]['row']
                self.dragonPosition['column']=NEWS[bichance]['column']

        elif directToGo=='SE' and accuracyOfSense!=-1:
            if chance<accuracyOfSense and len(self.southeast)>0:
                bichance=random.randrange(0,len(self.southeast))
                self.dragonPosition['row']=self.southeast[bichance]['row']
                self.dragonPosition['column']=self.southeast[bichance]['column']
            else:
                NEWS.extend(self.northeast)
                NEWS.extend(self.southwest)
                NEWS.extend(self.northwest)
                bichance=random.randrange(0,len(NEWS))
                self.dragonPosition['row']=NEWS[bichance]['row']
                self.dragonPosition['column']=NEWS[bichance]['column']
    

    def sightDragon(self,userPosition,dungenPosition):
        pass

######################## End of Dragon Class ###############################

class player():
    def __init__(self,userPosition={'row':0,'column':0}) -> None:
        self.userPosition=userPosition
    
    def get_direction(self,movement=''):
        if movement == 'up':
            if self.userPosition['row'] != 0:
                self.userPosition['row'] -= 1
            
        elif movement== 'down':
            if self.userPosition['row'] != 7:
                self.userPosition['row'] += 1

        elif movement == 'right':
            if self.userPosition['column'] != 7:
                self.userPosition['column'] += 1

        elif movement == 'left':
            if self.userPosition['column'] != 0:
                self.userPosition['column'] -= 1

############# End of Player/User Class ##########################


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

    user =player()
    
    mapPosition = {'row': random.randrange(0, 8), 'column': random.randrange(0, 8)}
    
    # شرط برای چک کردن موقعیت اژدها که توی خونه شروع 0و0 قرار نگیره 
    randomRow=random.randrange(0, 8); randomcolumn=random.randrange(0, 8)
    while randomcolumn+randomRow == 0:
        randomRow=random.randrange(0, 8); randomcolumn=random.randrange(0, 8)
    dragonFury=dragon({'row': randomRow, 'column': randomcolumn})

    # شرط برای چک کردن موقعیت دانجن که با موقعیت اژدها یکی نباشه
    dungenPosition = {'row': random.randrange(0, 8), 'column': random.randrange(0, 8)}
    while dragonFury.dragonPosition == dungenPosition:
        dungenPosition = {'row': random.randrange(0, 8), 'column': random.randrange(0, 8)}

    showMap(stdscr, user.userPosition, dragonFury.dragonPosition, dungenPosition, mapPosition)

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
            showMap(stdscr, user.userPosition, dragonFury.dragonPosition, dungenPosition, mapPosition)
        gameover, result = isGameover(user.userPosition, dungenPosition, dragonFury.dragonPosition)
        if gameover:
            stdscr.addstr(result)
            stdscr.refresh()
            time.sleep(3)
            break
        time.sleep(0.1)

curses.wrapper(main)
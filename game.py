from graphics import *
from random import *

def main():
    win = GraphWin('Graphics Window',300,300)
    
    #grid
    vertL= Line(Point(100,0),Point(100,300))
    vertR= Line(Point(200,0),Point(200,300))
    HoriL= Line(Point(0,100),Point(300,100))
    Horir= Line(Point(0,200),Point(300,200))
    
    vertL.draw(win)
    vertR.draw(win)
    HoriL.draw(win)
    Horir.draw(win)
    
    grid = [[Text(Point(50,50), "a1"),Text(Point(50,150), "a2"),Text(Point(50,250), "a3")],[Text(Point(150,50), "b1"),Text(Point(150,150), "b2"),Text(Point(150,250), "b3")],[Text(Point(250,50), "c1"),Text(Point(250,150), "c2"),Text(Point(250,250), "c3")]]
    
    for i in range(3):
        for j in range(3):
            grid[i][j].setSize(30)
    
    
    for i in range(6):
        #player Turn
        wrongMove = True
        while wrongMove==True:
            player = win.getMouse()
            pX = player.getX()
            pY = player.getY()
        #x value
            if pX<=100:
                X=0
            elif pX<=200:
                X=1
            else:
                X=2
        #y value  
            if pY<=100:
                Y=0
            elif pY<=200:
                Y=1
            else:
                Y=2
            
            if grid[X][Y].getText()=='O' or grid[X][Y].getText()=='X':
                wrongMove=True
            else:
                grid[X][Y].setText("O")
                grid[X][Y].draw(win)
                wrongMove=False
        
        #check if player Won
        pWin = False
        if grid[0][0].getText()=='O' and grid[1][0].getText()=='O' and grid[2][0].getText()=='O':
            pWin = True
        if grid[0][1].getText()=='O' and grid[1][1].getText()=='O' and grid[2][1].getText()=='O':
            pWin = True
        if grid[0][2].getText()=='O' and grid[1][2].getText()=='O' and grid[2][2].getText()=='O':
            pWin = True
        if grid[0][0].getText()=='O' and grid[0][1].getText()=='O' and grid[0][2].getText()=='O':
            pWin = True
        if grid[1][0].getText()=='O' and grid[1][1].getText()=='O' and grid[1][2].getText()=='O':
            pWin = True
        if grid[2][0].getText()=='O' and grid[2][1].getText()=='O' and grid[2][2].getText()=='O':
            pWin = True
        if grid[0][0].getText()=='O' and grid[1][1].getText()=='O' and grid[2][2].getText()=='O':
            pWin = True
        if grid[2][0].getText()=='O' and grid[1][1].getText()=='O' and grid[0][2].getText()=='O':
            pWin = True
        else:
            pass
        if pWin == True:
            end = Text(Point(150,150), "Player Win")
            end.setSize(20)
            end.setTextColor("red")
            end.draw(win)
            p = win.getMouse()
            win.close()
            return 0
        elif i == 4: 
            end = Text(Point(150,150), "Draw")
            end.setSize(20)
            end.setTextColor("red")
            end.draw(win)
            p = win.getMouse()
            win.close()
            return 0
        
        #npc Turn
        if i < 1:
            npcWrong=True
            while npcWrong==True:
                npcX = randrange(3)
                npcY = randrange(3)
            
                if grid[npcX][npcY].getText()=='O' or grid[npcX][npcY].getText()=='X':
                    npcWrong=True
                else:
                    grid[npcX][npcY].setText("X")
                    grid[npcX][npcY].draw(win)
                    npcWrong=False
                    
                    
        else:
            #AI Looking to win
            if grid[0][0].getText()!='O' and grid[1][0].getText()=='X' and grid[2][0].getText()=='X':
                grid[0][0].setText("X")
                grid[0][0].draw(win)
            elif grid[0][0].getText()=='X' and grid[1][0].getText()!='O' and grid[2][0].getText()=='X':
                grid[1][0].setText("X")
                grid[1][0].draw(win)
            elif grid[0][0].getText()=='X' and grid[1][0].getText()=='X' and grid[2][0].getText()!='O':
                grid[2][0].setText("X")
                grid[2][0].draw(win)
                
            elif grid[0][1].getText()!='O' and grid[1][1].getText()=='X' and grid[2][1].getText()=='X':
                grid[0][1].setText("X")
                grid[0][1].draw(win)
            elif grid[0][1].getText()=='X' and grid[1][1].getText()!='O' and grid[2][1].getText()=='X':
                grid[1][1].setText("X")
                grid[1][1].draw(win)
            elif grid[0][1].getText()=='X' and grid[1][1].getText()=='X' and grid[2][1].getText()!='O':
                grid[2][1].setText("X")
                grid[2][1].draw(win)
                
            elif grid[0][2].getText()!='O' and grid[1][2].getText()=='X' and grid[2][2].getText()=='X':
                grid[0][2].setText("X")
                grid[0][2].draw(win)
            elif grid[0][2].getText()=='X' and grid[1][2].getText()!='O' and grid[2][2].getText()=='X':
                grid[1][2].setText("X")
                grid[1][2].draw(win)
            elif grid[0][2].getText()=='X' and grid[1][2].getText()=='X' and grid[2][2].getText()!='O':
                grid[2][2].setText("X")
                grid[2][2].draw(win)
                
            elif grid[0][0].getText()!='O' and grid[0][1].getText()=='X' and grid[0][2].getText()=='X':
                grid[0][0].setText("X")
                grid[0][0].draw(win)
            elif grid[0][0].getText()=='X' and grid[0][1].getText()!='O' and grid[0][2].getText()=='X':
                grid[0][1].setText("X")
                grid[0][1].draw(win)
            elif grid[0][0].getText()=='X' and grid[0][1].getText()=='X' and grid[0][2].getText()!='O':
                grid[0][2].setText("X")
                grid[0][2].draw(win)
                
            elif grid[1][0].getText()!='O' and grid[1][1].getText()=='X' and grid[1][2].getText()=='X':
                grid[1][0].setText("X")
                grid[1][0].draw(win)
            elif grid[1][0].getText()=='X' and grid[1][1].getText()!='O' and grid[1][2].getText()=='X':
                grid[1][1].setText("X")
                grid[1][1].draw(win)
            elif grid[1][0].getText()=='X' and grid[1][1].getText()=='X' and grid[1][2].getText()!='O':
                grid[1][2].setText("X")
                grid[1][2].draw(win)
                
            elif grid[2][0].getText()!='O' and grid[2][1].getText()=='X' and grid[2][2].getText()=='X':
                grid[2][0].setText("X")
                grid[2][0].draw(win)
            elif grid[2][0].getText()=='X' and grid[2][1].getText()!='O' and grid[2][2].getText()=='X':
                grid[2][1].setText("X")
                grid[2][1].draw(win)
            elif grid[2][0].getText()=='X' and grid[2][1].getText()=='X' and grid[2][2].getText()!='O':
                grid[2][2].setText("X")
                grid[2][2].draw(win)
                
            elif grid[0][0].getText()!='O' and grid[1][1].getText()=='X' and grid[2][2].getText()=='X':
                grid[0][0].setText("X")
                grid[0][0].draw(win)
            elif grid[0][0].getText()=='X' and grid[1][1].getText()!='O' and grid[2][2].getText()=='X':
                grid[1][1].setText("X")
                grid[1][1].draw(win)
            elif grid[0][0].getText()=='X' and grid[1][1].getText()=='X' and grid[2][2].getText()!='O':
                grid[2][2].setText("X")
                grid[2][2].draw(win)
                
            elif grid[2][0].getText()!='O' and grid[1][1].getText()=='X' and grid[0][2].getText()=='X':
                grid[2][0].setText("X")
                grid[2][0].draw(win)
            elif grid[2][0].getText()=='X' and grid[1][1].getText()!='O' and grid[0][2].getText()=='X':
                grid[1][1].setText("X")
                grid[1][1].draw(win)
            elif grid[2][0].getText()=='X' and grid[1][1].getText()=='X' and grid[0][2].getText()!='O':
                grid[0][2].setText("X")
                grid[0][2].draw(win)
                
        
        #check if NPC Won part 1
        npcWin = False
        if grid[0][0].getText()=='X' and grid[1][0].getText()=='X' and grid[2][0].getText()=='X':
            npcWin = True
        if grid[0][1].getText()=='X' and grid[1][1].getText()=='X' and grid[2][1].getText()=='X':
            npcWin = True
        if grid[0][2].getText()=='X' and grid[1][2].getText()=='X' and grid[2][2].getText()=='X':
            npcWin = True
        if grid[0][0].getText()=='X' and grid[0][1].getText()=='X' and grid[0][2].getText()=='X':
            npcWin = True
        if grid[1][0].getText()=='X' and grid[1][1].getText()=='X' and grid[1][2].getText()=='X':
            npcWin = True
        if grid[2][0].getText()=='X' and grid[2][1].getText()=='X' and grid[2][2].getText()=='X':
            npcWin = True
        if grid[0][0].getText()=='X' and grid[1][1].getText()=='X' and grid[2][2].getText()=='X':
            npcWin = True
        if grid[2][0].getText()=='X' and grid[1][1].getText()=='X' and grid[0][2].getText()=='X':
            npcWin = True
        else:
            pass
        if npcWin == True:
            end = Text(Point(150,150), "Computer Win")
            end.setSize(20)
            end.setTextColor("red")
            end.draw(win)
            p = win.getMouse()
            win.close()
            return 0
        else: 
            pass
        
        
        
        #AI countering player move
            if grid[0][0].getText()!='X' and grid[1][0].getText()=='O' and grid[2][0].getText()=='O':
                grid[0][0].setText("X")
                grid[0][0].draw(win)
            elif grid[0][0].getText()=='O' and grid[1][0].getText()!='X' and grid[2][0].getText()=='O':
                grid[1][0].setText("X")
                grid[1][0].draw(win)
            elif grid[0][0].getText()=='O' and grid[1][0].getText()=='O' and grid[2][0].getText()!='X':
                grid[2][0].setText("X")
                grid[2][0].draw(win)
                
            elif grid[0][1].getText()!='X' and grid[1][1].getText()=='O' and grid[2][1].getText()=='O':
                grid[0][1].setText("X")
                grid[0][1].draw(win)
            elif grid[0][1].getText()=='O' and grid[1][1].getText()!='X' and grid[2][1].getText()=='O':
                grid[1][1].setText("X")
                grid[1][1].draw(win)
            elif grid[0][1].getText()=='O' and grid[1][1].getText()=='O' and grid[2][1].getText()!='X':
                grid[2][1].setText("X")
                grid[2][1].draw(win)
                
            elif grid[0][2].getText()!='X' and grid[1][2].getText()=='O' and grid[2][2].getText()=='O':
                grid[0][2].setText("X")
                grid[0][2].draw(win)
            elif grid[0][2].getText()=='O' and grid[1][2].getText()!='X' and grid[2][2].getText()=='O':
                grid[1][2].setText("X")
                grid[1][2].draw(win)
            elif grid[0][2].getText()=='O' and grid[1][2].getText()=='O' and grid[2][2].getText()!='X':
                grid[2][2].setText("X")
                grid[2][2].draw(win)
                
            elif grid[0][0].getText()!='X' and grid[0][1].getText()=='O' and grid[0][2].getText()=='O':
                grid[0][0].setText("X")
                grid[0][0].draw(win)
            elif grid[0][0].getText()=='O' and grid[0][1].getText()!='X' and grid[0][2].getText()=='O':
                grid[0][1].setText("X")
                grid[0][1].draw(win)
            elif grid[0][0].getText()=='O' and grid[0][1].getText()=='O' and grid[0][2].getText()!='X':
                grid[0][2].setText("X")
                grid[0][2].draw(win)
                
            elif grid[1][0].getText()!='X' and grid[1][1].getText()=='O' and grid[1][2].getText()=='O':
                grid[1][0].setText("X")
                grid[1][0].draw(win)
            elif grid[1][0].getText()=='O' and grid[1][1].getText()!='X' and grid[1][2].getText()=='O':
                grid[1][1].setText("X")
                grid[1][1].draw(win)
            elif grid[1][0].getText()=='O' and grid[1][1].getText()=='O' and grid[1][2].getText()!='X':
                grid[1][2].setText("X")
                grid[1][2].draw(win)
                
            elif grid[2][0].getText()!='X' and grid[2][1].getText()=='O' and grid[2][2].getText()=='O':
                grid[2][0].setText("X")
                grid[2][0].draw(win)
            elif grid[2][0].getText()=='O' and grid[2][1].getText()!='X' and grid[2][2].getText()=='O':
                grid[2][1].setText("X")
                grid[2][1].draw(win)
            elif grid[2][0].getText()=='O' and grid[2][1].getText()=='O' and grid[2][2].getText()!='X':
                grid[2][2].setText("X")
                grid[2][2].draw(win)
                
            elif grid[0][0].getText()!='X' and grid[1][1].getText()=='O' and grid[2][2].getText()=='O':
                grid[0][0].setText("X")
                grid[0][0].draw(win)
            elif grid[0][0].getText()=='O' and grid[1][1].getText()!='X' and grid[2][2].getText()=='O':
                grid[1][1].setText("X")
                grid[1][1].draw(win)
            elif grid[0][0].getText()=='O' and grid[1][1].getText()=='O' and grid[2][2].getText()!='X':
                grid[2][2].setText("X")
                grid[2][2].draw(win)
                
            elif grid[2][0].getText()!='X' and grid[1][1].getText()=='O' and grid[0][2].getText()=='O':
                grid[2][0].setText("X")
                grid[2][0].draw(win)
            elif grid[2][0].getText()=='O' and grid[1][1].getText()!='X' and grid[0][2].getText()=='O':
                grid[1][1].setText("X")
                grid[1][1].draw(win)
            elif grid[2][0].getText()=='O' and grid[1][1].getText()=='O' and grid[0][2].getText()!='X':
                grid[0][2].setText("X")
                grid[0][2].draw(win)
            else:
                if i > 0:
                    npcWrong=True
                    while npcWrong==True:
                        npcX = randrange(3)
                        npcY = randrange(3)
                
                        if grid[npcX][npcY].getText()=='O' or grid[npcX][npcY].getText()=='X':
                            npcWrong=True
                        else:
                            grid[npcX][npcY].setText("X")
                            grid[npcX][npcY].draw(win)
                            npcWrong=False
            
                
        
        #check if NPC Won part 2
        npcWin = False
        if grid[0][0].getText()=='X' and grid[1][0].getText()=='X' and grid[2][0].getText()=='X':
            npcWin = True
        if grid[0][1].getText()=='X' and grid[1][1].getText()=='X' and grid[2][1].getText()=='X':
            npcWin = True
        if grid[0][2].getText()=='X' and grid[1][2].getText()=='X' and grid[2][2].getText()=='X':
            npcWin = True
        if grid[0][0].getText()=='X' and grid[0][1].getText()=='X' and grid[0][2].getText()=='X':
            npcWin = True
        if grid[1][0].getText()=='X' and grid[1][1].getText()=='X' and grid[1][2].getText()=='X':
            npcWin = True
        if grid[2][0].getText()=='X' and grid[2][1].getText()=='X' and grid[2][2].getText()=='X':
            npcWin = True
        if grid[0][0].getText()=='X' and grid[1][1].getText()=='X' and grid[2][2].getText()=='X':
            npcWin = True
        if grid[2][0].getText()=='X' and grid[1][1].getText()=='X' and grid[0][2].getText()=='X':
            npcWin = True
        else:
            pass
        if npcWin == True:
            end = Text(Point(150,150), "Computer Win")
            end.setSize(20)
            end.setTextColor("red")
            end.draw(win)
            p = win.getMouse()
            win.close()
            return 0
        else: 
            pass
                
                
    

main()

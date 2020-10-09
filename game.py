  
from graphics import *
from random import *

def match_screen(win,grid):
    #grid
    vertL= Line(Point(1,0),Point(1,3))
    vertR= Line(Point(2,0),Point(2,3))
    HoriL= Line(Point(0,1),Point(3,1))
    Horir= Line(Point(0,2),Point(3,2))
    
    vertL.draw(win)
    vertR.draw(win)
    HoriL.draw(win)
    Horir.draw(win)

    for i in range(3):
        for j in range(3):
            grid[i][j].setSize(30)  
    pass

def player_turn(win,grid,i):
    #player Turn
    wrongMove = True
    while wrongMove==True:
        player = win.getMouse()
        pX = player.getX()
        pY = player.getY()
    #x value
        if pX<=1:
            X=0
        elif pX<=2:
            X=1
        else:
            X=2
    #y value  
        if pY<=1:
            Y=0
        elif pY<=2:
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
    win_game = win_check( 'O' , "Player " , i, win, grid)
    if win_game == 1:
        return 1
    return 0

def win_check( o_x , p_npc, i,win , grid):
    pWin = False
    if grid[0][0].getText()==o_x and grid[1][0].getText()==o_x and grid[2][0].getText()==o_x:
        pWin = True
    if grid[0][1].getText()==o_x and grid[1][1].getText()==o_x and grid[2][1].getText()==o_x:
        pWin = True
    if grid[0][2].getText()==o_x and grid[1][2].getText()==o_x and grid[2][2].getText()==o_x:
        pWin = True
    if grid[0][0].getText()==o_x and grid[0][1].getText()==o_x and grid[0][2].getText()==o_x:
        pWin = True
    if grid[1][0].getText()==o_x and grid[1][1].getText()==o_x and grid[1][2].getText()==o_x:
        pWin = True
    if grid[2][0].getText()==o_x and grid[2][1].getText()==o_x and grid[2][2].getText()==o_x:
        pWin = True
    if grid[0][0].getText()==o_x and grid[1][1].getText()==o_x and grid[2][2].getText()==o_x:
        pWin = True
    if grid[2][0].getText()==o_x and grid[1][1].getText()==o_x and grid[0][2].getText()==o_x:
        pWin = True
    else:
        pass
    if pWin == True:
        end = Text(Point(1.5,1.5), p_npc + "Win")
        end.setSize(20)
        end.setTextColor("red")
        end.draw(win)
        p = win.getMouse()
        win.close()
        return 1
    elif i == 4: 
        end = Text(Point(1.5,1.5), "Draw")
        end.setSize(20)
        end.setTextColor("red")
        end.draw(win)
        p = win.getMouse()
        win.close()
        return 1
    return 0

def computer_turn(win,grid,i):
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
        #check if computer won at this point
        win_game = win_check( 'X' , "Computer", i ,win , grid)
        if win_game == 1:
            return 1

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
    win_game = win_check( 'X' , "Computer", i ,win , grid)
    if win_game == 1:
        return 1
    return 0


def main():
    win = GraphWin('Graphics Window',300,300)
    win.setCoords(0, 3, 3, 0)
    grid = [[Text(Point(0.5,0.5), "a1"),Text(Point(0.5,1.5), "a2"),Text(Point(0.5,2.5), "a3")],[Text(Point(1.5,0.5), "b1"),Text(Point(1.5,1.5), "b2"),Text(Point(1.5,2.5), "b3")],[Text(Point(2.5,0.5), "c1"),Text(Point(2.5,1.5), "c2"),Text(Point(2.5,2.5), "c3")]]
    #creates the grid for the game
    match_screen(win,grid)
    
    for i in range(6):
        #player Turn
        turn = player_turn(win,grid, i)
        if turn == 1:
            return 1
        
        #npc Turn
        turn = computer_turn(win,grid, i)
        if turn == 1:
            return 1

main()

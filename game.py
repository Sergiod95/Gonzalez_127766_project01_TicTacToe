  
from graphics import *
from random import *


class game_master:
    def __init__(self):
        self.win = GraphWin('Graphics Window',300,300)
        self.win.setCoords(0, 3, 3, 0)
        self.grid = [[Text(Point(0.5,0.5), "a1"),Text(Point(0.5,1.5), "a2"),Text(Point(0.5,2.5), "a3")],[Text(Point(1.5,0.5), "b1"),Text(Point(1.5,1.5), "b2"),Text(Point(1.5,2.5), "b3")],[Text(Point(2.5,0.5), "c1"),Text(Point(2.5,1.5), "c2"),Text(Point(2.5,2.5), "c3")]]
        #creates the grid for the game
        self.number_matches = 0
        self.dificulty = 0
        self.contin = "yes"
        self.pc = player()
        self.npc = computer()

        
    def run_game(self):
        
        while( self.contin == "yes" ):
        
            self.menu_dif()
            if self.number_matches > 0:
                self.reset_screen()
                
            self.number_matches +=1
            self.match_screen()
            for i in range(6):
                #player Turn
                self.pc.player_turn(self.win,self.grid,i)
                turn = self.win_check( self.pc.o_x , self.pc.p_npc, i, self.win , self.grid)
                
                if turn == 1:
                    self.rematch()
                    break
            
                #npc Turn
                self.npc.computer_turn(self.win , self.grid , i , self.dificulty)
                turn =  self.win_check( self.npc.o_x , self.npc.p_npc, i,self.win , self.grid)
                if turn == 1:
                    self.rematch()
                    break
        p = self.win.getMouse()
        self.win.close()
        
    def match_screen(self):
        #grid
        vertL= Line(Point(1,0),Point(1,3))
        vertR= Line(Point(2,0),Point(2,3))
        HoriL= Line(Point(0,1),Point(3,1))
        Horir= Line(Point(0,2),Point(3,2))
    
        vertL.draw(self.win)
        vertR.draw(self.win)
        HoriL.draw(self.win)
        Horir.draw(self.win)

        for i in range(3):
            for j in range(3):
                self.grid[i][j].setSize(30)
                
    def reset_screen(self):
    
        for i in range(3):
            for j in range(3):
                self.grid[i][j].setText("empty")
                self.grid[i][j].undraw()  

    def menu_dif(self):
        
        r = Rectangle(Point(0.5,0.75),Point(2.5,2.25))
        r.setFill("Grey")
        r.setOutline("Black")
        r.draw(self.win)
        menu = Text(Point(1.5, 1),"Dificulty")
        menu.draw(self.win)

        easy = Rectangle(Point(0.65,1.5),Point(1.15,2))
        easy .setFill("White")
        easy .setOutline("Black")
        normal = Rectangle(Point(1.25,1.5),Point(1.75,2))
        normal .setFill("White")
        normal .setOutline("Black")
        hard = Rectangle(Point(1.85,1.5),Point(2.35,2))
        hard .setFill("White")
        hard .setOutline("Black")
        easy.draw(self.win)
        normal.draw(self.win)
        hard.draw(self.win)

        easpoint = easy.getCenter()
        norpoint = normal.getCenter()
        harpoint = hard.getCenter()
    
        eas = Text(easpoint,"Easy")
        eas.setTextColor("Black")
        eas.draw(self.win)
        norml = Text(norpoint,"Normal")
        norml.setTextColor("Black")
        norml.draw(self.win)
        har = Text(harpoint,"Hard")
        har.setTextColor("Black")
        har.draw(self.win)

        while True:
            p = self.win.getMouse()
            if p.getX()>0.65 and p.getX()<1.15 and p.getY()>1.5 and p.getY()<2:
                self.dificulty = 0
                break
            elif p.getX()>1.25 and p.getX()<1.75 and p.getY()>1.5 and p.getY()<2:
                self.dificulty = 1
                break
            elif p.getX()>1.85 and p.getX()<2.15 and p.getY()>1.5 and p.getY()<2:
                self.dificulty = 2
                break
        r.undraw()
        menu.undraw()
        easy.undraw()
        normal.undraw()
        hard.undraw()
        eas.undraw()
        norml.undraw()
        har.undraw()

    def rematch(self):
    
        r = Rectangle(Point(0.5,0.75),Point(2.5,2.25))
        r.setFill("Grey")
        r.setOutline("Black")
        r.draw(self.win)
        rematch = Text(Point(1.5, 1),"Rematch?")
        rematch.draw(self.win)

        y_b = Rectangle(Point(0.75,1.5),Point(1.25,2))
        y_b .setFill("White")
        y_b .setOutline("Black")
        n_b = Rectangle(Point(1.75,1.5),Point(2.25,2))
        n_b .setFill("White")
        n_b .setOutline("Black")
        y_b.draw(self.win)
        n_b.draw(self.win)

        ypoint = y_b.getCenter()
        npoint = n_b.getCenter()
    
        yes = Text(ypoint,"Yes")
        yes.setTextColor("Black")
        yes.draw(self.win)
        no = Text(npoint,"No")
        no.setTextColor("Black")
        no.draw(self.win)

        while True:
            p = self.win.getMouse()
            if p.getX()>0.75 and p.getX()<1.25 and p.getY()>1.5 and p.getY()<2:
                self.contin = "yes"
                break
            elif p.getX()>1.75 and p.getX()<2.25 and p.getY()>1.5 and p.getY()<2:
                self.contin = "no"
                break
        r.undraw()
        rematch.undraw()
        y_b.undraw()
        n_b.undraw()
        yes.undraw()
        no.undraw()

    def win_check( self, o_x , p_npc, i,win , grid):
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
            end.undraw()
            return 1
        elif i == 4: 
            end = Text(Point(1.5,1.5), "Draw")
            end.setSize(20)
            end.setTextColor("red")
            end.draw(win)
            p = win.getMouse()
            end.undraw()
            return 1
        return 0

    
class player:
    def __init__(self):
        self.o_x = "O"
        self.p_npc = "Player"
        

    def player_turn(self,win,grid,i):
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
        return 0

class computer:
    def __init__(self):
        self.o_x = "X"
        self.p_npc = "Computer"

    def computer_turn(self, win,grid,i,dificulty):
        move = False
        if i ==0 or dificulty==0:
            move = True
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
                move = True
            elif grid[0][0].getText()=='X' and grid[1][0].getText()!='O' and grid[2][0].getText()=='X':
                grid[1][0].setText("X")
                grid[1][0].draw(win)
                move = True
            elif grid[0][0].getText()=='X' and grid[1][0].getText()=='X' and grid[2][0].getText()!='O':
                grid[2][0].setText("X")
                grid[2][0].draw(win)
                move = True
                    
            elif grid[0][1].getText()!='O' and grid[1][1].getText()=='X' and grid[2][1].getText()=='X':
                grid[0][1].setText("X")
                grid[0][1].draw(win)
                move = True
            elif grid[0][1].getText()=='X' and grid[1][1].getText()!='O' and grid[2][1].getText()=='X':
                grid[1][1].setText("X")
                grid[1][1].draw(win)
                move = True
            elif grid[0][1].getText()=='X' and grid[1][1].getText()=='X' and grid[2][1].getText()!='O':
                grid[2][1].setText("X")
                grid[2][1].draw(win)
                move = True
                    
            elif grid[0][2].getText()!='O' and grid[1][2].getText()=='X' and grid[2][2].getText()=='X':
                grid[0][2].setText("X")
                grid[0][2].draw(win)
                move = True
            elif grid[0][2].getText()=='X' and grid[1][2].getText()!='O' and grid[2][2].getText()=='X':
                grid[1][2].setText("X")
                grid[1][2].draw(win)
                move = True
            elif grid[0][2].getText()=='X' and grid[1][2].getText()=='X' and grid[2][2].getText()!='O':
                grid[2][2].setText("X")
                grid[2][2].draw(win)
                move = True
                    
            elif grid[0][0].getText()!='O' and grid[0][1].getText()=='X' and grid[0][2].getText()=='X':
                grid[0][0].setText("X")
                grid[0][0].draw(win)
                move = True
            elif grid[0][0].getText()=='X' and grid[0][1].getText()!='O' and grid[0][2].getText()=='X':
                grid[0][1].setText("X")
                grid[0][1].draw(win)
                move = True
            elif grid[0][0].getText()=='X' and grid[0][1].getText()=='X' and grid[0][2].getText()!='O':
                grid[0][2].setText("X")
                grid[0][2].draw(win)
                move = True
                    
            elif grid[1][0].getText()!='O' and grid[1][1].getText()=='X' and grid[1][2].getText()=='X':
                grid[1][0].setText("X")
                grid[1][0].draw(win)
                move = True
            elif grid[1][0].getText()=='X' and grid[1][1].getText()!='O' and grid[1][2].getText()=='X':
                grid[1][1].setText("X")
                grid[1][1].draw(win)
                move = True
            elif grid[1][0].getText()=='X' and grid[1][1].getText()=='X' and grid[1][2].getText()!='O':
                grid[1][2].setText("X")
                grid[1][2].draw(win)
                move = True
                    
            elif grid[2][0].getText()!='O' and grid[2][1].getText()=='X' and grid[2][2].getText()=='X':
                grid[2][0].setText("X")
                grid[2][0].draw(win)
                move = True
            elif grid[2][0].getText()=='X' and grid[2][1].getText()!='O' and grid[2][2].getText()=='X':
                grid[2][1].setText("X")
                grid[2][1].draw(win)
                move = True
            elif grid[2][0].getText()=='X' and grid[2][1].getText()=='X' and grid[2][2].getText()!='O':
                grid[2][2].setText("X")
                grid[2][2].draw(win)
                move = True
                    
            elif grid[0][0].getText()!='O' and grid[1][1].getText()=='X' and grid[2][2].getText()=='X':
                grid[0][0].setText("X")
                grid[0][0].draw(win)
                move = True
            elif grid[0][0].getText()=='X' and grid[1][1].getText()!='O' and grid[2][2].getText()=='X':
                grid[1][1].setText("X")
                grid[1][1].draw(win)
                move = True
            elif grid[0][0].getText()=='X' and grid[1][1].getText()=='X' and grid[2][2].getText()!='O':
                grid[2][2].setText("X")
                grid[2][2].draw(win)
                move = True
                    
            elif grid[2][0].getText()!='O' and grid[1][1].getText()=='X' and grid[0][2].getText()=='X':
                grid[2][0].setText("X")
                grid[2][0].draw(win)
                move = True
            elif grid[2][0].getText()=='X' and grid[1][1].getText()!='O' and grid[0][2].getText()=='X':
                grid[1][1].setText("X")
                grid[1][1].draw(win)
                move = True
            elif grid[2][0].getText()=='X' and grid[1][1].getText()=='X' and grid[0][2].getText()!='O':
                grid[0][2].setText("X")
                grid[0][2].draw(win)
                move = True
            elif dificulty == 1:
                if i > 0:
                    move = True
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
            
            if move == True:
                return 1

        #AI countering player move
            if dificulty == 2:
                if grid[0][0].getText()!='X' and grid[1][0].getText()=='O' and grid[2][0].getText()=='O':
                    grid[0][0].setText("X")
                    grid[0][0].draw(win)
                    move = True
                elif grid[0][0].getText()=='O' and grid[1][0].getText()!='X' and grid[2][0].getText()=='O':
                    grid[1][0].setText("X")
                    grid[1][0].draw(win)
                    move = True
                elif grid[0][0].getText()=='O' and grid[1][0].getText()=='O' and grid[2][0].getText()!='X':
                    grid[2][0].setText("X")
                    grid[2][0].draw(win)
                    move = True
                    
                elif grid[0][1].getText()!='X' and grid[1][1].getText()=='O' and grid[2][1].getText()=='O':
                    grid[0][1].setText("X")
                    grid[0][1].draw(win)
                    move = True
                elif grid[0][1].getText()=='O' and grid[1][1].getText()!='X' and grid[2][1].getText()=='O':
                    grid[1][1].setText("X")
                    grid[1][1].draw(win)
                    move = True
                elif grid[0][1].getText()=='O' and grid[1][1].getText()=='O' and grid[2][1].getText()!='X':
                    grid[2][1].setText("X")
                    grid[2][1].draw(win)
                    move = True
                    
                elif grid[0][2].getText()!='X' and grid[1][2].getText()=='O' and grid[2][2].getText()=='O':
                    grid[0][2].setText("X")
                    grid[0][2].draw(win)
                    move = True
                elif grid[0][2].getText()=='O' and grid[1][2].getText()!='X' and grid[2][2].getText()=='O':
                    grid[1][2].setText("X")
                    grid[1][2].draw(win)
                    move = True
                elif grid[0][2].getText()=='O' and grid[1][2].getText()=='O' and grid[2][2].getText()!='X':
                    grid[2][2].setText("X")
                    grid[2][2].draw(win)
                    move = True
                    
                elif grid[0][0].getText()!='X' and grid[0][1].getText()=='O' and grid[0][2].getText()=='O':
                    grid[0][0].setText("X")
                    grid[0][0].draw(win)
                    move = True
                elif grid[0][0].getText()=='O' and grid[0][1].getText()!='X' and grid[0][2].getText()=='O':
                    grid[0][1].setText("X")
                    grid[0][1].draw(win)
                    move = True
                elif grid[0][0].getText()=='O' and grid[0][1].getText()=='O' and grid[0][2].getText()!='X':
                    grid[0][2].setText("X")
                    grid[0][2].draw(win)
                    move = True
                    
                elif grid[1][0].getText()!='X' and grid[1][1].getText()=='O' and grid[1][2].getText()=='O':
                    grid[1][0].setText("X")
                    grid[1][0].draw(win)
                    move = True
                elif grid[1][0].getText()=='O' and grid[1][1].getText()!='X' and grid[1][2].getText()=='O':
                    grid[1][1].setText("X")
                    grid[1][1].draw(win)
                    move = True
                elif grid[1][0].getText()=='O' and grid[1][1].getText()=='O' and grid[1][2].getText()!='X':
                    grid[1][2].setText("X")
                    grid[1][2].draw(win)
                    move = True
                    
                elif grid[2][0].getText()!='X' and grid[2][1].getText()=='O' and grid[2][2].getText()=='O':
                    grid[2][0].setText("X")
                    grid[2][0].draw(win)
                    move = True
                elif grid[2][0].getText()=='O' and grid[2][1].getText()!='X' and grid[2][2].getText()=='O':
                    grid[2][1].setText("X")
                    grid[2][1].draw(win)
                    move = True
                elif grid[2][0].getText()=='O' and grid[2][1].getText()=='O' and grid[2][2].getText()!='X':
                    grid[2][2].setText("X")
                    grid[2][2].draw(win)
                    move = True
                    
                elif grid[0][0].getText()!='X' and grid[1][1].getText()=='O' and grid[2][2].getText()=='O':
                    grid[0][0].setText("X")
                    grid[0][0].draw(win)
                    move = True
                elif grid[0][0].getText()=='O' and grid[1][1].getText()!='X' and grid[2][2].getText()=='O':
                    grid[1][1].setText("X")
                    grid[1][1].draw(win)
                    move = True
                elif grid[0][0].getText()=='O' and grid[1][1].getText()=='O' and grid[2][2].getText()!='X':
                    grid[2][2].setText("X")
                    grid[2][2].draw(win)
                    move = True
                    
                elif grid[2][0].getText()!='X' and grid[1][1].getText()=='O' and grid[0][2].getText()=='O':
                    grid[2][0].setText("X")
                    grid[2][0].draw(win)
                    move = True
                elif grid[2][0].getText()=='O' and grid[1][1].getText()!='X' and grid[0][2].getText()=='O':
                    grid[1][1].setText("X")
                    grid[1][1].draw(win)
                    move = True
                elif grid[2][0].getText()=='O' and grid[1][1].getText()=='O' and grid[0][2].getText()!='X':
                    grid[0][2].setText("X")
                    grid[0][2].draw(win)
                    move = True
                elif dificulty == 2:
                    if i > 0:
                        move = True
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
       
                if move == True:
                    return 1
                return 0





def main():
    gm = game_master()
    gm.run_game()
    
    

main()

def main():
    win = GraphWin('Graphics Window',300,300)
    wcircle = Circle(Point(150, 150), 100)
    wcircle.setOutline("black")
    wcircle.setFill("white")
    wcircle.draw(win)
    
    bcircle = Circle(Point(150,150), 80)
    bcircle.setOutline("black")
    bcircle.setFill("black")
    bcircle.draw(win)
    
    blcircle = Circle(Point(150, 150), 60)
    blcircle.setOutline("black")
    blcircle.setFill("blue")
    blcircle.draw(win)
    
    rcircle = Circle(Point(150, 150), 40)
    rcircle.setOutline("black")
    rcircle.setFill("red")
    rcircle.draw(win)
    
    ycircle = Circle(Point(150, 150), 20)
    ycircle.setOutline("black")
    ycircle.setFill("yellow")
    ycircle.draw(win)
    pass

main()from graphics import *

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
    
    #a1 = Text(Point(50,50), "a1")
    ###a2 = Text(Point(50,150), "a2")
    ##a3 = Text(Point(50,250), "a3")
    #b1 = Text(Point(150,50), "b1")
    #b2 = Text(Point(150,150), "b2")
    #b3 = Text(Point(150,250), "b3")
    #c1 = Text(Point(250,50), "c1")
    #c2 = Text(Point(250,150), "c2")
    #c3 = Text(Point(250,250), "c3")
    
    #a1.draw(win)
    #a2.draw(win)
    #a3.draw(win)
    #b1.draw(win)
    #b2.draw(win)
    #b3.draw(win)
    #c1.draw(win)
    #c2.draw(win)
    #c3.draw(win)
    
    
    grid = [[Text(Point(50,50), "a1"),Text(Point(50,150), "a2"),Text(Point(50,250), "a3")],[Text(Point(150,50), "b1"),Text(Point(150,150), "b2"),Text(Point(150,250), "b3")],[Text(Point(250,50), "c1"),Text(Point(250,150), "c2"),Text(Point(250,250), "c3")]]
    
    for i in range(9):
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
            
            if grid[X][Y].getText()=='O':
                wrongMove=True
            else:
                grid[X][Y].setText("O")
                grid[X][Y].draw(win)
                wrongMove=False
        
    
    a = win.getMouse()
    win.close()
    pass

main()

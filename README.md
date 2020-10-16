# TicTacToe Game

This is the classic came of TicTacToe it doesn't use any outside functions considering it was the first version of the progarm.
In the game the player is the 'O' and the computer is the 'X', the computer is programed to pick a random spot at the start then it will try to block the victory of the player
or it will try to win with three in a row, in case the computer can't block or win the game it will pick a random possition again. the game is programed to check if the the player or the computer won after each move. the game ends after ether the player or the computer wins or in some cases it ends in draw.

# Branch B (game_functions)

The updated versions uses functions in order to reduce the size of the main and make it more functional and easy to debug.

The menu_dif(win,dificulty) is used to draw and later undraw a menu to choose the dificulty of the game being easy
(the computer pick random places), normal(the computer try to block the player victory), and hard(the original dificulty of the game where the computer will block and try to win the game).

match_screen(win,grid) will create the screen with the grid for the player and the cumputer to play.

reset_screen(win,grid) will erase and reset the game screen and the inportant variables in order to play again.

player_turn(win,grid, i) is the function that lets the player play is turn, it will stop the player from making incorrect moves, at the end the function would check if the player won the game.

computer_turn(win,grid, i,dificulty) is the functions that plays for the computer, it varies depending on the dificulty that the player chose. it is the longest function because it evaluates all the possible situations. it will evaluate if the computer won at the end of it's move.

rematch(win,contin_playing) is a menu that ask the user if it wants to play again, if the answer is "Yes" then the program would start from the begining runing the function reset_screen(win,grid) in order to clean the screen from last match.

win_check() is used to see if there are the same symbols in a row and declare the winner of the game or the draw if needed.

# Branch C (game_classes)

another updated version of the game this time is organized in classes/objects.

the prinsipal class is the game_master(), the game_master() or gm uses the same functions that were used in the Branch B(gmae_functions) but adapted to be used in an object.

the gm has to more objects inside being the class player and the class computer, this two classes has their own function of turn that are similar to the function player_turn() and computer_turn(); however, the win_check() is a function of the class game_master() and it require the principal variables of the player and computer in order to verify

the lenght of the main in this code was reduced to just two lines having most of the process in the object gm.

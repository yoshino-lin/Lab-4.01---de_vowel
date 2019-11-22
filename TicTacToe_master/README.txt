# Project-4-Tic-Tac-Toe
Finally, let's play OOXX!

Using Python, students will create a Tic-Tac-Toe game. This project has two parts:

Designing the game so that two users can play Tic-Tac-Toe against one another.
Creating a Tic-Tac-Toe checker which will check the board to see if Xs or Os have won the game.
Overview
Tic-Tac-Toe (Links to an external site.)Links to an external site. is a game in which one player draws X's and another player draws O's inside a set of nine squares and each player tries to be the first to fill a row, column, or diagonal of squares with either X's or O's. We will be writing an interactive Tic-Tac-Toe program. At the end of each turn the computer will check to see if X's have won the game or if the O's have won the game.

Behavior
The program will prompt the user to enter their name and their opponents name.
Whoever enters their name first will be playing as X's, and the other player will be O's.
The players will take turns inputting the row and column they would like to place their mark.
If that spot is already taken the program will ask for the spot again.
At the end of each player's turn the program will check if that player has won.
At the end of each player's turn the program will print the updated game board.
If there are no more spots open and nobody has won the game, the program will print Tie game!.
Implementation Details
Use variables to store the user names for personalized prompts.
Create a game board represented as a list of lists, size 3 by 3. Note: This is a change from our earlier implementations of Tic-Tac-Toe. Why do you think this might be better?
Check for a winner horizontally, vertically, and on both diagonals.
Cannot allow a user to overwrite a spot on the board.
Stretch Assignments
Here are some stretch assignments you can attempt if you've finished the base functionality early. You can earn a bonus of 5 points for implementing one of these. (A total of 5 points, not 5 points per option)

At the start of the game, allow the player to choose board size. Odd numbers only (Evens make it difficult to do diagonal win conditions). If you've written your win condtions well, you shouldn't have to redesign a lot here. If you find yourself doing a lot of rewriting, try to think of a better way to calculate win conditions.]
Create a computer player that picks random position that hasn't already been chosen each turn.
Create a better computer player that tries to block any 3 in a row, but picks a random spot if there are no 2-in-a rows available to block
Rubric
Tic Tac Toe Project
Tic Tac Toe Project
Criteria	Ratings	Pts
This criterion is linked to a Learning Outcome Program prompts user for name
2.0 pts
Full Marks
0.0 pts
No Marks
2.0 pts
This criterion is linked to a Learning Outcome Program marks board where user requested
5.0 pts
Full Marks
0.0 pts
No Marks
5.0 pts
This criterion is linked to a Learning Outcome Program prints a readable board after user's turn
5.0 pts
Full Marks
0.0 pts
No Marks
5.0 pts
This criterion is linked to a Learning Outcome Program won't overwrite value on board
5.0 pts
Full Marks
0.0 pts
No Marks
5.0 pts
This criterion is linked to a Learning Outcome Program reports who won or if there was a tie
15.0 pts
Full Marks
0.0 pts
No Marks
15.0 pts
This criterion is linked to a Learning Outcome Program ends after a win, loss, or tie
3.0 pts
Full Marks
0.0 pts
No Marks
3.0 pts
This criterion is linked to a Learning Outcome Correct use of game loop
5.0 pts
Full Marks
0.0 pts
No Marks
5.0 pts
This criterion is linked to a Learning Outcome Correctly indexes into lists of lists to store board
5.0 pts
Full Marks
0.0 pts
No Marks
5.0 pts
This criterion is linked to a Learning Outcome Correctly check board for mark
5.0 pts
Full Marks
0.0 pts
No Marks
5.0 pts
This criterion is linked to a Learning Outcome Check for winners on all three horizontals and verticals
20.0 pts
Full Marks
0.0 pts
No Marks
20.0 pts
This criterion is linked to a Learning Outcome Checks for winners on both diagonals
10.0 pts
Full Marks
0.0 pts
No Marks
10.0 pts
Total Points: 80.0

import os
from helpers import check_turn, check_for_win, draw_board

'''
Each player will pick a number from 1 to 9 and replace it with X or O and then the board will have to be printed again.
The helpers function file was made to easily call the new printed board.
'''
spots = {1 : '1', 2 : '2', 3: '3', 4 : '4', 5 : '5', 
         6 : '6', 7 : '7',  8 : '8', 9 : '9'}
playing, complete = True, False
turn = 0
prev_turn = -1
'''
Game Loop is created and the os module is added to reset the screen so we don't have a new board drawn every time a player makes a move. 
'''
while playing:
    
    os.system('cls' if os.name == 'nt' else 'clear')
     
    draw_board(spots)
    if prev_turn == turn:
      print("Invalid spot selected, please pick another.")
    prev_turn = turn
    print("Player " + str((turn % 2) +1 ) + "'s turn: Pick your spot or press q to quit")
    
     
    choice = input()
     
    if choice == 'q':
        playing = False
    elif str.isdigit(choice) and int(choice) in spots:

      if not spots[int(choice)] in {"X", "O"}:
         
        turn += 1
        spots[int(choice)] = check_turn(turn)
      
     
    if check_for_win(spots): playing, complete = False, True
    if turn > 8: playing = False
    
  
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)
 
if complete:
  if check_turn(turn) == 'X': print("Player 1 Wins!!!")
  else: print("Player 2 Wins!!!")
else: 
   
  print("It's a tie!")
  
print("Thanks 4 playing!") 

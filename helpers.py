'''
The newline character (\n) in the formedeed string is added after 3 numbers on the board str to move down to the next row.
The variable spots[number] it's called from the dictionary on the main file.
'''   
def draw_board(spots):
  board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
             f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f"|{spots[7]}|{spots[8]}|{spots[9]}|")
  print(board)

'''
The module operator (%) is used to keep track of whom is playing 
by using even and odd numbers.
'''
def check_turn(turn):
  if turn % 2 == 0: return 'O'
  else: return 'X'
''' 
Defining the next blocks of code for winners 
on the horizonal, vertical and diagonal cases
'''
def check_for_win(spots):
   
  if   (spots[1] == spots[2] == spots[3]) \
    or (spots[4] == spots[5] == spots[6]) \
    or (spots[7] == spots[8] == spots[9]):
    return True
   
  elif   (spots[1] == spots[4] == spots[7]) \
    or (spots[2] == spots[5] == spots[8]) \
    or (spots[3] == spots[6] == spots[9]):
    return True
   
  elif (spots[1] == spots[5] == spots[9]) \
    or (spots[3] == spots[5] == spots[7]):
    return True
    
  else: return False

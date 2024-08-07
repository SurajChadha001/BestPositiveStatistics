def nextMove(posr, posc, board):
  for i in range(5):
    for j in range(5):
      if board[i][j] == 'd':
        dirty_r, dirty_c = i, j
        break
  if posr<dirty_r:
    print("Down")
  elif posr > dirty_r:
    print("UP")
  elif posc < dirty_c:
    print("RIGHT")
  elif posc > dirty_c:
    print("LEFT")
  else:
    print("CLEAN")
posr, posc = 0, 0
board = [
     "b---d",
      "-----",
      "-----",
      "-----",
      "-----"
]

  # Call the function with sample input
  nextMove(posr, posc, board)
  
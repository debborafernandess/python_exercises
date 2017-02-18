board = { 'top-l': '   ', 'top-m': '   ', 'top-r': '   ',
          'mid-l': '   ', 'mid-m': '   ', 'mid-r': '   ',
          'low-l': '   ', 'low-m': '   ', 'low-r': '   ' }

def avaliablePositions():
  print('Positions: %s' % ', '.join(board.keys()) )


def printBoard(board):
  lines = ['top', 'mid', 'low']

  avaliablePositions()
  for y in lines:
    print(board[y+'-l'] + '|' + board[y+'-m'] + '|' + board[y+'-r'])
    if y != 'low':
      print('___ ___ ___')


def changeTurn(turn):
  if turn == 'X':
    return 'O'
  else:
    return 'X'


def game():
  turn = 'X'
  printBoard(board)

  for i in range(9):
    print('\n Turn of %s. Choose your position: ' % turn)
    move = input()

    if move == 'exit':
      break
    elif not board[move].isspace():
      print('Essa jogada já foi feita')
      continue
    else:
      board[move] = ' ' + turn + ' '
      turn = changeTurn(turn)

    printBoard(board)

# Run Game
game()
print('Vc saiu do jogo! Até a próxima!')

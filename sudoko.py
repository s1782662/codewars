import numpy as np

board = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]

'''
def DoneorNot(board):
    # row wise
    board_row_length = len(board)
    for i in range(board_row_length):
        if len(board[i]) != len(set(board[i])):
            return 'Try again'

    def get_column(board,column_no):
        return [row[i] for row in board]

    for i in range(board_row_length):
        elem = get_column(board,i)
        if len(elem) != len(set(elem)):
            return 'Try again'

    offset = 3
    board = np.array(board)
    def check_size(sub_section):
        r,c = sub_section.shape
        if r*c != len(np.unique(sub_section)):
            return False
        return True

    for i in range(0,9,3):
        for j in range(0,9,3):
            if not check_size(board[i:i+offset,j:j+offset]):
                return 'Try again'

    return 'Finished'
# column wise
'''



def done_or_not(aboard): #board[i][j]
  board = np.array(aboard)

  rows = [board[i,:] for i in range(9)]
  print(rows,'\n')
  cols = [board[:,j] for j in range(9)]
  print(cols,'\n')
  sqrs = [board[i:i+3,j:j+3].flatten() for i in [0,3,6] for j in [0,3,6]]
  print(sqrs,'\n')
  print(np.vstack((rows,cols,sqrs)))
  for view in np.vstack((rows,cols,sqrs)):
      if len(np.unique(view)) != 9:
          return 'Try again!'

  return 'Finished!'


print(done_or_not(board))

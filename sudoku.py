import random

def solveBoard(board):
    c=1
    while unsolved(board) and c<5:
        board=try_pass(board, c)
        c+=1
    return board

def try_pass(board, c):
    base_board=copy(board)
    unchange=True
    while unchange and unsolved(board):
        unchange=False
        for row in range(9):
            for col in range(9):
                if board[row][col] is None:
                    av=available(row, col, board)
                    if len(av) <= c and len(av) != 0:
                        r=random.randint(0,len(av)-1)
                        board[row][col]=av[r]
                        unchange=True   
                    elif len(av) == 0:
                        board=copy(base_board) 
                        unchange=True
    return board

def available(i,j,board):
    row=inRow(i,board)
    col=inCol(j,board)
    cell=inCell(i,j,board)
    open=[1,2,3,4,5,6,7,8,9]
    for l in row:
        open.remove(l)
    for l in col:
        if l in open:
            open.remove(l)
    for l in cell:
        if l in open:
            open.remove(l)
    return open

def inCell(i,j,board):
    taken=[]
    row=int(i/3)*3
    col=int(j/3)*3
    for x in range(row, row+3):
        for y in range(col, col+3):
            if(board[x][y] is not None):
                taken.append(board[x][y])
    return taken

def inRow(i,board):
    taken=[]
    for n in board[i]:
        if n is not None:
            taken.append(n)
    return taken

def inCol(j,board):
    taken=[]
    for n in board:
        if n[j] is not None:
            taken.append(n[j])
    return taken

def shortest(one, two, three):
    if len(one) < len(two) and len(one) < len(three):
        return one
    elif len(two)<len(three) and len(two)<len(one):
        return two
    else:
        return three

def unsolved(board):
    for n in board:
        if None in n:
            return True
    return False

def copy(board):
    re=[]
    for n in range(len(board)):
        re.append([])
        for l in board[n]:
            re[n].append(l)
    return re

board= [[None,  3,      None,   6,      None,   5,      None,   None,   4],
        [7,     None,   None,   None,   None,   None,   None,   3,      None],
        [None,  None,   None,   None,   None,   4,      None,   None,   None],
        [None,  None,   None,   4,      None,   3,      1,      None,   None],
        [None,  None,   9,      None,   None,   None,   6,      None,   None],
        [8,     None,   None,   None,   2,      None,   None,   None,   None],
        [None,  None,   None,   None,   None,   None,   None,   None,   9],
        [None,  1,      5,      None,   None,   None,   None,   8,      None],
        [None,  None,   None,   None,   9,      None,   None,   5,      2]]


board2=[[None, None,   None,   None,   2,      None,   5,      6,      8],
        [None,  None,   None,   None,   None,   None,   None,   None,   None],
        [None,  8,      7,      9,      1,      None,   3,      4,      2],
        [4,     7,      None,   1,      3,      None,   None,   None,   None],
        [None,  6,      2,      None,   9,      None,   None,   None,   None],
        [None,  3,      None,   7,      6,      None,   2,      1,      None],
        [None,  None,   5,      8,      None,   None,   None,   2,      6],
        [7,     None,   None,   3,      None,   9,      8,      5,      None],
        [8,     9,      1,      2,      5,      None,   None,   None,   3]]

print(solveBoard(board))
# print(inCell(8, 5, board2))
# print(inRow(8, board2))
# print(inCol(5, board2))
# print(available(8, 5, board2))

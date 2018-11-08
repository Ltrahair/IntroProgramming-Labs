# CMPT 120 Intro to Programming
# Lab #7 – Tic tac toe
# Author: Linus Trahair
# Created: 2018-11-8
symbol = [ " ", "x", "o" ]
board= [[0,0,0],[0,0,0],[0,0,0]]
player=1
def printRow(row):
    print("|",symbol[row[0]],"|",symbol[row[1]],"|",symbol[row[2]],"|")
def printBoard(board):
    for i in board:
        print("+-----------+")
        printRow(i)
    print("+-----------+")
def markBoard(row, col, player):
    global board
    if not board[col][row]>0:
        board[col][row]=player
    
 # check to see whether the desired square is blank
 # if so, set it to the player number
def getPlayerMove():
 r=input("which row?\n")
 print()
 c=input("which column?\n")# prompt the user separately for the row and column numbers
 return (int(c),int(r)) # then return that row and column instead of (0,0)
def hasBlanks(board):
    for b in board:
        if 0 in b:
            return True
    return False
def checkRows(board):
    for row in board:
        if row[0]==row[1] and row[1]==row[2] and not row[0]==0:
            return True
    return False
def checkColumn(board):
    if board[0][0]==board[1][0] and board[1][0]==board[2][0] and not board[0][0]==0:
        return True
    elif board[0][1]==board[1][1] and board[1][1]==board[2][1] and not board[0][1]==0:
        return True
    elif board[0][0]==board[1][2] and board[1][2]==board[2][2] and not board[0][2]==0:
        return True
    else:
        return False
def checkDiag(board):
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and not board[0][0]==0:
        return True
    elif board[0][2]==board[1][1] and board[1][1]==board[2][0] and not board[1][1]==0:
        return True
    else:
        return False
def checkWinner(board):
    global player
    if checkRows(board) or checkColumn(board) or checkDiag(board):
        if player==1:
            print("p2 wins")
        else:
            print("p1 wins")
        return True
    else:
        return False
def main():
    global player
# TODO replace this with a three-by-three matrix of zeros
    player = 1
    win=False
    while hasBlanks(board):
    
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(row,col,player)
        player = player % 2 + 1 # switch player for next turn
        win=checkWinner(board)
        if win:
            break
        
main()

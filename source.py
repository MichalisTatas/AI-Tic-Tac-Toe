from board import *
from math import inf

def getSuccessorStates(myBoard, player):
    if player == 'human':
        symbol = 'X'
    else:
        symbol = 'O'
    successorStates = []
    tempBoard = myBoard.copy()
    i=0
    while i<9:
        if tempBoard[i] == ' ': 
            tempBoard[i] = symbol
            successorStates.append(tempBoard)
            tempBoard=myBoard.copy()
        i = i+1
    return successorStates


def isDrawTest(b):
    if (b[0] != ' ' and b[1] != ' ' and b[2] != ' ' and
        b[3] != ' ' and b[4] != ' ' and b[5] != ' ' and
        b[6] != ' ' and b[7] != ' ' and b[8] != ' '):
        return True
    return False

def isWinForPlayerTest(b):
    if (b[0] == 'X' and b[1] == 'X' and b[2] == 'X' or
        b[3] == 'X' and b[4] == 'X' and b[5] == 'X' or
        b[6] == 'X' and b[7] == 'X' and b[8] == 'X' or
        b[0] == 'X' and b[4] == 'X' and b[8] == 'X' or
        b[2] == 'X' and b[4] == 'X' and b[6] == 'X' or
        b[0] == 'X' and b[3] == 'X' and b[6] == 'X' or
        b[1] == 'X' and b[4] == 'X' and b[7] == 'X' or
        b[2] == 'X' and b[5] == 'X' and b[8] == 'X') :
        return True
    return False

def isWinForAiTest(b):
    if (b[0] == 'O' and b[1] == 'O' and b[2] == 'O' or
        b[3] == 'O' and b[4] == 'O' and b[5] == 'O' or
        b[6] == 'O' and b[7] == 'O' and b[8] == 'O' or
        b[0] == 'O' and b[4] == 'O' and b[8] == 'O' or
        b[2] == 'O' and b[4] == 'O' and b[6] == 'O' or
        b[0] == 'O' and b[3] == 'O' and b[6] == 'O' or
        b[1] == 'O' and b[4] == 'O' and b[7] == 'O' or
        b[2] == 'O' and b[5] == 'O' and b[8] == 'O') :
        return True
    return False

def MiniMax(myBoard, player, a, b):
    if isWinForAiTest(myBoard):
        return 10
    if isWinForPlayerTest(myBoard):
        return -10
    if isDrawTest(myBoard):
        return 0

    if player == 'ai' :
        maxEvaluation = -float("inf")
        for successorState in getSuccessorStates(myBoard, 'ai'):
            evaluation = MiniMax(successorState, 'human', a, b)
            maxEvaluation = max(maxEvaluation, evaluation)
            a = max(a, maxEvaluation)
            if b < a:
                return maxEvaluation
        return maxEvaluation

    else:
        minEvaluation = float("inf")
        for successorState in getSuccessorStates(myBoard, 'human'):
            evaluation = MiniMax(successorState, 'ai', a, b)
            minEvaluation = min(minEvaluation, evaluation)
            b = min(b, minEvaluation)
            if b < a:
                return minEvaluation
        return minEvaluation

def humanTurn():
    enableButton()
    board.wait_variable(var)

def aiTurn():
    currentBoard = getBoard()
    a = -float("inf")
    b = float("inf")
    bestScore = -inf
    for successorState in getSuccessorStates(currentBoard, 'ai'):
        score = MiniMax(successorState, 'human', a, b)
        if score > bestScore:
            bestScore = score
            bestB = successorState.copy()
        a = max(a, bestScore)
    i=0
    while i<9:
        if(currentBoard[i] != bestB[i]):
            if i==0:
                button1['text'] = 'O'
                board.update()
                break
            if i==1:
                button2['text'] = 'O'
                board.update()
                break
            if i==2:
                button3['text'] = 'O'
                board.update()
                break
            if i==3:
                button4['text'] = 'O'
                board.update()
                break
            if i==4:
                button5['text'] = 'O'
                board.update()
                break
            if i==5:
                button6['text'] = 'O'
                board.update()
                break
            if i==6:
                button7['text'] = 'O'
                board.update()
                break
            if i==7:
                button8['text'] = 'O'
                board.update()
                break
            if i==8:
                button9['text'] = 'O'
                board.update()
                break
        i = i+1

    
if __name__ == "__main__":
    while True:
        humanTurn()     
        board.update_idletasks()
        board.update()
        if isWinForPlayer():
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "you won")
            board.quit()
            break
        elif isDraw():
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "Its a Tie")
            board.quit()
            break     
        
        aiTurn()
        board.update_idletasks()
        board.update()
        if isWinForAi():
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "ai won")
            board.quit()
            break
        

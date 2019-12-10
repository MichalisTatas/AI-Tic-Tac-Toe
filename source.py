from board import *
from math import inf

def getSuccessorStates(myBoard, player):
    if player == 'human':
        symbol = 'X'
    else:
        symbol = 'O'
    successorStates = []
    i=0
    while i<9:
        if myBoard[i] == ' ':
            myBoard[i] = symbol
            successorStates.append(myBoard)
            myBoard[i] = ' '
        i = i+1
    return successorStates


def isDrawTest(b):
    if (b[0] != ' ' and b[1] != ' ' and b[2] != ' ' and
        b[3] != ' ' and b[4] != ' ' and b[5] != ' ' and
        b[6] != ' ' and b[7] != ' ' and b[8] != ' '):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie! ")
        board.quit()
        return True
    return False


def isWinForPlayerTest(b):
    if (b[0] == 'X' and b[1] == 'X' and b[3] == 'X' or
        b[3] == 'X' and b[4] == 'X' and b[5] == 'X' or
        b[6] == 'X' and b[7] == 'X' and b[8] == 'X' or
        b[0] == 'X' and b[4] == 'X' and b[8] == 'X' or
        b[2] == 'X' and b[4] == 'X' and b[6] == 'X' or
        b[0] == 'X' and b[1] == 'X' and b[2] == 'X' or
        b[0] == 'X' and b[3] == 'X' and b[6] == 'X' or
        b[1] == 'X' and b[4] == 'X' and b[7] == 'X' or
        b[6] == 'X' and b[5] == 'X' and b[8] == 'X') :
        # disableButton()
        return True
    return False

    # elif(flag == 8):
    #     tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
def isWinForAiTest(b):
    if (b[0] == 'O' and b[1] == 'O' and b[2] == 'O' or
        b[3] == 'O' and b[4] == 'O' and b[5] == 'O' or
        b[6] == 'O' and b[7] == 'O' and b[8] == 'O' or
        b[0] == 'O' and b[4] == 'O' and b[8] == 'O' or
        b[2] == 'O' and b[4] == 'O' and b[6] == 'O' or
        b[0] == 'O' and b[1] == 'O' and b[2] == 'O' or
        b[0] == 'O' and b[3] == 'O' and b[6] == 'O' or
        b[1] == 'O' and b[4] == 'O' and b[7] == 'O' or
        b[6] == 'O' and b[5] == 'O' and b[8] == 'O') :
        disableButton()
        return True
    return False





def MiniMax(myBoard, depth, player, a, b):
    if isWinForAiTest(myBoard):
        print("DADA")
        return 10
    if isWinForPlayerTest(myBoard):
        print("MAMA")
        return -10
    if isDrawTest(myBoard):
        print("FUCKBOY")
        return 0
    if depth == 5 :
        print("CARUSO")
        return 5

    if player == 'human' :
        maxEvaluation = -float("inf")
        for successorState in getSuccessorStates(myBoard, 'human'):
            evaluation = MiniMax(successorState, depth-1, 'ai', a, b)
            maxEvaluation = max(maxEvaluation, evaluation)
            a = max(a, maxEvaluation)
            if b < a:
                return maxEvaluation
        return maxEvaluation

    else:
        minEvaluation = float("inf")
        for successorState in getSuccessorStates(myBoard, 'ai'):
            evaluation = MiniMax(successorState, depth-1, 'human', a, b)
            minEvaluation = min(minEvaluation, evaluation)
            b = min(b, minEvaluation)
            if b < a:
                return minEvaluation
        return minEvaluation

    
def humanTurn():
    enableButton()
    board.wait_variable(var)

def aiTurn(depth):
    # disableButton()
    currentBoard = getBoard()
    a = -float("inf")
    b = float("inf")
    bestScore = -inf

    for successorState in getSuccessorStates(currentBoard, 'human'):
        score = MiniMax(successorState, depth, 'ai', a, b)
        if score > bestScore:
            bestScore = score
            bestB = successorState
        a = max(a, bestScore)
    i=0
    while i<9:
        print("MPAMPAS")
        if(currentBoard[i] != bestB[i]):
            currentBoard[i] = 'O'
        i = i+1

    
if __name__ == "__main__":
    depth = 8
    while True:
        humanTurn()     
        board.update_idletasks()
        board.update()
        if isWinForPlayer():
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "you won")
            board.quit()
            break
        # cu = getBoard()
        # for x in getSuccessorStates(cu, 'ai'):
        #     print(x[0]["text"],x[1]["text"], x[2]["text"], x[3]["text"])
            
        
        aiTurn(depth)
        depth = depth -1
        board.update_idletasks()
        board.update()
        if isWinForAi():
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "ai won")
            board.quit()
            break
        

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
        if myBoard[i]["text"] == ' ':
            myBoard[i]["text"] = symbol
            successorStates.append(myBoard)
            myBoard[i]["text"] = ' '
        i = i+1
    return successorStates


def MiniMax(myBoard, depth, player, a, b):
    if isWinForAi():
        return 10
    if isWinForPlayer():
        return -10
    if isDraw():
        return 0
    if depth == 0 :
        # print("CARUSO")
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
        print("MPAMPAS")
        score = MiniMax(successorState, depth, 'ai', a, b)
        if score > bestScore:
            bestScore = score
            bestB = successorState
        a = max(a, bestScore)
    i=0
    while i<9:
        if(currentBoard[i] != bestB[i]):
           currentBoard[i]["text"] = "O" 
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
        #     print("POUTAS")
        
        aiTurn(depth)
        depth = depth -1
        board.update_idletasks()
        board.update()
        if isWinForAi():
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "ai won")
            board.quit()
            break
        

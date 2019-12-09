from tkinter import *
import tkinter.messagebox
board = Tk()
board.title("Tic Tac Toe")

bclick = True
flag = 0

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)



def btnClick(buttons):
    global bclick, flag, player2_name, player1_name, playerb, pa
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        playerb = "AI  Wins!"
        pa = "You Win!"
        checkForWin()
        flag += 1


    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def checkForWin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "you won")
        board.quit()


    elif(flag == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "ai won")
        board.quit()

buttons = StringVar()

button1 = Button(board, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(board, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(board, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(board, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(board, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(board, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(board, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(board, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(board, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

# board.mainloop()
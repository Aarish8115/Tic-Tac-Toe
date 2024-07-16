import tkinter

def new_game():# starts a new game
    global current,inputs
    current=inputs[0]
    playerLabel.config(text=current+"'s Turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="")

def turn(row,column):#processes the user input and changes UI for the next move
    global current
    if buttons[row][column]['text']=="" and check_status()==False:
        buttons[row][column]['text']=current
        if check_status()==True:
            playerLabel.config(text=current+" Wins")
        elif check_status()==False:
            change_player()
            playerLabel.config(text=current+"'s Turn")
        elif check_status()=="Tie":
            playerLabel.config(text="Tie")


def space():#checks if any empty spaces are left on the board
    ct=9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text']!="":
                ct-=1
    if ct==0:
        return False


def check_status():#checks for win or a tie after every move
    for row in range(3):
        if buttons[row][0]['text']==buttons[row][1]['text']==buttons[row][2]['text']!="":
            return True
    for column in range(3):
        if buttons[0][column]['text']==buttons[1][column]['text']==buttons[2][column]['text']!="":
            return True
    if buttons[0][0]['text']==buttons[1][1]['text']==buttons[2][2]['text']!="":
        return True
    elif buttons[0][2]['text']==buttons[1][1]['text']==buttons[2][0]['text']!="":
        return True
    
    
    elif space()==False:
        return "Tie"
    else:
        return False


def change_player(): #changes player after every move
    global current,inputs
    if current==inputs[0]:
        current=inputs[1]
    elif current==inputs[1]:
        current=inputs[0]



window=tkinter.Tk()
window.title("Tic Tac Toe")
inputs=["X","O"]#the two players
current=inputs[0]#active player
buttons=[[None,None,None],
         [None,None,None],
         [None,None,None]]#board

playerLabel=tkinter.Label(text=current+"'s turn",font=(50))
playerLabel.pack()

frame=tkinter.Frame(window,border=20)
frame.pack()

for row in range(3):#buttons on the board
    for column in range(3):
        buttons[row][column]=tkinter.Button(frame,text="",width=10,height=5,command=lambda row=row,column=column:turn(row,column))
        buttons[row][column].grid(row=row,column=column)

restartbtn=tkinter.Button(text="Restart",font=(40),padx=10,pady=5,command=new_game)
restartbtn.pack()#restarts the game

window.mainloop()
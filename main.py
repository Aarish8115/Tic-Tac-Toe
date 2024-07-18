from customtkinter import *
def new_game():# starts a new game
    global current,inputs
    current=inputs[0]
    playerLabel.configure(text=current+"'s Turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].configure(text="",fg_color="#a9b0b0",hover=True)

def turn(row,column):#processes the user input and changes UI for the next move
    global current
    if buttons[row][column].cget("text")=="" and check_status()==False:
        buttons[row][column].configure(text=current)
        if check_status()==True:
            playerLabel.configure(text=current+" Wins")
            for row in range(3):
                for column in range(3):
                    buttons[row][column].configure(hover=False)
        elif check_status()==False:
            change_player()
            playerLabel.configure(text=current+"'s Turn")
        elif check_status()=="Tie":
            for row in range(3):
                for column in range(3):
                    buttons[row][column].configure(hover=False,fg_color='#4179e0')
            playerLabel.configure(text="Tie")


def space():#checks if any empty spaces are left on the board
    ct=9
    for row in range(3):
        for column in range(3):
            if buttons[row][column].cget("text")!="":
                ct-=1
    if ct==0:
        return False


def check_status():#checks for win or a tie after every move
    for row in range(3):
        if buttons[row][0].cget("text")==buttons[row][1].cget("text")==buttons[row][2].cget("text")!="":
            buttons[row][0].configure(fg_color='#03cf00')
            buttons[row][1].configure(fg_color='#03cf00')
            buttons[row][2].configure(fg_color='#03cf00')
            return True
    for column in range(3):
        if buttons[0][column].cget("text")==buttons[1][column].cget("text")==buttons[2][column].cget("text")!="":
            buttons[0][column].configure(fg_color='#03cf00')
            buttons[1][column].configure(fg_color='#03cf00')
            buttons[2][column].configure(fg_color='#03cf00')
            return True
    if buttons[0][0].cget("text")==buttons[1][1].cget("text")==buttons[2][2].cget("text")!="":
        buttons[0][0].configure(fg_color='#03cf00')
        buttons[1][1].configure(fg_color='#03cf00')
        buttons[2][2].configure(fg_color='#03cf00')
        return True
    elif buttons[0][2].cget("text")==buttons[1][1].cget("text")==buttons[2][0].cget("text")!="":
        buttons[0][2].configure(fg_color='#03cf00')
        buttons[1][1].configure(fg_color='#03cf00')
        buttons[2][0].configure(fg_color='#03cf00')

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



app=CTk()
app.title("Tic Tac Toe")
app.resizable(False,False)
set_appearance_mode("dark")
inputs=["X","O"]#the two players
current=inputs[0]#active player
buttons=[[None,None,None],
         [None,None,None],
         [None,None,None]]#board

head=CTkLabel(app,text="Tic Tac Toe",font=('Poppins',32,'bold'),pady=20)
head.pack()
playerLabel=CTkLabel(app,text=current+"'s Turn",font=('Poppins',22))
playerLabel.pack()

frame=CTkFrame(app)
frame.pack(padx= 30, pady=20)

for row in range(3):#buttons on the board
    for column in range(3):
        buttons[row][column]=CTkButton(frame,text="",width=100,fg_color="#a9b0b0",hover_color='#919999',font=('Monospace',40,"bold"),height=100,command=lambda row=row,column=column:turn(row,column))
        buttons[row][column].grid(row=row,column=column,padx= 10, pady=10)

restartbtn=CTkButton(app,text="Restart",fg_color='#03cf00',hover_color='#008746',width=100,height=40,font=('Poppins',20),command=new_game)
restartbtn.pack(padx= 10, pady=20)#restarts the game

app.mainloop()
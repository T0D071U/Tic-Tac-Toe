# imports
import tkinter as tk
from tkinter import messagebox

#setup
root = tk.Tk()
root.title("Tik_Tac_Toe")
isX = True
player = True
winner = ""
count = 0

#functions
def  play():
    reset()
    game_Frame.tkraise()

def checkIfWinner():
    global winner, count

    for winConditions in gameBoard:
        for items in winConditions:
            if(items[0].button['text'] == items[1].button['text'] and items[1].button['text'] == items[2].button['text']):
                winner = items[0].button['text']

                for square in items:
                    square.button['bg'] = 'green'

                messagebox.showinfo("Tic-Tac-Toe", '{} has won this round!'.format(winner))\
    
    if(count == 9 and winner == ""):
        messagebox.showinfo("Tic-Tac-Toe", 'It\'s a tie!')




def reset():
    global winner, isX, count

    winner=''
    isX=True
    count=0

    for row in winRows:
        for square in row:
            square.reset()

#Tkinter frames
menu_Frame=tk.Frame(root)
menu_Frame.grid(row=0,column=0,sticky="news")

game_Frame = tk.Frame(root)
game_Frame.grid(row=0, column=0, sticky="news")

settings_Frame = tk.Frame(root)
game_Frame.grid(row=0, column=0, sticky="news")

credits_Frame = tk.Frame(root)
credits_Frame.grid(row=0, column=0, sticky="news")

#Menu frame content
menu_Label = tk.Label(menu_Frame, text="Lets play Tik_Tac_Toe!", width=30, font=('Helvetica', 20))
menu_Label.pack(pady=4)

menu_Play = tk.Button(menu_Frame, text="Play", width=10, command=play)
menu_Play.pack(pady=2)

menu_Settings = tk.Button(menu_Frame, text="Settings", width=10)
menu_Settings.pack(pady=2)

menu_Credits = tk.Button(menu_Frame, text="Credits", width=10)
menu_Credits.pack(pady=2)

menu_Exit = tk.Button(menu_Frame, text="Exit", width=10)
menu_Exit.pack(pady=2)

#Game frame content
class gameSpot:
    def __init__(self, **kwargs):
        global game_Frame

        self.name = kwargs["name"]
        self.initial = kwargs['initial']
        self.pos = kwargs['position']
        self.isEnabled = True
        self.initial = kwargs['initial']
        self.pos = kwargs['position']
        self.isEnabled = True


        self.button = tk.Button(game_Frame, text=self.initial, font=('Helvetica', 20), height=3, width=6, bg="white", command=self.clicked)
        self.button.grid(column=self.pos[0], row=self.pos[1], sticky="news")

    def clicked(self):
        global isX, count

        if(self.isEnabled == False):
            return
        


        self.button = tk.Button(game_Frame, text=self.initial, font=('Helvetica', 20), height=3, width=6, bg="white", command=self.clicked)
        self.button.grid(column=self.pos[0], row=self.pos[1], sticky="news")

    def clicked(self):
        global isX, count, player

        if(self.isEnabled == False or winner != ''):
            return
        
        if player == True:
            self.button['fg'] = 'red'
            player = False
        else:
            self.button['fg'] = 'green'
            player = True

        if isX == True:
            self.button["text"] = 'X'
            self.isEnabled = False
            isX = False
            count += 1
        else:
            self.button["text"] = 'O'
            self.isEnabled = False
            isX = True
            count += 1

        checkIfWinner()

    def reset(self):
        self.isEnabled = True
        self.button['bg'] = 'white'
        self.button['text'] = self.initial

##############
game_Title = tk.Label(game_Frame, text="Example text")
game_Title.grid(column=0, row=0, columnspan=3, sticky='news')
                
game_Player1 = tk.Label(game_Frame, text='Player1:\n0', fg='red')
game_Player1.grid(column=0, row=1)

game_player2 = tk.Label(game_Frame, text="Player2:\n0", fg='blue')
game_player2.grid(column=2, row=1)

game_Reset = tk.Button(game_Frame, text='Reset the game!', command=reset)
game_Reset.grid(column=0, row=5, columnspan=3, sticky='news')

game_Homescreen = tk.Button(game_Frame, text='Go back to the home screen!', command= menu_Frame.tkraise)
game_Homescreen.grid(column=0, row=6, columnspan=3, sticky="news")

#Top row of buttons
top_Left = gameSpot(
    position = (0,2),
    name = "1",
    initial = " "
)

top_Mid = gameSpot(
    position = (1,2),
    name = "2",
    initial = "  "
)

top_Right = gameSpot(
    position = (2,2),
    name = "3",
    initial = ""
)

#Middle row of buttons
mid_Left = gameSpot(
    position = (0,3),
    name = "4",
    initial = ""
)

mid_Mid = gameSpot(
    position = (1,3),
    name = "5",
    initial = " "
)

mid_Right = gameSpot(
    position = (2,3),
    name = "6",
    initial = "  "
)

#Bottom row of buttons
bot_Left = gameSpot(
    position = (0,4),
    name = "7",
    initial = " "
)

bot_Mid = gameSpot(
    position = (1,4),
    name = "8",
    initial = ""
)

bot_Right = gameSpot(
    position = (2,4),
    name = "9",
    initial = "  "
)

winRows = [[top_Left, top_Mid, top_Right], [mid_Left, mid_Mid, mid_Right], [bot_Left, bot_Mid, bot_Right]]
winColumns = [[top_Left, mid_Left, bot_Left], [top_Mid, mid_Mid, bot_Mid], [top_Right, mid_Right, bot_Right]]
winDiagnals = [[top_Left, mid_Mid, bot_Right], [top_Right, mid_Mid, bot_Left]]

gameBoard = [winRows, winColumns, winDiagnals]


menu_Frame.tkraise()
#mainloop
root.mainloop()

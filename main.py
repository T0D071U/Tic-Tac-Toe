# imports
import tkinter as tk

#setup
root = tk.Tk()
root.title("Tik-Tac-Toe")

#tkinter
menu_Frame=tk.Frame(root)
menu_Frame.grid(row=0,column=0,sticky="news")

#menu frame
menu_Label = tk.Label(menu_Frame, text="Lets play Tik-Tac-Toe!", width=30)
menu_Label.pack(pady=4)

menu_Play = tk.Button(menu_Frame, text="Play", width=10)
menu_Play.pack(pady=2)

menu_Settings = tk.Button(menu_Frame, text="Settings", width=10)
menu_Settings.pack(pady=2)

menu_Credits = tk.Button(menu_Frame, text="Credits", width=10)
menu_Credits.pack(pady=2)

menu_Exit = tk.Button(menu_Frame, text="Exit", width=10)
menu_Exit.pack(pady=2)

root.mainloop()

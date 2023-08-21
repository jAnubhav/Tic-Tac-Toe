from tkinter import *
from functools import partial
from tkinter.messagebox import showinfo, askyesno

def answer(pos):
    global chance
    if value[pos] == ' ':
        value[pos] = players[chance%2]
        btn[pos].config(text = players[chance%2])
        chance += 1
    else:
        showinfo("Invalid Move", "A Player has already made that move!\nMake another move.")
    winner = check(value)
    if winner[0] == True:
        display('Success', f"Player {2-chance%2} has won!\nDo you want to restart the game?")
    if ' ' not in value:
        display('Match Draw', "No Move Left!\nDo you want to restart the game?")

def check(l):
    for i in range(3):
        if l[i] == l[i+3] and l[i] == l[i+6] and l[i] != ' ':
            return [True, l[i]]
    for i in range(0, 7, 3):
        if l[i] == l[i+1] and l[i] == l[i+2] and l[i] != ' ':
            return [True, l[i]]
    if l[0] == l[4] and l[0] == l[8] and l[0] != ' ':
        return [True, l[0]]
    if l[2] == l[4] and l[2] == l[6] and l[2] != ' ':
        return [True, l[2]]
    return [False, 'X']

def display(val1, val2):
    global value, btn, chance
    choice = askyesno(val1, val2)
    if choice == 1:
        value = list(' ' * 9)
        chance = 0
        for i in range(9):
            btn[i].config(text = ' ')
    else:
        root.destroy()

btn = []
chance = 0
players = ['X', 'O']
value = list(' ' * 9)

root = Tk()
root.title('TicTacToe')
root.geometry('393x372+200+100')
root.config(bg='white')
root.resizable(False, False)

for i in range(9):
    btn.append(Button(root, text=' ', width=5, height=2, font=('arial', 20, 'bold'), bg='steel blue', fg='white', activebackground='light blue', bd=20, relief=SUNKEN, command=partial(answer, i)))
    btn[i].grid(row=i//3, column=i%3)

root.mainloop()

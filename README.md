# GUI-projects
from tkinter import *

top = Tk()
groceryList = []
def result():
    print(groceryList)
def addToList():
    newItem = E1.get()
    groceryList.append(newItem)
#This is a label widget
L1 = Label(top, text="What's up, nerd?")
L1.grid(column = 0, row = 1)
#This is an entry widget
E1 = Entry(top, bd = 5, relief = "ridge")
E1.grid(column = 0, row = 2)
#This is a button widget
B1 = Button(text =" Print your list ", bg = "#00beff", command = result)
B1.grid(column = 0, row = 3)

B2 = Button(text =" Add items to your list ", bg = "#00beff", command = addToList)
B2.grid(column = 0, row = 4)


B3 = Button(text =" RANDOM USELESS BUTTON TIME ", bg = "#00beff", font =("playfair display", 12), fg = "White")
B3.grid(column = 0, row = 5)




top.mainloop()

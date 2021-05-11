# GUI-projects
from tkinter import *

top = Tk()
groceryList = []
def result():
    print(groceryList)

def exportList():
    with open('test.txt', 'w') as f:
        for item in groceryList:
            f.write("%s\n" % item)
def clearWindow():
    for children in top.winfo_children():
        children.destroy()

def mainMenu():
    clearWindow()
    L1Main = Label(top, text = "Block 5 GUIs")
    L1Main.grid(column = 1, row = 1)
    
    B1Main = Button(text = " Week 1 ", bg = "#000fbe", command = week1, fg = "White", font = ("Times", 11, "italic"))
    B1Main.grid(column = 1, row = 2)
    
    B2Main = Button(text = " Week 2 ", bg = "#000eff", command = week2, fg = "White", font = ("Times", 11, "italic"))
    B2Main.grid(column = 1, row = 3)
    
    B3Main = Button(text = " Week 3 ", bg = "#00beff", font =("Times", 11, "italic"), fg = "White")
    B3Main.grid(column = 1, row = 4)

def week1():
    clearWindow()
    def addToList():
        newItem = E1.get()
        groceryList.append(newItem)
        E1.delete(0, END)
    
    #This is a label widget
    L1 = Label(top, text = "What's up, nerd?")
    L1.grid(column = 0, row = 1)
    #This is an entry widget
    E1 = Entry(top, bd = 5, relief = "ridge")
    E1.grid(column = 0, row = 2)
    #This is a button widget
    B1 = Button(text = " Add ", bg = "#000fbe", command = addToList, fg = "White", font = ("Times", 11, "italic"))
    B1.grid(column = 0, row = 3)

    B2 = Button(text = " Print ", bg = "#000eff", command = result, fg = "White", font = ("Times", 11, "italic"))
    B2.grid(column = 0, row = 4)


    B3 = Button(text = " Random useless button ", bg = "#00beff", font =("Times", 11, "italic"), fg = "White")
    B3.grid(column = 0, row = 5)

    B4 = Button(text = " Export ", bg = "#beffff", command = exportList, font = ("Times", 11, "italic"), fg = "Black")
    B4.grid(column = 0, row = 6)

    B5 = Button(text = " Main ", bg = "white", command = mainMenu, font = ("Times", 11, "italic"), fg = "Black")
    B5.grid(column = 0, row = 7)

def week2():
    clearWindow()
    L1 = Label(top, text = "Dice Roller")
    L1.grid(column = 1, row = 0)

    L2 = Label(top, text = "How many sides?")
    L2.grid(column = 0, row = 1)

    L3 = Label(top, text = "How many rolls?")
    L3.grid(column = 3, row = 1)

    E1 = Entry(top, bd = 4, relief = "ridge")
    E1.grid(column = 0, row = 2)

    E1 = Entry(top, bd = 4, relief = "ridge")
    E1.grid(column = 3, row = 2)

    B1 = Button(text = " Roll! ", bg = "#000bfe", fg = "White", font = ("Times", 11, "italic"))
    B1.grid(column = 1, row = 4)
    
    #command =


if __name__ == "__main__":
    mainMenu()
    top.mainloop()

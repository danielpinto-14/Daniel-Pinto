from tkinter import *

green = "#06c22f"
blue = "#1b3cc2"
red = "#c20e2c"
purple = "#6a1380"
nigger = "#0a0a0a"
wigger = "#ffffff"

def Purple():
    janela.configure(background=purple)
    labelColor.configure(background=purple, text="Purple")

def Green():
    janela.configure(background=green)
    labelColor.configure(background=green, text="Green")

def Blue():
    janela.configure(background=blue)
    labelColor.configure(background=blue, text="Blue")

def Red():
    janela.configure(background=red)
    labelColor.configure(background=red, text="Red")

janela = Tk()
janela.title("RODRIGO")
janela.geometry("600x600+500+100")
janela.wm_resizable(width = False, height = False)
janela.configure(background = nigger)

button4 = Button(janela, text = "FRANCISCO AND RODRIGO ARE NIGGAS", command = Purple, font = "Arial 7 bold", bg = purple, fg = nigger)
button4.place(width = 200, height = 160, x = 40, y = 20)

button1 = Button(janela, text = "WE ARE CHARLIE KIRK", command = Green, font = "Arial 11 bold", bg = green, fg = nigger)
button1.place(width = 200, height = 160, x = 260, y = 20)

button2 = Button(janela, text = "EFN", command = Blue, font = "Arial 23 bold", bg = blue, fg = nigger)
button2.place(width = 200, height = 160, x = 40, y = 200)

button3 = Button(janela, text = "CITY BOY", command = Red, font = "Arial 15 bold", bg = red, fg = nigger)
button3.place(width = 200, height = 160, x = 260, y = 200)

labelColor = Label(janela, text = "RAAAAAAAAAHHHHHH", font = "Arial 9 bold", bg = purple, fg = wigger)
labelColor.place(width = 150, height = 60, x = 190, y = 390)

janela.mainloop()

from tkinter import *

def Teste():
    rodrigo = Label(francisco, text = "Rodrigo", font = "Time 20 bold")
    rodrigo.place(width = 150, height = 100, x = 105, y = 250)

    buttonclickb = Button(francisco, text = "Francisco", command = TesteDois, font = "Time 20 bold")
    buttonclickb.place(width = 150, height = 100, x = 100, y = 150)

def TesteDois():
    rodrigob = Label(francisco, text = "Francisco", font = "Time 20 bold")
    rodrigob.place(width = 150, height = 100, x = 111, y = 500)

francisco = Tk()
francisco.title("RODRIGO")
francisco.geometry("400x600+500+100")
francisco.wm_resizable(width = True, height = True)


buttonclick = Button(francisco, text = "Rodrigo", command = Teste, font = "Time 20 bold")
buttonclick.place(width = 150, height = 100, x = 100, y = 50)



francisco.mainloop()
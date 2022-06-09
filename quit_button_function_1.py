from tkinter import *

main_window =Tk()

def quit():
    main_window.destroy()

Button(main_window, text="Quit",command=quit).grid(column=7, row=2)



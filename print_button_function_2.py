from tkinter import *

main_window =Tk()

def quit():
    main_window.destroy()

def print_hired_details():
    global j_names, total_entries, name_count
    name_count = 0
    Label(main_window, text="Row").grid(column=1, row=10)
    Label(main_window, text="Full Name").grid(column=2, row=10)
    Label(main_window, text="Item").grid(column=3, row=10)
    Label(main_window, text="Receipt Number").grid(column=4, row=10)
    Label(main_window, text="Number of Hired").grid(column=5, row=10)
    Label(main_window, text="Price").grid(column=6, row=10)
    Label(main_window, text="Cost").grid(column=7, row=10)

    while name_count < total_entries :
        Label(main_window, text=name_count).grid(column=1, row=name_count+8)
        Label(main_window, text=(hired_details[name_count][0])).grid(column=2, row=name_count+8)
        Label(main_window, text=(hired_details[name_count][1])).grid(column=3, row=name_count+8)
        Label(main_window, text=(hired_details[name_count][2])).grid(column=4, row=name_count+8)
        Label(main_window, text=(hired_details[name_count][3])).grid(column=5, row=name_count+8)
        Label(main_window, text=(hired_details[name_count][4])).grid(column=6, row=name_count+8)
        Label(main_window, text=(hired_details[name_count][5])).grid(column=7, row=name_count+8)
        name_count += 1
              

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

def setup_buttons():
    global hired_details
    Button(main_window, text="Print Details",command=print_hired_details).grid(column=3, row=2)
    Button(main_window, text="Quit",command=quit).grid(column=7, row=2)
    Label(main_window, text="Julie's Party Hire").grid(column=3, row=0)
    Label(main_window, text="Full Name :").grid(column=2, row=3)
    entry_full_name = Entry(main_window)
    entry_full_name.grid(column=3, row=3)
    Label(main_window, text="Item :").grid(column=2, row=4)
    entry_item = Entry(main_window)
    entry_item.grid(column=3, row=4)
    Label(main_window, text="Number of Hired :").grid(column=2, row=5)
    entry_number_hired = Entry(main_window)
    entry_number_hired.grid(column=3, row=5)
    Label(main_window, text="Price :").grid(column=2, row=6)
    entry_price = Entry(main_window)
    entry_price.grid(column=3,row=6)
    Label(main_window, text="Receipt Num :").grid(column=2, row=7)
    entry_receipt_num = Entry(main_window)
    entry_receipt_num.grid(column=3, row=7)
    Label(main_window, text="Row #").grid(column=2, row=8)
    entry_row = Entry(main_window)
    entry_row.grid(column=3, row=8)
    
    
              


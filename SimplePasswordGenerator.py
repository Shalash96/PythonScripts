from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip

root = Tk()
root.title('Simple password generator')
Label(root, text='Version 1.0').grid(row=0, column=0, columnspan=3)
entry = Entry(root, width=60)
entry.grid(row=1, column=0, columnspan=3, padx=20, pady=15)


def password():
    if radiobuttonSelection.get() == 0:
        data = string.ascii_letters
    elif radiobuttonSelection.get() == 1:
        data = string.ascii_letters + string.digits
    elif radiobuttonSelection.get() == 2:
        data = string.ascii_letters + string.digits + string.punctuation

    if entry.get().isnumeric():
        new_password = ''.join(random.sample(data, int(entry.get())))
        entry.delete(0, END)
        entry.insert(0, new_password)
    elif not entry.get().isnumeric():
        messagebox.showwarning('ERROR', 'enter only numbers')
        entry.delete(0, END)


def clear():
    entry.delete(0, END)


def copy():
    pyperclip.copy(entry.get())
    entry.delete(0, END)


radiobuttonSelection = IntVar()
radiobuttonSelection.set(2)
Radiobutton(root, text='Alphabetic only', variable=radiobuttonSelection, value=0).grid(row=2, column=0)
Radiobutton(root, text='Alphabetic and numbers', variable=radiobuttonSelection, value=1).grid(row=2, column=1)
Radiobutton(root, text='Alphabetic, numbers and punctuation', variable=radiobuttonSelection, value=2).grid(row=2, column=2)

generate_button = Button(root, text='Generate', command=password)
clear_button = Button(root, text='clear', command=clear)
copy_button = Button(root, text='copy to clipboard', command=copy)
generate_button.grid(row=3, column=0)
clear_button.grid(row=3, column=1)
copy_button.grid(row=3, column=2)
root.mainloop()


from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip

root = Tk()
root.title('Simple password generator')
Label(root, text='Version 2.0').grid(row=0, column=0, columnspan=3)
entry = Entry(root, width=60)
entry.grid(row=1, column=0, columnspan=3, padx=20, pady=30)


def password():
    data = ''
    if alphaVar.get() == 1:
        data += string.ascii_letters
    if numVar.get() == 1:
        data += string.digits
    if punVar.get() == 1:
        data += string.punctuation
    if entry.get().isnumeric():
        new_password = ''.join(random.sample(data * 30, int(entry.get())))
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


alphaVar = IntVar()
Checkbutton(root, text='Alphabetic', variable=alphaVar).grid(row=2, column=0)
numVar = IntVar()
Checkbutton(root, text='Numbers', variable=numVar).grid(row=2, column=1)
punVar = IntVar()
Checkbutton(root, text='Punctuations', variable=punVar).grid(row=2, column=2)

generate_button = Button(root, text='Generate', command=password)
clear_button = Button(root, text='clear', command=clear)
copy_button = Button(root, text='copy to clipboard', command=copy)
generate_button.grid(row=3, column=0)
clear_button.grid(row=3, column=1)
copy_button.grid(row=3, column=2)
root.mainloop()

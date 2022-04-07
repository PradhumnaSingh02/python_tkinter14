from tkinter import *
import tkinter.messagebox as tmsg
def add():
    global i
    lbx.insert(ACTIVE,f'{i}')
    i+=1

i = 0
root = Tk()
root.geometry('644x456')
root.title('Listbox')

lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First item of our listbox")

Button(root, text='Add item', command=add).pack()

root.mainloop()
from tkinter import *

window = Tk()
window.title("First Tkinter")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)
lable = Label(text="Hari Prasath",font=("Arial",24))
lable.grid(column=1,row=1)


input = Entry(width=10)
input.grid(column=4, row=3)

button = Button(text="click")
button.grid(column=2,row=2)

button = Button(text="New click")
button.grid(column=3,row=1)





window.mainloop()


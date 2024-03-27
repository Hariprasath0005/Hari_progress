from tkinter import *

def convert():
    miles = float(input.get())
    km = miles*1.6
    result.config(text=f"{km}")



window = Tk()
window.title("Miles to Km converter")
window.config(padx=20,pady=20)

input = Entry(width=15)
input.grid(row=1,column=2)

mile = Label(text="miles",font=("Arial",12))
mile.grid(row=1,column=4)

equal = Label(text="is equal to",font=("Arial",12))
equal.grid(row=2,column=1)

result = Label(text="0",font=("Arial",12))
result.grid(row=2,column=2)

km = Label(text="km",font=("Arial",12))
km.grid(row=2,column=4)

button = Button(text="Calculate",command=convert)
button.grid(row=3,column=2)


window.mainloop()
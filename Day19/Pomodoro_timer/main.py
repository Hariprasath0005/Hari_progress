from tkinter import *
import math 
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#FFE167"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
timing = None

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=GREEN)


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timing)
    canvas.itemconfig(timer,text="00:00")
    label.config(text="Timer",fg=RED)
    check.config(text=" ")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps+=1
    min = WORK_MIN*60
    short = SHORT_BREAK_MIN*60
    long = LONG_BREAK_MIN*60
    
    if reps%8==0:
        count_down(long)
        label.config(text="Break",fg=RED,font=(FONT_NAME,40,"bold"))
        
    elif reps%2==0:
        count_down(short)
        label.config(text="Break",fg=PINK,font=(FONT_NAME,40,"bold"))
        
    else:
        count_down(min)
        label.config(text="Work",fg=YELLOW,font=(FONT_NAME,40,"bold"))
        


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec=f"0{count_sec}"
    if count_min == 0:
        count_min="00"

    canvas.itemconfig(timer,text=f"{count_min}:{count_sec}")
    if count>0:
        global timing
        timing = window.after(1000,count_down,count-1)
    else:
        start()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks +="✔"
        check.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
#Title 
label = Label(text="Timer",fg=RED,bg=GREEN,font=(FONT_NAME,40,"bold"))
label.grid(row=1,column=2)

#Reset button
reset_button = Button(text="Reset",bg=PINK,highlightthickness=0,command=reset)
reset_button.grid(row=3,column=3)

#Tomato image
canvas = Canvas(width=200,height=224,bg=GREEN,highlightthickness=0)
tomato_image = PhotoImage(file="./Day19/Pomodoro_timer/tomato.png")
canvas.create_image(100, 112, image = tomato_image)

#Adding the time on image
timer = canvas.create_text(105,135,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=2,column=2)

#start button
start_button = Button(text="Start",bg="#DFC57B",highlightthickness=0,command=start)
start_button.grid(row=3,column=1)

#check symbol
check = Label(fg=RED,bg=GREEN,highlightthickness=0)
check.grid(row=4,column=2)

window.mainloop()


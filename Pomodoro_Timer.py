from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1

window=Tk()
window.minsize(width=300,height=300)
window.config(padx=40,pady=20,bg=YELLOW)
canvas= Canvas(width=200,height=220,bg=YELLOW,highlightthickness=0 )
tomato_image=PhotoImage(file='tomato.png')
canvas.create_image(100,107,image=tomato_image)
text_count=canvas.create_text(100,130,text='00:00',fill='white',font=(FONT_NAME,29,'bold'))

canvas.grid(row=1,column=3)
reps=1



def countdown(count):
    global reps
    if reps in (1,3,5,7):
        count_minutes=math.floor(count/60)
        count_seconds=count%60
        if count_seconds < 10:
            count_seconds=f'0{count_seconds}'
        if count_seconds==0:
            count_seconds='00'
        if count_minutes==0:
            count_minutes='00'
        if count_minutes == '00' and count_seconds == '00':
            reps += 1
            print(reps)
        canvas.itemconfig(text_count,text=f'{count_minutes}:{count_seconds}')
        if count>0:
            window.after(1000,countdown,count-1)

    else:
        count_minutes=math.floor(count/60)
        count_seconds=count%60
        if count_seconds < 10:
            count_seconds=f'0{count_seconds}'
        if count_seconds==0:
            count_seconds='00'
        if count_minutes==0:
            count_minutes='00'
        if count_minutes=='00' and count_seconds=='00':
            reps += 1
            print(reps)
        canvas.itemconfig(text_count,text=f'{count_minutes}:{count_seconds}')
        if count>0:
            window.after(1000,countdown,count-1)
def timer_countdown():
    global reps
    if reps in (2,4,6):
        countdown(SHORT_BREAK_MIN*1)
        label_correct = Label(text='BREAK', font=("Times New Roman", 23, 'bold'), bg=YELLOW, fg=GREEN)
        label_correct.grid(row=0, column=3)
        label_display()
    elif reps in (1,3,5,7):
        countdown(WORK_MIN * 2)
        label_correct = Label(text='WORK', font=("Times New Roman", 23, 'bold'), bg=YELLOW, fg=GREEN)
        label_correct.grid(row=0, column=3)
        label_display()
    elif reps==8:
        countdown(LONG_BREAK_MIN * 3)
        label_correct = Label(text='LONG BREAK', font=("Times New Roman", 23, 'bold'), bg=YELLOW, fg=GREEN)
        label_correct.grid(row=0, column=3)
        label_display()
start_button = Button(text='Start', command=timer_countdown)
start_button.grid(row=2, column=2)

reset_button=Button(text='Reset')
reset_button.grid(row=2,column=9)


def label_display():

    label_correct1=Label(text='✓',bg=YELLOW,fg=GREEN)
    label_correct1.place(x=reps*23+39.6,y=290)


window.mainloop()

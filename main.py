from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

#add image using canvas widget:
canvas = Canvas(width=200 ,height=224, bg=YELLOW, highlightthickness=0)#highlightthickness = 0 get rid of border around canvas
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image= tomato_img) #x, y, image as PhotoImage
canvas.create_text(100, 130, text= "00:00", fill="white", font=(FONT_NAME, 35, "bold")) #same values as the image for position
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)


checkmarks = Label(text="✓", fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)



window.mainloop()
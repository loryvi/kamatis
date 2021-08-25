from tkinter import *
from PIL import ImageTk, Image
import time


root = Tk()  # root is mywindow
# Creating at Label Widget
root.title("KAMATIS")
root.geometry("400x420")  # window size
root.resizable(0, 0)
root.config(background="#E9DECA", highlightbackground="#E9DECA",
            highlightcolor="#E9DECA")
root.iconbitmap('pythonprojects/icon2.ico')


def pomo():

    for widgets in root.winfo_children():
        widgets.destroy()

    img2 = Image.open("pythonprojects/tomato.png")
    resize_image2 = img2.resize((290, 280))
    tomato_img = ImageTk.PhotoImage(resize_image2)
    canvas2 = Canvas(root, width=300, height=300)
    canvas2.create_image(150, 150, anchor="center", image=tomato_img)
    canvas2.config(highlightthickness=0)
    canvas2.pack(pady=20)

    global buttonClicked
    buttonClicked = not buttonClicked

    t = 10
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)  # delays the overwrite by one second
        t -= 1  # overwrite the timer
        #print("Break time")
    # breaktime()  # goes to function pomodoro


def breaktime():
    t = 5
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    #print("Pomodoro Start")
    pomo()  # goes back to function appstart again


# image in start app
img = Image.open("pythonprojects/Start.png")
resize_image = img.resize((284, 331))
kamatis_img1 = ImageTk.PhotoImage(resize_image)
canvas = Canvas(root, width=284, height=331, background="#E9DECA")
canvas.create_image(142, 165, anchor="center", image=kamatis_img1)
canvas.config(highlightthickness=0)
canvas.pack(pady=10, padx=20)

buttonClicked = False  # Bfore first click
# button to pomodoro timer
main_button = Button(root, text=">>", padx=50,
                     command=pomo, background="#63190E", fg="#F2D393")
main_button.pack(pady=20)


# keeps the widget open
root.mainloop()

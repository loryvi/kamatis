import tkinter as tk
from tkinter import *
import datetime
import winsound as ws


class Countdown(tk.Frame):
    def __init__(self, master):  # main function
        super().__init__(master)
        self.create_widgets()  # functiom
        self.show_widgets()  # another functions
        self.seconds_left = 0
        self._timer_on = False

    def home(self):
        self.seconds_left = int(self.timer)
        self.stop_timer()
        self.label["text"] = ""
        for widgets in self.winfo_children():
            widgets.destroy()
        start2 = StartApp(self)
        start2.pack()

    def create_widgets(self):
        self.bg = PhotoImage(file="kamatis/images/Tomato.png")

        # create canvas
        self.my_canvas1 = tk.Canvas(self, width=400, height=400)
        self.my_canvas1.create_image(0, 0, image=self.bg, anchor="nw")
        self.my_canvas1.config(highlightthickness=0)

        # frame for text

        self.center_frame = tk.Frame()
        self.center_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.label = tk.Label(self.center_frame, text="Start Pomodoro: ", font=(
            "Comic Sans MS", 25), bg="#e9deca", fg='#63190E')

        self.timer = 25*60  # 25 minutes countdown

        # stop,start,Reset button goes to function start,stop,reset_button
        self.reset = tk.Button(self, text="Reset Timer", font=("Arial", 10), background="#63190E", fg="#F2D393",
                               command=self.reset_button)
        self.stop = tk.Button(self, text="Stop Timer", font=("Arial", 10), background="#63190E", fg="#F2D393",
                              command=self.stop_button)
        self.start = tk.Button(self, text="Start Timer", font=("Arial", 10), background="#63190E", fg="#F2D393",
                               command=self.start_button)

        # home button
        self.home_btn = tk.Button(self, text="Home", font=(
            "Arial", 10), background="#63190E", fg="#F2D393", command=self.home)

    def show_widgets(self):  # children buttons
        self.my_canvas1.pack(fill="both", expand=True)
        self.label.pack()  # text

        # buttons
        self.home_window = self.my_canvas1.create_window(
            10, 10, anchor="nw", window=self.home_btn)
        self.start_window = self.my_canvas1.create_window(
            10, 370, anchor="nw", window=self.start)
        self.stop_window = self.my_canvas1.create_window(
            100, 370, anchor="nw", window=self.stop)
        self.reset_window = self.my_canvas1.create_window(
            310, 370, anchor="nw", window=self.reset)

    def countdown(self):

        if self.seconds_left:
            self.label["text"] = self.convert_seconds_left_to_time()
            self.seconds_left -= 1
            self._timer_on = self.after(1000, self.countdown)  # sleep 1s
        else:
            self._timer_on = False  # off the timer
            self.label["text"] = "You're done!"
            ws.PlaySound('kamatis/storedoorchime.wav', ws.SND_FILENAME)
            # wav file from https://soundbible.com/1599-Store-Door-Chime.html

    def reset_button(self):
        self.seconds_left = 0
        self.stop_timer()  # stop timer /pause
        self._timer_on = False  # stop timer
        self.label["text"] = "Start Pomodoro"
        self.start.forget()  # buttons
        self.stop.forget()
        self.reset.forget()

        self.home_window = self.my_canvas1.create_window(
            10, 10, anchor="nw", window=self.home_btn)
        self.start_window = self.my_canvas1.create_window(
            10, 370, anchor="nw", window=self.start)
        self.stop_window = self.my_canvas1.create_window(
            100, 370, anchor="nw", window=self.stop)
        self.reset_window = self.my_canvas1.create_window(
            310, 370, anchor="nw", window=self.reset)

    def stop_button(self):

        self.seconds_left = int(self.timer)
        self.stop_timer()

    def start_button(self):
        self.seconds_left = int(self.timer)
        self.stop_timer()
        self.countdown()
        self.start.forget()
        self.stop.forget()
        self.reset.forget()

        self.home_window = self.my_canvas1.create_window(
            10, 10, anchor="nw", window=self.home_btn)
        self.start_window = self.my_canvas1.create_window(
            10, 370, anchor="nw", window=self.start)
        self.stop_window = self.my_canvas1.create_window(
            100, 370, anchor="nw", window=self.stop)
        self.reset_window = self.my_canvas1.create_window(
            310, 370, anchor="nw", window=self.reset)

    def stop_timer(self):

        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on = False  # ooff the timer, stop

    def convert_seconds_left_to_time(self):
        return datetime.timedelta(seconds=self.seconds_left)


class StartApp(tk.Frame):
    def __init__(self1, master1):  # main function
        super().__init__(master1)
        self1.create_widgets1()
        self1.show_widgets1()

    def pomo(self1):
        for widgets in self1.winfo_children():
            widgets.destroy()
        countdown = Countdown(self1)
        countdown.pack()

    def create_widgets1(self1):
        self1.bg1_ = PhotoImage(file="kamatis/images/StartApp.png")

        # Create a canvas
        self1.my_canvas = tk.Canvas(self1, width=400, height=400)
        self1.my_canvas.create_image(0, 0, image=self1.bg1_, anchor="nw")
        self1.my_canvas.config(highlightthickness=0)
        self1.start_btn = tk.Button(self1, text=">>", font=(
            "Comic Sans", 12), padx=50, background="#63190E", fg="#F2D393", command=self1.pomo)

    def show_widgets1(self1):
        self1.my_canvas.pack(fill="both", expand=True)
        self1.button1_window = self1.my_canvas.create_window(
            200, 370, anchor="center", window=self1.start_btn)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")
    root.resizable(0, 0)  # cant stretch it, no resize
    root.title("KAMATIS")
    root.iconbitmap('kamatis/icon.ico')

    start1 = StartApp(root)  # create a variable start1
    start1.pack()

    root.mainloop()

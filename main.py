import time

def appstart():
    pomodoro = int(input("Enter 1 to start pomodoro: "))
    t = 25*60 #25 minutes
    if(pomodoro == 1):
        while t:
            mins = t // 60
            secs = t % 60 
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1) #delays the overwrite by one second
            t -= 1 #overwrite the timer
        print("Break time")
    breaktime() #goes to function pomodoro


def breaktime():
    t = 5*60 #5 minutes breaktime
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Pomodoro Start")
    appstart() #goes back to function appstart again


appstart() #starts the function

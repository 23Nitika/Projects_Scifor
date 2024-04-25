from tkinter import *
import datetime
import winsound
from threading import Thread

# Function to play alarm sound
def play_alarm():
    winsound.Beep(440, 1000)  

# Function to check and trigger the alarm
def check_alarm():
    set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == set_alarm_time:
            play_alarm()
            break

# Function to start the alarm in a separate thread
def start_alarm():
    t1 = Thread(target=check_alarm)
    t1.start()

# GUI setup
root = Tk()
root.title("Python Alarm Clock")

frame = Frame(root)
frame.pack()

hour = StringVar(frame)
hour.set('00')
minute = StringVar(frame)
minute.set('00')
second = StringVar(frame)
second.set('00')

hour_menu = OptionMenu(frame, hour, *['{:02d}'.format(i) for i in range(25)])
hour_menu.grid(row=0, column=0)
minute_menu = OptionMenu(frame, minute, *['{:02d}'.format(i) for i in range(60)])
minute_menu.grid(row=0, column=1)
second_menu = OptionMenu(frame, second, *['{:02d}'.format(i) for i in range(60)])
second_menu.grid(row=0, column=2)

start_button = Button(frame, text="Start Alarm", command=start_alarm)
start_button.grid(row=1, columnspan=3)

root.mainloop()
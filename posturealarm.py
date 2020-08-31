# Alarm clock that rings every hour to remind me to keep my back straight
'''
How will it work?
- A small icon pops up from the bottom right corner of the screen.
- The message should only pop up if the screen is on.
- Window should be about 8cm by 8cm
- The window will contain some sort of message - something like "Reminder! Check your posture!" and will contain a funny animation
of someone with bad posture and someone with good posture.
- There should be an acknowledge button which will 'snooze' the reminder for a specific amount of time.
'''

from tkinter import *
from tkinter import ttk
import winsound
from datetime import datetime, timedelta

HEIGHT = 300
WIDTH = 300

root = Tk()

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Added window title
root.title('Posture Check Reminder')

# Added background image
background_img = PhotoImage(file='background.png')
back_label = Label(root, image=background_img)
back_label.place(x=0, y=0)

# Added simple text to the top of the page
Label(root, text="Posture Check!", fg="red", relief="solid", font=("Comic Sans MS", 20, "bold")).place(x=57, y=35)
Label(root, text="Remind me in", fg="black", relief="solid", font=("Helevetica", 10, "bold")).place(x=107, y=115)

# Added window icon
Tk.iconbitmap(root, default='meerkat.ico')

# Function to minimize/maximize app after a specific amount of time
def sleepfunc(option):


    seconds_dictionary_boundary_1 = {
        '1': datetime.now() + timedelta(seconds=60),
        '2': datetime.now() + timedelta(seconds=1800),
        '3': datetime.now() + timedelta(seconds=3600),
        '4': datetime.now() + timedelta(seconds=7200)
    }
    seconds_dictionary_boundary_2 = {
        '1': datetime.now() + timedelta(seconds=62),
        '2': datetime.now() + timedelta(seconds=1803),
        '3': datetime.now() + timedelta(seconds=3603),
        '4': datetime.now() + timedelta(seconds=7203)
    }

    if option == 1:
        winsound.PlaySound('click.wav', winsound.SND_ASYNC)
        while datetime.now() < seconds_dictionary_boundary_1['1'] and datetime.now() < seconds_dictionary_boundary_2['1']:
            root.wm_state('iconic')
        winsound.PlaySound('ding-sound-effect_2.wav', winsound.SND_ASYNC)
        root.wm_state('normal')
    elif option == 2:
        winsound.PlaySound('click.wav', winsound.SND_ASYNC)
        while datetime.now() < seconds_dictionary_boundary_1['2'] and datetime.now() < seconds_dictionary_boundary_2[
            '2']:
            root.wm_state('iconic')
        winsound.PlaySound('ding-sound-effect_2.wav', winsound.SND_ASYNC)
        root.wm_state('normal')
    elif option == 3:
        winsound.PlaySound('click.wav', winsound.SND_ASYNC)
        while datetime.now() < seconds_dictionary_boundary_1['3'] and datetime.now() < seconds_dictionary_boundary_2[
            '3']:
            root.wm_state('iconic')
        winsound.PlaySound('ding-sound-effect_2.wav', winsound.SND_ASYNC)
        root.wm_state('normal')
    elif option == 4:
        winsound.PlaySound('click.wav', winsound.SND_ASYNC)
        while datetime.now() < seconds_dictionary_boundary_1['4'] and datetime.now() < seconds_dictionary_boundary_2[
            '4']:
            root.wm_state('iconic')
        winsound.PlaySound('ding-sound-effect_2.wav', winsound.SND_ASYNC)
        root.wm_state('normal')

# Added buttons to the canvas
b1 = ttk.Button(root, text='15 Minutes', command=lambda: sleepfunc(1))
b1.place(height=50, width=100, anchor=SE, relx=0.50, rely=0.65)
b2 = ttk.Button(root, text='30 Minutes', command=lambda: sleepfunc(2))
b2.place(height=50, width=100, anchor=SE, relx=0.84, rely=0.65)
b3 = ttk.Button(root, text='1 Hour', command=lambda: sleepfunc(3))
b3.place(height=50, width=100, anchor=SE, relx=0.50, rely=0.85)
b4 = ttk.Button(root, text='2 hours', command=lambda: sleepfunc(4))
b4.place(height=50, width=100, anchor=SE, relx=0.84, rely=0.85)

# Prevent the canvas from being resizeable
root.resizable(False, False)

root.mainloop()
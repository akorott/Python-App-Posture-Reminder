from tkinter import *
from tkinter import ttk
import winsound

HEIGHT = 300
WIDTH = 300

root = Tk()
root.geometry(f"{HEIGHT}x{WIDTH}")

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

def on_alarm():
    winsound.PlaySound('ding-sound-effect_2.wav', winsound.SND_ASYNC)
    root.wm_state('normal')

# Function to minimize/maximize app after a specific amount of time
def sleepfunc(option):
    winsound.PlaySound('click.wav', winsound.SND_ASYNC)
    root.wm_state('iconic')
    if option == 1:
        # schedule the on_alarm function to run in 15 minutes
        # after method needs that converted to milliseconds,
        # therefore 15 minutes * 60 seconds per minute * 1000 milliseconds per second
        root.after(15*60*1_000, on_alarm)
    elif option == 2:
        root.after(30*60*1_000, on_alarm)
    elif option == 3:
        root.after(60*60*1_000, on_alarm)
    elif option == 4:
        root.after(120*60*1_000, on_alarm)

# Added buttons
b1 = ttk.Button(root, text='15 Minutes', command=lambda: sleepfunc(1))
b1.place(height=50, width=100, anchor=SE, relx=0.50, rely=0.65)
b2 = ttk.Button(root, text='30 Minutes', command=lambda: sleepfunc(2))
b2.place(height=50, width=100, anchor=SE, relx=0.84, rely=0.65)
b3 = ttk.Button(root, text='1 Hour', command=lambda: sleepfunc(3))
b3.place(height=50, width=100, anchor=SE, relx=0.50, rely=0.85)
b4 = ttk.Button(root, text='2 hours', command=lambda: sleepfunc(4))
b4.place(height=50, width=100, anchor=SE, relx=0.84, rely=0.85)

# Prevent the window from being resizeable
root.resizable(False, False)

root.mainloop()
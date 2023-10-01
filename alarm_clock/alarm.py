from tkinter import Tk, messagebox
from tkinter import ttk, Entry, Spinbox
from PIL import ImageTk
from PIL.Image import open
from pygame import mixer
import datetime
import time
from tkinter import *
from time import strftime
import customtkinter
from threading import Thread

class AlarmClock:
    def __init__(self):
        self.ringtones_list = ['jaz', 'wakeup', 'motivational']

        self.ringtones_path = {
            'motivational': 'alarm_tones/motivational.mp3',
            'jaz': 'alarm_tones/Swing Jazz.mp3',
            'wakeup': 'alarm_tones/wakeup.mp3'
        }

        self.root = customtkinter.CTk()
        self.root.title("Alarm Clock")
        self.root.geometry("360x350")
        self.root.resizable(0, 0)

        rootBackground = open("images/BGgenerated.jpg")
        size = 500, 500
        rootBackground.thumbnail(size)
        self.background = ImageTk.PhotoImage(rootBackground)
        self.background_label = Label(self.root, image=self.background)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.mark = Label(self.root, height=1, font=('calibri', 30, 'bold'), foreground='white', bg='#4d6a94')
        self.mark.place(relx=0.48, rely=0.1, anchor="center")
        self.Dclock()

        Label(self.root, text='Choose the alarm time', font=("Comic Sans MS", 15, 'bold'),
                  foreground="white", bg='#4d6a94').place(relx=0.23, rely=0.16)
        Label(self.root, text='Hour', font=("Comic Sans MS", 10, 'bold'), foreground="white",
                  bg='#4d6a94').place(relx=0.30, rely=0.27)
        Label(self.root, text='Minute', font=("Comic Sans MS", 10, 'bold'), foreground="white",
                  bg='#4d6a94').place(relx=0.5, rely=0.27)

        self.hour = IntVar()
        Spinbox(width=5, from_=0, to=23, state="readonly", textvariable=self.hour,
                wrap=True, font=("Comic Sans MS", 13)).place(relx=0.30, rely=0.32)

        self.minutes = IntVar()
        Spinbox(width=4, from_=0, to=59, state="readonly", textvariable=self.minutes,
                wrap=True, font=("Comic Sans MS", 13)).place(relx=0.5, rely=0.32)

        self.ringtone_label = Label(self.root, text="Ringtones",
                                        font=("Comic Sans MS", 14, 'bold'),
                                        foreground="white", bg='#4d6a94')
        self.ringtone_label.place(relx=0.13, rely=0.44)

        self.ringtone_var = StringVar()
        self.ringtone_combo = ttk.Combobox(self.root,
                                           width=14, height=10, textvariable=self.ringtone_var,
                                           font=("Comic Sans MS", 12))
        self.ringtone_combo['values'] = self.ringtones_list
        self.ringtone_combo.current(0)
        self.ringtone_combo.place(relx=0.35, rely=0.447)

        testMusic_img = open('images/speaker.png')
        self.testMusic_btn = ImageTk.PhotoImage(testMusic_img)
        self.testMusic = customtkinter.CTkButton(self.root,
                                    image=self.testMusic_btn,
                                    text="",
                                    command=self.preview_alarm,
                                    width=5,
                                    height=5,
                                    fg_color="#4d6a94")
        self.testMusic.place(relx=0.73, rely=0.44)

        self.message_label = Label(self.root, text="Message",
                                       font=("Comic Sans MS", 14, 'bold'), foreground="white", bg='#4d6a94')
        self.message_label.place(relx=0.13, rely=0.527)

        self.message_var = StringVar()
        self.message_entry = Entry(self.root,
                                   textvariable=self.message_var, font=("Comic Sans MS", 12), width=19)
        self.message_entry.insert(0, 'Wake Up')
        self.message_entry.place(relx=0.35, rely=0.54)

        self.confirm = customtkinter.CTkButton(master=self.root,
                                   width=170,
                                   height=5,
                                   text="Set alarm",
                                   font=("Comic Sans MS", 17,"bold"), 
                                   command=self.alarm_time,
                                   text_color="white",
                                   fg_color="#1a2d47")
        self.confirm.place(relx=0.5, rely=0.74, anchor='center')

        self.exit = customtkinter.CTkButton(master=self.root,
                                   width=40,
                                   height=5,
                                   text="Quit",
                                   font=("Comic Sans MS", 13,"bold"), 
                                   command=self.root.destroy,
                                   text_color="white",
                                   fg_color="#42618f",
                                   hover_color="#952323") 
        self.exit.place(relx=0.5, rely=0.88, anchor='center')

    def Dclock(self):
        time1 = ''
        time1 = time.strftime('%H:%M:%S')
        self.mark.config(text=time1)
        self.mark.after(200, self.Dclock)

    def preview_alarm(self):
        ringtone = self.ringtone_var.get()
        mixer.init()
        mixer.music.load(self.ringtones_path[ringtone])
        mixer.music.play()
        messagebox.showinfo('Playing...', 'press OK to stop playing')
        mixer.music.stop()

    def play_music(self,sound_name):
        mixer.init()
        mixer.music.load(self.ringtones_path[sound_name])
        mixer.music.play()
        time.sleep(5)

    def show_message_box(self,message,alarm_time):
        root = Tk()
        root.withdraw()  # Hide the Tkinter root window
        messagebox.showinfo("Alarm", f"{message}, It's {alarm_time}")
        # Stop the music when the message box is closed
        mixer.music.stop()
        # After the message box is closed, destroy the root window
        root.destroy()

    def start_alarm(self,alarm_time):
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(current_time)

            if current_time == alarm_time:
                alarm_time = str(self.hour.get()) + ":" + str(self.minutes.get())        
                ringtone = self.ringtone_var.get()
                message = self.message_var.get()
                # Playing a sound when the current time is the same as the alarm time
                music_thread = Thread(target=self.play_music,args=(ringtone,))
                music_thread.start()
                # Schedule the message box to appear after a delay
                self.root.after(5, self.show_message_box, message, alarm_time)
                break 
                            
    def alarm_time(self):
        # Get the hour and minute values from the user input
        hour = self.hour.get()
        minute = self.minutes.get()
        
        set_alarm = f"{hour}:{minute}:00"
        
        # Create a list of seconds for hours, minutes, and seconds
        seconds_hms = [3600, 60, 1]
        
        current_time = datetime.datetime.now()
        
        # Convert the current time into seconds
        currentTimeInSeconds = sum([hms_sec * current_time_unit for hms_sec, current_time_unit in zip(seconds_hms, [current_time.hour, current_time.minute, current_time.second])])
        alarmSeconds = sum([a*b for a,b in zip(seconds_hms[:2], [hour,minute])])
        
        secondsUntilAlarm = alarmSeconds - currentTimeInSeconds
        
        #If the time different is negative, that means that the alarm needs to be set for the next day.
        if secondsUntilAlarm < 0:
            secondsUntilAlarm += 86400 # number of seconds in a day
            
        answer = messagebox.showinfo("Set alarm",
        f"Alarm will signal at\n{hour}:{minute} in %s" % datetime.timedelta(seconds=secondsUntilAlarm))
        self.start_alarm(set_alarm)


    def run(self):
        self.root.mainloop()


alarm_clock = AlarmClock()
alarm_clock.run()
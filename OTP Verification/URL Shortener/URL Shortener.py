import tkinter as tk
import customtkinter
import pyshorteners

def shorten_url():
    url = URL_entry.get()
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    result_label.insert(0,shortened_url)

# Create the main window
window = customtkinter.CTk()
window.title("URL Shortener")
window.geometry("360x350")


URL_label = customtkinter.CTkLabel(window,
                     font=("ADLaM Display", 20,"bold"),
                     text="ENTER URL")
URL_label.place(relx=0.36, rely=0.1)

# Create the URL entry
URL_entry = customtkinter.CTkEntry(window,font=("Comic Sans MS", 12), width=330)
URL_entry.place(relx=0.04, rely=0.2)

# Create the "Shorten" button
button = customtkinter.CTkButton(window,
                                 width=170,
                                 height=10,
                                 text="Shorten",
                                 command=shorten_url,
                                 text_color="white",
                                 fg_color="#1a2d47")
button.place(relx=0.26, rely=0.32)

# Create the label to display the shortened URL
result_label = customtkinter.CTkEntry(window, font=("ADLaM Display", 12),width=330,state="disabled")
result_label.place(relx=0.04, rely=0.41)

# Start the main loop
window.mainloop()
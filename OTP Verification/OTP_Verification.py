import random 
import smtplib
import ssl
from tkinter import messagebox
from tkinter import Entry
from PIL import ImageTk
from PIL.Image import open
from tkinter import *
import customtkinter

class OTPVerificationGUI:
    def __init__(self):
        self.OTP = self.generate_OTP()
        self.sender_email = "your_email@gmail.com"  # Replace with your email
        self.sender_password = "your_16_digit_code"       # Replace with your 16-digit code
        self.smtp_server = 'smtp.gmail.com'
        self.smtp_port = 465
        self.context = ssl.create_default_context()

        self.root = customtkinter.CTk()
        self.root.title("Authentication")
        self.root.geometry("660x650")
        self.root.resizable(0, 0)

        self.rootBackground = open("Background.jpg")
        size = 850, 890
        self.rootBackground.thumbnail(size)

        self.background = ImageTk.PhotoImage(self.rootBackground)
        self.background_label = Label(self.root, image=self.background)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.email_label = Label(self.root, text="Enter your email", font=("Comic Sans MS", 25, 'bold'),
                          foreground="white", bg='#445d48')
        self.email_label.place(relx=0.34, rely=0.37)

        self.email_entry = Entry(self.root, font=("Comic Sans MS", 19), width=35)
        self.email_entry.insert(0, 'example@example.com')
        self.email_entry.place(relx=0.19, rely=0.45)

        self.send_button = customtkinter.CTkButton(self.root,
                                        width=170,
                                        height=5,
                                        text="Send OTP",
                                        font=("Comic Sans MS", 22,"bold"), 
                                        command=self.send_otp,
                                        text_color="white",
                                        fg_color="#606C5D",
                                        hover_color="#1c2f36")
        self.send_button.place(relx=0.5, rely=0.55, anchor='center')

        self.otp_label = Label(self.root, text="Enter the OTP you received", font=("Comic Sans MS", 19, 'bold'),
                          foreground="white", bg='#445d48')
        self.otp_label.place(relx=0.29, rely=0.61)

        self.otp_entry = Entry(self.root, font=("Comic Sans MS", 19), width=35)
        self.otp_entry.place(relx=0.19, rely=0.67)

        self.verify_button = customtkinter.CTkButton(self.root,
                                        width=170,
                                        height=5,
                                        text="Verify",
                                        font=("Comic Sans MS", 22,"bold"), 
                                        command=self.verify,
                                        text_color="white",
                                        fg_color="#606C5D",
                                        hover_color="#1c2f36")
        self.verify_button.place(relx=0.5, rely=0.78, anchor='center')

    def generate_OTP(self):
        return str(random.randint(100000,999999))

    def send_mail(self, receiver_email, OTP):
        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=self.context) as server:
            server.login(self.sender_email, self.sender_password)
            subject = 'SYNC INTERN OTP Authentication'
            body = f'Your OTP is {OTP}. Please use this to verify your account.'
            message = f'Subject: {subject}\n\n{body}'
            server.sendmail(self.sender_email, receiver_email, message)

    def send_otp(self):
        receiver_email = self.email_entry.get()
        self.send_mail(receiver_email, self.OTP)
        messagebox.showinfo("OTP Verification", "OTP sent to your email.")

    def verify(self):
        user_otp = self.otp_entry.get()
        if user_otp == self.OTP:
            messagebox.showinfo("OTP Verification", "OTP verified!")
        else:
            messagebox.showerror("OTP Verification", "Invalid OTP. Please try again.")

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    otp_verification_gui = OTPVerificationGUI()
    otp_verification_gui.run()
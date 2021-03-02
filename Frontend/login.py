from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from datetime import *
import time
from math import *


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        title = Label(self.root, text="Login System for Hotel Management System", font=("poopins", 20, "bold"),
                      bg="#04444a", fg="white").place(x=0, y=0)

        left_lbl = Label(self.root, bg="#021e2f", bd=0)
        left_lbl.place(x=0, y=0, relheight=1, width=600)

        right_lbl = Label(self.root, bg="#031F3c", bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)

        # ======= Frame====================
        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=250, y=100, width=800, height=500)

        title = Label(login_frame, text="LOGIN HERE", font=("poopins", 30, "bold"), bg="white", fg="#08A3D2").place(
            x=300, y=50)

        email = Label(login_frame, text="Email Address", font=("poopins", 18, "bold"), bg="white", fg="black").place(
            x=250, y=150)
        self.txt_email = Entry(login_frame, font=("Times new roman", 15), bg="Lightgray")
        self.txt_email.place(x=250, y=180, width=350, height=35)

        pasw = Label(login_frame, text="Password", font=("poopins", 18, "bold"), bg="white", fg="black").place(x=250,
                                                                                                               y=250)
        self.txt_pasw = Entry(login_frame, font=("Times new roman", 15), bg="Lightgray")
        self.txt_pasw.place(x=250, y=280, width=350, height=35)

        btn_reg = Button(login_frame, text="Register new Account", font=("Times new roman", 14, "bold"), bg="white",
                         bd=1, fg="red", cursor="hand2").place(x=250, y=340)
        btn_log = Button(login_frame, text="LOGIN", font=("POOPINS", 20, "bold"), bg="white", fg="green",
                         cursor="hand2").place(x=250, y=390, width=180, height=40)

        # ==========clock============================
        self.lbl = Label(self.root, text="\nWebcode clock", font=("Book Antiqua", 25, "bold"), compound=BOTTOM,
                         bg="#081923", fg="White", bd=0)
        self.lbl.place(x=90, y=120, height=450, width=350)

        self.working()

    def clock_image(self, hr, min_, sec_):
        clock = Image.new("RGB", (400, 400), (8, 25, 35))
        draw = ImageDraw.Draw(clock)
        #  for clock Image=====
        bg = Image.open("images/clock1.jpg")
        bg = bg.resize((300, 300), Image.ANTIALIAS)
        clock.paste(bg, (50, 50))
        # ===for Hour line Image===
        origin = 200, 200
        draw.line((origin, 200 + 50 * sin(radians(hr)), 200 - 50 * cos(radians(hr))), fill="black", width=4)
        # ===for minute line Image===
        draw.line((origin, 200 + 80 * sin(radians(min_)), 200 - 80 * cos(radians(min_))), fill="blue", width=3)
        # ===for Second line Image===
        draw.line((origin, 200 + 100 * sin(radians(sec_)), 200 - 100 * cos(radians(sec_))), fill="green", width=2)
        draw.ellipse((190, 190, 210, 210), fill="black")
        clock.save("clock_new.png")

    def working(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second

        hr = (h / 12) * 360
        min_ = (m / 60) * 360
        sec_ = (s / 60) * 360
        self.clock_image(hr, min_, sec_)
        self.img = ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(190, self.working)


root = Tk()
obj = Login_window(root)
root.mainloop()
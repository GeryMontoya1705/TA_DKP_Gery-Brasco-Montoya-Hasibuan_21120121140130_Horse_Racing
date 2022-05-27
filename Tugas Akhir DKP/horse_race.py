from tkinter import *
import time
import random
from tkinter import messagebox

#Aksekoris
winner = False

mon_boy_x = 12
mon_boy_y = 5

white_hawk_x = -2
white_hawk_y = 110

biscuit_x = -5
biscuit_y = 200

leaderboard = []

dataBoard1 = "1. Monaghan Boy \n2. White Hawk \n3. Biscuit"
dataBoard2 = "1. Monaghan Boy \n2. Biscuit \n3. White Hawk"
dataBoard3 = "1. White Hawk \n2. Monaghan Boy \n3. Biscuit"
dataBoard4 = "1. White Hawk \n2. Biscuit \n3. White Hawk"
dataBoard5 = "1. Biscuit \n2. Monaghan Boy \n3. White Hawk"
dataBoard6 = "1. Biscuit \n2. White Hawk \n3. Monaghan Boy"

#Pergerakan Kuda
def start_game():
    global mon_boy_x
    global white_hawk_x
    global biscuit_x
    global winner

    while winner == False:
        time.sleep(0.05)
        random_move_mon_boy = random.randint(0,20)
        random_move_white_hawk = random.randint(0,20)
        random_move_biscuit = random.randint(0,20)
        #Update X Positions of Horses
        mon_boy_x += random_move_mon_boy
        white_hawk_x += random_move_white_hawk
        biscuit_x += random_move_biscuit

        move_horses(random_move_mon_boy, random_move_white_hawk, random_move_biscuit)
        main_screen.update()
        winner = check_winner()

    if winner == "Tie":
        Label(main_screen, text = winner, font = ('Times New Roman', 20), fg = "green").place(x = 270, y = 380)
    else:
        Label(main_screen, text = winner + " Wins !!", font = ('Times New Roman', 20), fg = "green").place(x = 230, y = 380)
        view_leaderboard()

def move_horses(mon_boy_random_move, white_hawk_random_move, biscuit_random_move):
    canvas.move(mon_boy, mon_boy_random_move,0)
    canvas.move(white_hawk, white_hawk_random_move,0)
    canvas.move(biscuit, biscuit_random_move,0)

#Cek Pemenang dan Stack Leaderboard
def check_winner():
    if mon_boy_x >= 750 and white_hawk_x >= 750 and biscuit_x >= 750:
        return "Tie"
    elif mon_boy_x >= 750 and white_hawk_x >= 750:
        return "Tie"
    elif mon_boy_x >= 750 and biscuit_x >= 750:
        return "Tie"
    elif white_hawk_x >= 750 and biscuit_x >= 750:
        return "Tie"
    elif mon_boy_x >= 750:
        if mon_boy_x > white_hawk_x and white_hawk_x > biscuit_x:
            leaderboard.append(dataBoard1)
        elif mon_boy_x > biscuit_x and biscuit_x > white_hawk_x:
            leaderboard.append(dataBoard2)
        return "Monaghan Boy (Black)"
    elif white_hawk_x >= 750:
        if white_hawk_x > mon_boy_x and mon_boy_x > biscuit_x:
            leaderboard.append(dataBoard3)
        elif white_hawk_x > biscuit_x and biscuit_x > mon_boy_x:
            leaderboard.append(dataBoard4)
        return "White Hawk (White)"
    elif biscuit_x >= 750:
        if biscuit_x > mon_boy_x and mon_boy_x > white_hawk_x:
            leaderboard.append(dataBoard4)
        elif biscuit_x > white_hawk_x and white_hawk_x > mon_boy_x:
            leaderboard.append(dataBoard5)
        return "Biscuit (Brown)"
    return False

#Leaderboard di Message Box
def view_leaderboard():
    messagebox.showinfo('Leaderboard',leaderboard)

#Setting Screen Utama
main_screen = Tk()
main_screen.title('Horse Racing')
main_screen.geometry('800x430')
main_screen.config(background = 'white')

#Setting Canvas Main Screen
canvas = Canvas(main_screen, width = 800, height = 312, bg = 'yellow green')
canvas.pack(pady = 20)

#Import Gambar Kuda
mon_boy_img = PhotoImage(file = "C:\\Users\\Gery Montoya\\Documents\\Kuliah\\Academics\\Semester 2\\Note and Material\\Practicum of Basic Computer and Programming\\Python\\Tugas Akhir DKP\\images\\mon_boy.png")
white_hawk_img = PhotoImage(file = "C:\\Users\\Gery Montoya\\Documents\\Kuliah\\Academics\\Semester 2\\Note and Material\\Practicum of Basic Computer and Programming\\Python\\Tugas Akhir DKP\\images\\white_hawk.png")
biscuit_img = PhotoImage(file = "C:\\Users\\Gery Montoya\\Documents\\Kuliah\\Academics\\Semester 2\\Note and Material\\Practicum of Basic Computer and Programming\\Python\\Tugas Akhir DKP\\images\\biscuit.png")

#Edit Ukuran Gambar
mon_boy_img = mon_boy_img.zoom(15)
mon_boy_img = mon_boy_img.subsample(70)
white_hawk_img = white_hawk_img.zoom(15)
white_hawk_img = white_hawk_img.subsample(70)
biscuit_img = biscuit_img.zoom(15)
biscuit_img = biscuit_img.subsample(65)

#Start Track
start_img = PhotoImage(file = "C:\\Users\\Gery Montoya\\Documents\\Kuliah\\Academics\\Semester 2\\Note and Material\\Practicum of Basic Computer and Programming\\Python\\Tugas Akhir DKP\\images\\start.png")
start_img = start_img.zoom(15)
start_img = start_img.subsample(18)
start_x1 = 150
start_y1 = 120
start1 = canvas.create_image(start_x1, start_y1, image = start_img)
start_x2 = 767
start_y2 = 120
start2 = canvas.create_image(start_x2, start_y2, image = start_img)

#Menempatkan Gambar Kuda ke Canvas Main Screen
mon_boy = canvas.create_image(mon_boy_x, mon_boy_y, anchor = NW, image = mon_boy_img)
white_hawk = canvas.create_image(white_hawk_x, white_hawk_y, anchor = NW, image = white_hawk_img)
biscuit = canvas.create_image(biscuit_x, biscuit_y, anchor = NW, image = biscuit_img)

#Aksesoris Screen Utama
l1 = Label(main_screen, text = 'Race Start!', font = ('Times New Roman', 20), bg = "white")
l1.place(x = 330, y = 340)

#Window Pertama
window = Tk()
window.geometry("300x300")
window.title("Bet Placement")
window.config(background = 'red')

#Aksesoris Window Pertama

labelLogo = Label(window,
                  text = "INSIDE TRACK",
                  font = ("times new roman", 25,"bold"),
                  fg = 'white',
                  bg = 'red').place(x=25, y=20)

#Tempat Input
labelName = Label(window,
                  text = "Name\t:",
                  font = ("times new roman", 10),
                  fg = 'white',
                  bg = 'red').place(x=30, y=80)
labelCash = Label(window,
                  text = "Cash\t:",
                  font = ("times new roman", 10),
                  fg = 'white',
                  bg = 'red').place(x=30, y=110)
labelHorse = Label(window,
                text = "Horse\t:",
                font = ("times new roman", 10),
                fg = 'white',
                bg = 'red').place(x=30, y=140)

#Input
strName = StringVar()
entrynama = Entry(window,
                  textvariable = strName,
                  font = ("times new roman", 10)).place(x=100, y=80)

strCash = StringVar()
entrycash = Entry(window,
                  textvariable = strCash,
                  font = ("times new roman", 10)).place(x=100, y=110)

#Pilihan dalam Button
radio = IntVar()
Radiobutton(window,
                 text = "Monaghan Boy (Black)",
                 font = ("times new roman", 10),
                 fg = 'black',
                 bg = 'red',
                 variable = radio,
                 value = 1).place(x = 100, y = 140)

Radiobutton(window,
                 text = "White Hawk (White)",
                 font = ("times new roman", 10),
                 fg = 'black',
                 bg = 'red',
                 variable = radio,
                 value = 2).place(x = 100, y = 160)

Radiobutton(window,
                 text = "Biscuit (Brown)",
                 font = ("times new roman", 10),
                 fg = 'black',
                 bg = 'red',
                 variable = radio,
                 value = 3,).place(x = 100, y = 180)

#Eksekusi dalam Button
buttonsubmit = Button(window, 
                text = "Start!",
                command = start_game, 
                font = ("Times New Roman", 13),
                fg = "black",
                state = ACTIVE 
                ).place(x = 125, y = 230)

#Loop Kedua Window
main_screen.mainloop()
window.mainloop()
from tkinter import *
import tkinter.messagebox as msgbox
from PIL import ImageTk, Image
from QuestionsDB import questions
import random


answer = 0
score = 0
life = 3
player_name = ""
highest_score = 0
highest_name = ""


try:
    with open("highscore.txt", 'r') as hs:
        if hs.read():
            hs.seek(0)
            data = hs.read().split()
            highest_name = data[1]
            highest_score = int(data[3])

except FileNotFoundError:
    pass

r = random.choice(questions)


def rand_upd():
    global r, questions
    questions.remove(r)
    if questions:
        r = random.choice(questions)
    else:
        gameover()


def a_resp():
    global answer
    answer = 1
    check_ans()


def b_resp():
    global answer
    answer = 2
    check_ans()


def c_resp():
    global answer
    answer = 3
    check_ans()


def d_resp():
    global answer
    answer = 4
    check_ans()


def closegame():
    choice = msgbox.askyesno( root, "Do You Really Want to Quit?")
    if choice:
        quit()


def check_ans():
    global score, answer, life, r, current_score
    if life > 1:
        if answer == r['answer']:
            score = score + 1
            loc = score * 60
            canvas_tower.create_image(2, 660 - loc, anchor=NW, image=new_image2)
            msgbox.showinfo("Correct!","That's Right! Congratulations!\n Your tower is now higher by one more block")


        else:
            msgbox.showerror("Incorrect!","Sorry, that's not correct. You lost a life")
            life = life - 1
        rand_upd()
        canvas.itemconfig(ques, text=r['question'])
        canvas1.itemconfig(rem_life, text=f"Remaining lives : {'❤' * life}")
        b1['text'] = r['choices'][0]
        b2['text'] = r['choices'][1]
        b3['text'] = r['choices'][2]
        b4['text'] = r['choices'][3]
        current_score_canvas.itemconfig(score_current, text=f"Your Current Score : {score}")

    else:
        if score >= highest_score:
            with open('highscore.txt','w') as f:
                f.write(f"Name: {player_name}\nScore: {score}")
        gameover()

def gameover():
    canvas_tower.delete("all")
    msgbox.showinfo("GAME OVER!", "The game is over")
    exit()

def start():
    global player_name
    if name.get():
        player_name = name.get()
        first.destroy()
    else:
        msgbox.showerror("Name Error", 'Please Enter Your Name')


first = Tk()

first.geometry("1500x800")
first.config(bg='#7BE0AD')
cs = Canvas(first, width=1200, height=80, bg="#F7A072")

cs.create_text(600, 40, text="GET.... SET.... GO....", fill='black', font=('', '35', 'bold'))
cs.place(relx=0.08, rely=0.25)

cs1 = Canvas(first, width=450, height=60, bg="#F7A072")
cs1.create_text(230, 30, text="Enter Your Name & Click Start", fill='black', font=('', '20'))
cs1.place(relx=0.17, rely=0.4)

name = Entry(first, width=19, font=('', '40'), relief=RIDGE)
name.place(relx=0.47, rely=0.4)

sub = Button(text="Let's Play", background='#F7A072', fg='black', font=('', '35'), relief=GROOVE, command=start)
sub.place(relx=0.43, rely=0.52)

first.mainloop()

if player_name:
    root = Tk()
    root.geometry("1920x1080")

    menubar = Menu(root, background='blue', fg='white')
    file = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='File', menu=file)

    file.add_command(label='New Game')
    file.add_command(label='Save Game')
    file.add_command(label='Exit', command=closegame)


    root.config(bg='white', menu=menubar)
    root.title("Quiz Game")

# metrics and question block

    welcome = Canvas(root, width=1450, height=40, bg="#E0E0EE")
    welcome.create_text(700, 24, text=f"★   WELCOME {player_name.upper()}   ★", fill="#83838B", font=(" ", 24))
    welcome.place(relx=0.02, rely=0.02)

    canvas2 = Canvas(root, width=400, height=80, bg="royalblue")
    curr_score = canvas2.create_text(200, 30, text=f"HIGHEST SCORE : {highest_score} towers by {highest_name}", fill="white", font=("", 16))
    canvas2.place(relx=0.61, rely=0.12)

    canvas1 = Canvas(root, width=400, height=80, bg="#856ff8")
    rem_life = canvas1.create_text(200, 30, text=f"Remaining lives : {'❤️' * life}", fill="white", font=("", 16))
    canvas1.place(relx=0.61, rely=0.25)

    canvas = Canvas(root, width=500, height=300, bg='black')
    ques = canvas.create_text(250, 60, text=r['question'], fill="white", font=("", 14), width=500)
    canvas.place(relx=0.6, rely=0.39)




    b1 = Button(root, text=r['choices'][0],font=(" ", 30), padx=25,command=a_resp)
    b1.place(relx=0.582, rely=0.79)

    b2 = Button(root, text=r['choices'][1], font=(" ", 30), padx=25, command=b_resp)
    b2.place(relx=0.676, rely=0.79)

    b3 = Button(root, text=r['choices'][2], font=(" ", 30), padx=25, command=c_resp)
    b3.place(relx=0.77, rely=0.79)

    b4 = Button(root, text=r['choices'][3], font=(" ", 30), padx=25, command=d_resp)
    b4.place(relx=0.87, rely=0.79)

# tower code

    canvas_tower = Canvas(root, width=245, height=660,background='white')
    img2 = (Image.open("D:/Users/HP/block.png"))
    resized_image2 = img2.resize((245, 60), Image.LANCZOS)
    new_image2 = ImageTk.PhotoImage(resized_image2)
    canvas_tower.place(relx=0.04, rely=0.10)

    current_score_canvas = Canvas(root, width=250, height=40, bg="red")
    score_current = current_score_canvas.create_text(140, 25, text=f"Your current Score : {score}", fill="white", font=("", 12))
    current_score_canvas.place(relx=0.36, rely=0.75)

    canvas_always = Canvas(root, width=245, height=60,background='white')
    img1 = (Image.open("D:/Users/HP/block.png"))
    resized_image1 = img1.resize((245, 60), Image.LANCZOS)
    new_image1 = ImageTk.PhotoImage(resized_image1)
    canvas_always.create_image(2, 2, anchor=NW, image=new_image1)
    canvas_always.place(relx=0.36, rely=0.82)

    root.mainloop()


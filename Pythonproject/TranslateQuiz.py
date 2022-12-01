from tkinter import *
from translate import Translator
import random

root = Tk()
root.resizable(0,0)
ts = Translator(to_lang="th")
root.title("Translate Quiz")
labelhead = Label(root,text = "Translate Quiz",font = "arial 20 bold").grid(row=0,column=1)

#list Quizz
eng_list = ["Signal","Wallet","Read","Random","Different","Empty","Telephone","Bakery","Company ","Interview","Salary","Arrive"
              ,"Ferry","Route","Road","Correct","Solve","Various","Increase","Practice","Afford","Economy","Domestic","Efficiently"
              ,"Learned","Allow"]
empty_list = ["Signal","Wallet","Read","Random","Different","Empty","Telephone","Bakery","Company ","Interview","Salary","Arrive"
              ,"Ferry","Route","Road","Correct","Solve","Various","Increase","Practice","Afford","Economy","Domestic","Efficiently"
              ,"Learned","Allow"]

#Translate
def bt1click():
    Label(root, font="arial 10", bg="#FFF", width=22).grid(row=3, column=1)
    Engtxt.get()
    thtxt = ts.translate(Engtxt.get())
    #Label(root,width=70,bg="#FFF").grid(row=3,column=1)
    Label(root,text=thtxt,font="arial 10",bg="#FFF").grid(row=3,column=1)
    eng_list.append(str(Engtext.get()))

#Reset
def bt2click():
    Label(root,font="arial 10",bg="#FFF",width=22).grid(row=3, column=1)
    Engtext.delete(0,END)

#Quiz
def bt3click():
    global button4, button5, answertxt, answer, ranEmp, ranEng
    Label(root, text="                 ", font="arial 32", fg="red").grid(row=15, column=1)
    Label(root, text="                ", font="arial 32", fg="red").grid(row=16, column=1)
    Label(root,font="arial 10",bg="#FFF",width=22).grid(row=3, column=1)
    Engtext.delete(0,END)

    ranEmp = random.choice(empty_list)
    if not eng_list:
        pass
    else:
        ranEng = random.choice(eng_list)

    Label(root,text="Start Quiz",font="arial 20 bold").grid(row=10,column=1)
    Label(root,font="arial 22",width=10).grid(row=12, column=1)

    if not eng_list:
        Label(root, text=ranEmp, font="arial 20", bg="#FFF").grid(row=12, column=1)
    else:
        Label(root, text=ranEng, font="arial 20", bg="#FFF").grid(row=12, column=1)

    Label(root,text="พิมพ์คำตอบคองคุณ : ",font="arial 10").grid(row=13,column=0)
    answer = StringVar()
    answertxt = Entry(root,width=30,textvariable=answer).grid(row=13,column=1)

    #button submit
    button4 = Button(root,text="Submit",command=bt4click).grid(row=17,column=1)

    # button play again
    #button5 = Button(root, text="Play again", command=bt5click).grid(row=17, column=2)

#Submit Quiz
def bt4click():
    global LC1,LC2,LI1,LI2,LI3,LI4
    tsEmp = ts.translate(ranEmp)
    #Label(root, text="          ", font="arial 32", fg="red").grid(row=17, column=1)
    # button play again
    button5 = Button(root, text="Play again", command=bt5click).grid(row=17, column=1)
    if not eng_list:
        pass
    else:
        tsEng = ts.translate(ranEng)
    ansget = answer.get()
    if not eng_list:
        if ansget == tsEmp:
            LC1 = Label(root,text="Correct!!!", font="arial 32",fg="Green").grid(row=15, column=1)
        else:
            if ansget != tsEmp:
                LI1 = Label(root,text="Incorrect!!!", font="arial 32", fg="red").grid(row=15, column=1)
                LI2 = Label(root, text=tsEmp, font="arial 28", fg="blue").grid(row=16, column=1)
    else:
        if ansget == tsEng:
            LC2 = Label(root, text="Correct!!!", font="arial 32", fg="Green").grid(row=15, column=1)
        else:
            if ansget != tsEng:
                LI3 = Label(root, text="Incorrect!!!", font="arial 32", fg="red").grid(row=15, column=1)
                LI4 = Label(root, text=tsEng, font="arial 28", fg="blue").grid(row=16, column=1)

#play again
def bt5click():
    global button4, button5, answertxt, answer, ranEmp, ranEng
    Label(root, text="                 ", font="arial 32", fg="red").grid(row=15, column=1)
    Label(root, text="                ", font="arial 32", fg="red").grid(row=16, column=1)
    Label(root,font="arial 10",bg="#FFF",width=22).grid(row=3, column=1)
    Engtext.delete(0,END)

    ranEmp = random.choice(empty_list)
    if not eng_list:
        pass
    else:
        ranEng = random.choice(eng_list)

    Label(root,text="Start Quiz",font="arial 20 bold").grid(row=10,column=1)
    Label(root,font="arial 22",width=10).grid(row=12, column=1)

    if not eng_list:
        Label(root, text=ranEmp, font="arial 20", bg="#FFF").grid(row=12, column=1)
    else:
        Label(root, text=ranEng, font="arial 20", bg="#FFF").grid(row=12, column=1)

    Label(root,text="พิมพ์คำตอบคองคุณ : ",font="arial 10").grid(row=13,column=0)
    answer = StringVar()
    answertxt = Entry(root,width=30,textvariable=answer).grid(row=13,column=1)

    #button submit
    Label(root, text="          ", font="arial 32", fg="red").grid(row=17, column=1)
    button4 = Button(root,text="Submit",command=bt4click).grid(row=17,column=1)

    #button play again
    #button5 = Button(root,text="Play again",command=bt5click).grid(row=17,column=2)


#Eng Textbox
label_eng = Label(root,text = "     Enter eng text : ",font = "arial 10").grid(row=2,column=0)
Engtxt = StringVar()
Engtext = Entry(root,width=30,textvariable=Engtxt)
Engtext.grid(row=2,column=1)

#Thai textbox
thai_label = Label(root,text="                 คำแปล : ",font="arial 10").grid(row=3,column=0)
Label(root,font="arial 10",bg="#FFF",width=22).grid(row=3, column=1)

#space
Label(root).grid(row=1, column=1)
Label(root).grid(row=4, column=1)
Label(root).grid(row=5, column=1)
Label(root).grid(row=8, column=1)
Label(root).grid(row=9, column=1)
Label(root).grid(row=11, column=1)
Label(root).grid(row=15, column=1)
Label(root).grid(row=14, column=1)

#translate button
button1 = Button(root,text="Translate",command=bt1click).grid(row=6,column=1)

#Del Button
button2 = Button(root,text="Reset",command=bt2click).grid(row=6,column=2)

#Quiz button
button3 = Button(root,text="Quiz",command=bt3click).grid(row=6,column=0)

#screen size
root.geometry("420x550")
root.mainloop()

from tkinter import *
import tkinter as tk
from db import  DBhelper
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image,ImageTk
import time
import shutil, os

class quizapp:



    def __init__(self):
        self.db = DBhelper()
        self.root = Tk()

        self.root.title("My Quiz App")

        self.root.configure(background="#043CFA")

        self.root.minsize(1000,600)
        self.root.maxsize(1000,600)

        self.load_gui()

    def load_gui(self):
        self.clear()

        self.label1 = Label(self.root, text="Quiz App", fg="cyan", bg="#043CFA")
        self.label1.configure(font=("Times", 30, "bold"))
        self.label1.pack(pady=(10, 20))

        self.label2 = Label(self.root, text="Email", fg="white", bg="#043CFA")
        self.label2.configure(font=("Times", 20, "italic"))
        self.label2.pack(pady=(5, 5))

        self.emailinput = Entry(self.root)
        self.emailinput.configure(font=("Times",20,"italic"))
        self.emailinput.pack(pady=(0, 40), ipadx=40, ipady=5)

        self.label3 = Label(self.root, text="Password", fg="white", bg="#043CFA")
        self.label3.configure(font=("Times", 20, "italic"))
        self.label3.pack(pady=(0, 5))

        self.password = Entry(self.root)
        self.password.configure(font=("Times", 20, "italic"))
        self.password.pack(pady=(0, 20), ipadx=40, ipady=5)

        self.login = Button(self.root, text="Login", bg="white", command=lambda: self.log_in())
        self.login.configure(font=("Times", 20))
        self.login.pack(pady=(0, 50), ipadx=50, ipady=4)

        self.label4 = Label(self.root, text="Not Registered?", fg="white", bg="#043CFA")
        self.label4.configure(font=("Times", 20, "italic"))
        self.label4.pack(pady=(10, 5))

        self.register = Button(self.root, text="Sign up", bg="white", command=lambda: self.register_form())
        self.register.configure(font=("Times", 15))
        self.register.pack(pady=(5, 10), ipadx=30, ipady=4)

        self.root.mainloop()

    def log_in(self):
        email = self.emailinput.get()
        password = self.password.get()
        data = self.db.check_login(email, password)

        if len(data)>0:
            self.clear()
            self.user_id=data[0][0]
            self.user_data=data[0]
            self.answer_count =0
            self.load_user_details(mode=1)
        else:
            messagebox.showerror("Error","Incorrect Email/password")


    def load_user_details(self,mode=None):
        if mode==1:
            self.main_window(self.user_data,mode=1)


    def navbar(self,mode=None):

        menu = Menu(self.root)
        self.root.config(menu=menu)

        if mode==1:
            menu.add_command(label="My Profile", command=lambda: self.main_window(self.user_data,mode=1))
            menu.add_command(label="Show Leaderboard",command=lambda :self.leaders())
            menu.add_command(label="Logout", command=lambda: self.logout())
        if mode==2:
            menu.add_command(label="My Profile", command=lambda: self.main_window(self.user_data, mode=2))
            menu.add_command(label="Show Leaderboard", command=lambda: self.leaders())
            menu.add_command(label="Logout", command=lambda: self.logout())


    def leaders(self):

        topper=self.db.leader_board()
        print (topper)
        self.clear()
        self.frame6=LabelFrame(self.root)
        self.frame6.pack(padx=30,pady=20)
        lb=Listbox(self.frame6,width=400)

        for i in range(0,len(topper)):
            lb.insert(i+1,"     "+str(i+1)+"         "+topper[i][0]+" (Score="+str(topper[i][1])+")")
        lb.configure(font=("Times",20,'italic'),fg='red',bg="#22E7EA")
        lb.pack(padx=(20,20),pady=15)

    def logout(self):
        self.navbar(mode=0)
        self.clear()
        self.load_gui()



    def main_window(self,data,mode=None):

        if mode==1:
            self.clear()

            self.navbar(mode=1)

            imageUrl = "images/{}".format(data[6])

            load = Image.open(imageUrl)
            load = load.resize((200,200), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)

            img = Label(image=render)
            img.image = render
            img.pack()

            self.label1 = Label(self.root, text="Name: "+" "+data[1], fg="white", bg="#043CFA")
            self.label1.configure(font=("Times", 20, "bold"))
            self.label1.pack(pady=(20, 30))

            self.label2 = Label(self.root, text="College:  " + data[4], fg="white", bg="#043CFA")
            self.label2.configure(font=("Times", 15, "bold"))
            self.label2.pack(pady=(5, 30))


            self.label3 = Label(self.root, text="Date of Birth:  " + str(data[5]), fg="white", bg="#043CFA")
            self.label3.configure(font=("Times", 15, "bold"))
            self.label3.pack(pady=(5, 40))

            self.label4 = Label(self.root, text="Check your knowledge" , fg="#EAF4F4", bg="#043CFA")
            self.label4.configure(font=("Times", 20, "bold"))
            self.label4.pack(pady=(5,2))

            self.quiz=Button(self.root,text="Quiz",bg="#25F0D4",command=lambda: self.quiz_window(self.user_data,mode=1,index=1))
            self.quiz.configure(font=("Times",15,"italic"))
            self.quiz.pack(pady=(1,5),ipadx=20)

        else:
            self.clear()
            self.navbar(mode=1)

            imageUrl = "images/{}".format(data[6])

            load = Image.open(imageUrl)
            load = load.resize((200, 200), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)

            img = Label(image=render)
            img.image = render
            img.pack()

            self.label1 = Label(self.root, text="Name: " + " " + data[1], fg="white", bg="#043CFA")
            self.label1.configure(font=("Times", 20, "bold"))
            self.label1.pack(pady=(20, 30))

            self.label2 = Label(self.root, text="College:  " + data[4], fg="white", bg="#043CFA")
            self.label2.configure(font=("Times", 15, "bold"))
            self.label2.pack(pady=(5, 30))

            self.label3 = Label(self.root, text="Date of Birth:  " + str(data[5]), fg="white", bg="#043CFA")
            self.label3.configure(font=("Times", 15, "bold"))
            self.label3.pack(pady=(5, 40))


    def quiz_window(self,data,mode=None,index=None):

        self.q_no=index

        if mode==1:

            self.navbar(mode=0)

            self.clear()
            self.label0 = Label(self.root, text="Questions" , fg="yellow",bg="blue")
            self.label0.configure(font=("Times", 30, "bold"))
            self.label0.place(x=350,y=20)

            self.freame2=LabelFrame(self.root,height=400,width=700)
            self.freame2.place(x=30,y=80)

            self.question = self.db.quiz_set(self.q_no)
            self.answer=self.question[0][-1]


            option=[(self.question[0][2],1),(self.question[0][3],2),(self.question[0][4],3),(self.question[0][5],4)]


            self.qus = Label(self.freame2, text="Q" + str(self.question[0][0]) + ". " + self.question[0][1])
            self.qus.configure(font=("Times", 20, "italic"))
            self.qus.pack(padx=5, pady=10)

            self.v = IntVar()
            for text,val in option:
                self.op=Radiobutton(self.freame2,text=text,padx=20,variable=self.v,value=val,command=self.score)
                self.op.configure(font=("Times",20))
                self.op.pack(anchor=W)


            questions = self.db.fetch_questions(self.q_no)
            self.num = len(questions)


            self.frame3 =Frame(self.root,bg='#043CFA')
            self.frame3.place(x=250,y=390)


            if index != (self.num+1):
                self.save = Button(self.frame3, text="Save & Next", font=("Time", 20, 'italic'), bg="cyan",command=lambda:self.recover(index=index + 1))
                self.save.pack()


            self.freame1 = LabelFrame(self.root, width=500, height=2000)
            self.freame1.pack(padx=(750,10),pady=(130,10))

            imageUrl = "images/{}".format(data[6])
            load = Image.open(imageUrl)
            load = load.resize((100, 100), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = Label(image=render)
            img.image = render
            img.place(x=810,y=20)

            self.label1 = Label(self.freame1, text="Name: " + " " + data[1], fg="blue")
            self.label1.configure(font=("Times", 12, "bold"))
            self.label1.pack(pady=10)

            self.label3 = Label(self.freame1, text="Your's time left", fg="red", bg="white")
            self.label3.configure(font=("Times",15, "bold"))
            self.label3.pack(pady=20)


            self.label2=Label(self.freame1,fg="red")
            self.label2.configure(font=("Times",30,"bold"))
            self.label2.pack()
            self.countdown(remaining=600)

            self.submit= Button(self.freame1, text="Submit", bg="#25F0D4",command=lambda :self.submit_btn())
            self.submit.configure(font=("Times", 15, "italic"))
            self.submit.pack(pady=70)

        else:

            self.q_clear()

            self.question = self.db.quiz_set(self.q_no)
            self.answer = self.question[0][-1]


            option = [(self.question[0][2], 1), (self.question[0][3], 2), (self.question[0][4], 3),
                      (self.question[0][5], 4)]



            self.qus = Label(self.freame2, text="Q" + str(self.question[0][0]) + ". " + self.question[0][1])
            self.qus.configure(font=("Times",20, "italic"))
            self.qus.pack(padx=5, pady=10)

            self.v = IntVar()
            for text, val in option:
                self.op = Radiobutton(self.freame2, text=text, padx=20, variable=self.v, value=val,command=self.score)
                self.op.configure(font=("Times", 20))
                self.op.pack(anchor=W)

            self.frame3= Frame(self.root,bg='#043CFA')
            self.frame3.place(x=250,y=390)

            questions = self.db.fetch_questions(self.q_no)
            self.num = len(questions)

            if index != (self.num+1):
                self.save = Button(self.frame3, text="Save & Next", font=("Time", 20, 'italic'), bg="cyan",command=lambda:self.recover(index=index + 1))
                self.save.pack()

    def recover(self,index=None):
        self.quiz_window(self.user_data,mode=2,index=index)



    def score(self):

        if  self.v.get()==self.answer:
            self.answer_count+=1


    def submit_btn(self):

        self.db.score_update(self.user_id,self.answer_count)

        self.clear()

        self.navbar(mode=2)

        self.frame5=LabelFrame(self.root,bg='cyan').pack()
        self.awnswer_display=Label(self.frame5,text="Number of correct answer",font=("Times",50,"italic"),fg="#FC5800",bg='black').pack(pady=(100,5))

        self.correct=Label(self.frame5,text=self.answer_count,font=("Times",80,"bold"),fg='#FC5800',bg='black').pack(ipadx=50,pady=30)



    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining
            self.minute = self.remaining // 60
            self.remaining = self.remaining % 60

        if self.minute == -1:
            self.label2.configure(text="Time's up!")
            self.root.after(1000,self.submit_btn)

        else:

            self.label2.configure(text="{}:{}".format( self.minute,self.remaining))
            self.remaining = self.remaining - 1

            if self.remaining==-1:
                self.minute-=1
                self.remaining=59
            self.freame1.after(1000, self.countdown)





    def register_form(self):
        self.clear()

        self.label1 = Label(self.root, text="Fill the registration form carefully", fg="white", bg="#043CFA")
        self.label1.configure(font=("Times", 20, "italic"))
        self.label1.pack(pady=(10,20))

        frame = Frame(self.root)
        frame.pack()

        self.label2=Label(frame,text="Name: ",fg="white", bg="#043CFA")
        self.label2.configure(font=("Times", 20, "italic"))
        self.label2.pack(side="left")

        self.name=Entry(frame)
        self.name.configure(font=("Times",20,"italic"))
        self.name.pack(side="left")

        frame1 = Frame(self.root)
        frame1.pack(pady=(10,10))

        self.label3 = Label(frame1, text="Email: ", fg="white", bg="#043CFA")
        self.label3.configure(font=("Times", 20, "italic"))
        self.label3.pack(side="left")

        self.email = Entry(frame1)
        self.email.configure(font=("Times", 20, "italic"))
        self.email.pack(side="left")

        frame2 = Frame(self.root)
        frame2.pack(pady=(0, 10))

        self.label4 = Label(frame2, text="Password: ", fg="white", bg="#043CFA")
        self.label4.configure(font=("Times", 20, "italic"))
        self.label4.pack(side="left")

        self.password = Entry(frame2)
        self.password.configure(font=("Times", 20, "italic"))
        self.password.pack(side="left")

        frame3 = Frame(self.root)
        frame3.pack(pady=(0, 10))

        self.label5 = Label(frame3, text="College: ", fg="white", bg="#043CFA")
        self.label5.configure(font=("Times", 20, "italic"))
        self.label5.pack(side="left")

        self.college = Entry(frame3)
        self.college.configure(font=("Times", 20, "italic"))
        self.college.pack(side="left")

        frame4 = Frame(self.root)
        frame4.pack(pady=(0, 10))

        self.label6 = Label(frame4, text='''Date of birth
        (YYYY-MM-DD): ''', fg="white", bg="#043CFA")
        self.label6.configure(font=("Times",10, "italic"))
        self.label6.pack(side="left")

        self.dob= Entry(frame4)
        self.dob.configure(font=("Times", 20, "italic"))
        self.dob.pack(side="left")

        self.filebtn = Button(self.root, text="Upload Pic", bg="white", command=lambda: self.upload_file())
        self.filebtn.pack(pady=(15, 0), ipadx=40, ipady=4)

        self.filename = Label(self.root)
        self.filename.pack(pady=(5, 5), ipadx=40, ipady=4)

        self.register = Button(self.root, text="Sign Up", bg="white", command=lambda: self.reg_submit())
        self.register.configure(font=("Times",15,"italic"))
        self.register.pack(pady=(20,30), ipadx=70, ipady=4)

        self.label4 = Label(self.root, text="To login Press the Button", fg="white", bg="#043CFA")
        self.label4.configure(font=("Times", 15, "italic"))
        self.label4.pack(pady=(10,3))

        self.register = Button(self.root, text="Sign In", bg="white", command=lambda: self.load_gui())
        self.register.configure(font=("Times", 10))
        self.register.pack(pady=(0, 10), ipadx=30, ipady=4)

    def upload_file(self):
        filename = filedialog.askopenfilename(initialdir="/images", title="Somrhting")
        self.filename.configure(text=filename)

    def reg_submit(self):
        name = self.name.get()
        email = self.email.get()
        password = self.password.get()
        college=self.college.get()
        dob=self.dob.get()
        filename=self.filename['text'].split('/')[-1]

        response = self.db.insert_user(name,email,password,college,dob,filename)

        if response==1:

            shutil.copyfile(self.filename['text'],"C:\\Users\\SHIBAM\\PycharmProject\\quizapp\\images\\"+filename)
            messagebox.showinfo("Registration successful","You may login proceed!")
        else:
            messagebox.showerror("Database Error"," Fill the ragistration form properly")






    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
        for i in self.root.place_slaves():
            i.destroy()

    def q_clear(self):
        for i in self.freame2.pack_slaves():
            i.destroy()
        for i in self.frame3.pack_slaves():
            i.destroy()


obj=quizapp()
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from DBhelper import *
from tkinter import filedialog
import os,shutil



class Login:

	def __init__(self):
		self.db = DBhelper()
		self.root = Tk()

		self.root.title("my log in page")

		self.root.configure(background="#FE5667")

		self.root.minsize(300, 500)
		self.root.maxsize(300, 500)

		self.Load_gui()
	#clear root pack function
	def clear(self):
	 	for i in self.root.pack_slaves():
	 		i.destroy()
	#clear navbar manu
	def remove_nav(self):
		# emptyMenu = Menu(self.root)       #this is navbar clean method
		# self.root.config(menu=emptyMenu)
		self.root.config(menu=self.root)
	 #front page of gui
	def Load_gui(self):

		#clear screen
		self.clear()
		self.remove_nav()

		self.label1 = Label(self.root, text="tinder", fg="white", bg="#FE5667")
		self.label1.configure(font=("times", 30, "bold"))
		self.label1.pack(pady=(30, 50))

		self.label2 = Label(self.root, text="email", fg="white", bg="#FE5667")
		self.label2.configure(font=("", 15, ""))
		self.label2.pack(pady=(0, 0))

		self.email = Entry(self.root)
		self.email.pack(pady=(0, 0), ipadx=25, ipady=2)

		self.lable3 = Label(self.root, text="password", fg="white", bg="#FE5667")
		self.lable3.configure(font=("", 15, ""))
		self.lable3.pack(pady=(20, 0))

		self.password = Entry(self.root)
		self.password.pack(pady=(0, 0), ipadx=25, ipady=2)

		# self.button1=Button(self.root, text="login",fg="#FE5667") #this method also work
		# self.button1.pack(pady=(40,0),ipadx=40,ipady=5)

		self.button1 = Button(self.root, text="login", height=2, width=15, fg="#FE5667",command=lambda: self.button_click())
		self.button1.pack(pady=(50, 0))

		self.lable4 = Label(self.root, text="not a member?", fg="#A5B1F8", bg="#FE5667")
		self.lable4.configure(font=("", 10, "italic"))
		self.lable4.pack(pady=(10, 0))

		self.button2 = Button(self.root, text="sign up", height=2, width=15, fg="#FE5667",command=lambda: self.register_gui())
		self.button2.pack(pady=(0, 0))

		self.root.mainloop()


	#registration page of gui, if registrainon_button click from main gui

	def register_gui(self):

		#clean screen
		self.clear()

		self.label1=Label(self.root, text="tinder",fg="white",bg="#FE5667")
		self.label1.configure(font=("times",30,"bold"))
		self.label1.pack(pady=(30,10))

		self.label2=Label(self.root, text="name",fg="white",bg="#FE5667")
		self.label2.configure(font=("",15,""))
		self.label2.pack(pady=(0,0))

		self.name=Entry(self.root)
		self.name.pack(pady=(0,0),ipadx=25,ipady=2)

		self.lable3=Label(self.root, text="email", fg="white", bg="#FE5667")
		self.lable3.configure(font=("",15,""))
		self.lable3.pack(pady=(10,0))

		self.email = Entry(self.root)
		self.email.pack(pady=(0,0),ipadx=25,ipady=2)

		self.lable4 = Label(self.root, text="password", fg="white", bg="#FE5667")
		self.lable4.configure(font=("", 15, ""))
		self.lable4.pack(pady=(10, 0))

		self.password = Entry(self.root)
		self.password.pack(pady=(0, 0), ipadx=25, ipady=2)

		# self.button1=Button(self.root, text="login",fg="#FE5667") #this method also work
		# self.button1.pack(pady=(40,0),ipadx=40,ipady=5)

		self.lable5 = Label(self.root, text="age"+"18+", fg="white", bg="#FE5667")
		self.lable5.configure(font=("", 15, ""))
		self.lable5.pack(pady=(10, 0))

		self.age = Entry(self.root)
		self.age.pack(pady=(0, 0), ipadx=25, ipady=2)

		self.button1=Button(self.root,text="register", height=2, width=15, fg="#FE5667", command=lambda :self.reg_submit())
		self.button1.pack(pady=(20,10))

		# self.lable4=Label(self.root, text="not a member?", fg="#A5B1F8", bg="#FE5667")
		# self.lable4.configure(font=("",10,"italic"))
		# self.lable4.pack(pady=(10,0))

		self.button2=Button(self.root,text="log in", height=2, width=15, fg="#FE5667",command=lambda :self.Load_gui())
		self.button2.pack(pady=(0,0))

	#log in button click
	def button_click(self):


		email=self.email.get()
		password=self.password.get()
		if len(email)!=0 and len(password)!=0:
			login_data=self.db.check_login(email,password)
			if len(login_data)>0:
				self.user_id=login_data[0][0]
				self.user_data=login_data[0]
				self.load_user_info()
			else:
				messagebox.showerror("Error", "bad credential")
		else:
			messagebox.showerror("Error", "fill email and password")


	#register function from registration page for register button
	def reg_submit(self):
		name=self.name.get()
		email=self.email.get()
		password=self.password.get()
		age=self.age.get()
		if len(name)!=0 and len(email)!=0 and len(password)!=0 and len(age)!=0:
			response=self.db.insert_user(name,email,password,age)

			if response==1:
				messagebox.showinfo("register", "successful")
				self.clear()
				self.Load_gui()
			elif response==2:
				messagebox.showerror("Error", "try after 18")
			else:
				messagebox.showerror("Error", "fill age properly")
		else:
			messagebox.showerror("error", "fill all box")

	def load_user_info(self):
		self.main_window(self.user_data)

	#navbar code

	def navbar(self):
		menu = Menu(self.root)
		self.root.config(menu=menu)
		filemenu = Menu(menu)
		menu.add_cascade(label="Home", menu=filemenu)
		filemenu.add_command(label="My Profile", command = lambda : self.main_window(self.user_data))
		filemenu.add_command(label="Edit Profile", command= lambda : self.edit_profile())
		filemenu.add_command(label="View Profile", command = lambda : self.other_profile())
		filemenu.add_command(label="LogOut", command= lambda : self.logout() )

		helpmenu = Menu(menu)
		menu.add_cascade(label="Proposals", menu=helpmenu)
		helpmenu.add_command(label="My Proposals")
		helpmenu.add_command(label="My Requests")
		helpmenu.add_command(label="My Matches")




	#login page
	def main_window(self,data,mode=1,index= None, num=None):
		self.clear()
		self.navbar()
		# print("main", index)
		
		if len(data[8])!=0:
			imageUrl = "images/{}".format(data[8])

			load = Image.open(imageUrl)
			load = load.resize((200, 200), Image.ANTIALIAS)
			render = ImageTk.PhotoImage(load)

			img = Label(image=render)
			img.image = render
			img.pack(pady=(10,0))

		if len(data[1])!=0:
			lable1=Label(self.root, text='Name: ' + data[1], fg="white", bg="#FE5667")
			lable1.pack(pady=(20,10))

		if len(data[2]) != 0:
			lable2 = Label(self.root, text='email: ' + data[2], fg="white", bg="#FE5667")
			lable2.pack(pady=(10, 10))

		if len(data[4]) != 0:
			lable3 = Label(self.root, text='bio: ' + data[4], fg="white", bg="#FE5667")
			lable3.pack(pady=(10, 10))

		if data[5]!=0:
			lable3 = Label(self.root, text= data[5], fg="white", bg="#FE5667")
			lable3.pack(pady=(10, 10))

		if len(data[6]) != 0:
			lable3 = Label(self.root, text='gender: ' + data[6], fg="white", bg="#FE5667")
			lable3.pack(pady=(10, 10))


		if len(data[7]) != 0:
			lable4 = Label(self.root, text='city: ' + data[7], fg="white", bg="#FE5667")
			lable4.pack(pady=(10, 10))


		if mode!=1:

			#button gui in view profile page
			frame=Frame(self.root)
			frame.configure(bg="#FE5667")
			frame.pack(pady=(10, 0))
			if index !=0:
				Button(frame, text="previous", fg="#FE5667", height="2", width="8", command=lambda: self.other_profile(index-1)).pack(side='left')
			Button(frame, text="propose", fg="#FE5667", height="2", width="8", command=lambda: self.propose(self.user_id)).pack(side='left')
			if index !=(num-1):
				Button(frame, text='right', fg="#FE5667", height="2", width="8", command=lambda: self.other_profile(index+1)).pack(side='left')

	def propose(self, romeo_id, juliet_id):

		response = self.db.propose(romeo_id, juliet_id)
		if response == 1:
			pass

	#show other profile function
	# def other_profile(self, index=0):
	#
	# 	data=self.db.fetch_profile(self.user_id)
	# 	# print(data)
	# 	# if index==len(data)-1:
	# 	# 	self.main_window(data[index],mode=2, index=0)
	# 	# else:
	# 	# 	print("index", index)
	# 	# 	self.main_window(data[index], mode=2, index=index)
	# 	if len(data)<index:
	# 	# print("index", index)
	# 	# self.main_window(data[index], mode=2, index=index)
	# 	# print(data[index])
	#
	# 	# print("len",len(data))
	# #edit profile gui

	# show other profile function

	def other_profile(self, index=0):

		#fatch data
		data = self.db.fetch_profile(self.user_id)
		num=len(data)
		self.main_window(data[index], mode=2, index=index, num=num)










	def edit_profile(self):

		self.clear()

		self.label0= Label(self.root, text="Edit Profile", fg="white", bg="#FE5667")
		self.label0.configure(font=("Times", 25, "bold"))
		self.label0.pack(pady=(20, 10))

		self.label1 = Label(self.root, text="Bio:", fg="white", bg="#FE5667")
		self.label1.configure(font=("Times", 15, "italic"))
		self.label1.pack(pady=(5, 5))

		self.bio = Entry(self.root)
		self.bio.pack(pady=(0, 10), ipadx=25,ipady=2)

		self.label2 = Label(self.root, text="Age:", fg="white", bg="#FE5667")
		self.label2.configure(font=("Times", 15, "italic"))
		self.label2.pack(pady=(5, 5))

		self.age = Entry(self.root)
		self.age.pack(pady=(0, 10), ipadx=25,ipady=2)

		self.label3 = Label(self.root, text="Gender:", fg="white", bg="#FE5667")
		self.label3.configure(font=("Times", 15, "italic"))
		self.label3.pack(pady=(5, 5))

		self.gender = Entry(self.root)
		self.gender.pack(pady=(0, 10), ipadx=25,ipady=2)

		self.label4 = Label(self.root, text="City:", fg="white", bg="#FE5667")
		self.label4.configure(font=("Times", 10, "italic"))
		self.label4.pack(pady=(5, 5))

		self.city = Entry(self.root)
		self.city.pack(pady=(0, 10), ipadx=25,ipady=2)

		Label(self.root,text="upload picture",fg="white", bg="#FE5667").pack(pady=(0,0))
		Button(self.root,text="upload",command= lambda: self.upload()).pack(pady=(0,0))
		self.file=Label(self.root,fg="white", bg="#FE5667")
		self.file.pack()



		self.edit = Button(self.root, height=2, width=15, text="Edit Profile", bg="white",fg="#FE5667" , command=lambda: self.update_profile())
		self.edit.pack(pady=(15, 0))

	def upload(self):
		filename=filedialog.askopenfilename(initialdir="/images", title="Somrhting")
		self.file.configure(text=filename)

	#update_profile
	def update_profile(self):
		bio = self.bio.get()
		age = self.age.get()
		gender = self.gender.get()
		city = self.city.get()
		dp= self.file['text'].split('/')[-1]


		if len(age)!=0:
			info = [bio, age, gender, city, dp]

			response = self.db.update_profile(self.user_id, info)

			if response == 1:
				messagebox.showinfo("Success", "Profile Updated")
				self.submit_reg()
			else:
				messagebox.showerror("Error", "Some error occured")
		else:
			messagebox.showerror("error","age must be filled")
	#after submit update profile this function halpe to update main window
	def submit_reg(self):
		#print(self.user_id)
		data=self.db.submit_reg_check(self.user_id)
		self.user_data= data
		self.main_window(data)

	#logout function
	def logout(self):
		self.user_id = ''
		self.user_data = ''

		self.Load_gui()









	# def navbar(self):
	#     menu = Menu(self.root)
	#     self.root.config(menu=menu)
	#     filemenu = Menu(menu)
	#     menu.add_cascade(label="Home", menu=filemenu)
	#     filemenu.add_command(label="My Profile")
	#     filemenu.add_command(label="Edit Profile")
	#     filemenu.add_command(label="View Profile")
	#     filemenu.add_command(label="LogOut")
	#
	#     helpmenu = Menu(menu)
	#     menu.add_cascade(label="Proposals", menu= helpmenu)
	#     helpmenu.add_command(label="My Proposals")
	#     helpmenu.add_command(label="My Requests")
	#     helpmenu.add_command(label="My Matches")

obj=Login()
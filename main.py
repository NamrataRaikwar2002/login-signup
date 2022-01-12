import json
import os
# if os.path.exists("userdetail.json"):
# 	pass
# else:
# 	file=open("userdetail.json","w")
# 	file.close()
print("do you want to login or signup\n 1.signup \n 2.login")
user={}
data=[]
user_data={}
profile={}
def signfun(): 
	global username
	username=input("Enter username:")
	global password1
	password1=input("Enter your password:")
	special_char="@#$%^&*"
	up=0
	lw=0
	di=0
	sc=0
	for i in password1:
		if i.isdigit():
			di+=1
		if i.isupper():
			up+=1
		if i.islower():
			lw+=1
		if i in special_char:
			sc+=1
	if up>=1 and lw>=1 and di>=1 and sc>=1 and up+lw+di>=4:
		print("strong password")
		confirm()
	else:
		print("Please enter password with all required\n1. enter any digit\n2. uppercase letter needed\n3. lowercase letter\n4. Enter any special character")
		signfun()
def confirm():
	data=[]
	global confirm_pswd
	confirm_pswd=input("Confirm password:")
	if password1==confirm_pswd:
		if os.path.exists("userdetail.json"):
			sfile=open("userdetail.json","r")
			sfile1=json.load(sfile)
			# print(sfile1,type(sfile1))
			for l in range(len(sfile1["user"])):
				signed_username=sfile1["user"][l]["username"]
			# print(signed_username)
				if signed_username == username:
					print("username already exist")
					break
			else:
				more_detail()
		else:
			more_detail()
	else:
		print("both the password are not same")
		confirm()
def more_detail():
	detail_list=[]
	print(username,"You are signed up succesfully")
	description=input("Bio:")
	dob=input("enter date of birth:")
	hobby=input("hobbies:")
	gender=input("Enter gender:")
	user_data["username"]=username
	user_data["password"]=confirm_pswd
	profile["description"]=description
	profile["dob"]=dob
	profile["hobbies"]=hobby
	profile["gender"]=gender
	user_data["profile"]=profile
	data.append(user_data)
	user["user"]=data
	if os.path.exists("userdetail.json"):
		rfile=open("userdetail.json")
		file1=json.load(rfile)
		detail_list=file1["user"]
		detail_list.append(user_data)
		print(detail_list)
		user["user"]=detail_list
		with open("userdetail.json","w") as update_detail:
			json.dump(user,update_detail,indent=4)
				
	else:
		with open("userdetail.json","w") as wfile:
			json.dump(user,wfile,indent=4)
		
	
def login():
	username=input("enter username:")
	logpassword=input("enter password:")
	if os.path.exists("userdetail.json"):
		file=open("userdetail.json")
		file1=json.load(file)
		for l in range(len(file1["user"])):
			loggged_username=file1["user"][l]["username"]
			if loggged_username == username:
					print(username,"you are logged in successfully")
					break
		else:
			print("invalid username or password")
	else:
         print("sign in first")

def choice():
	actinput=input("enter your choice:")
	if actinput=="1":
		return signfun()
	elif actinput=="2":
		return login()
	else:
		print("invalid entry")
		choice()
choice()





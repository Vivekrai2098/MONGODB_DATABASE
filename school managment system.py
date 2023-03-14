# PYTHON,TKINTER,OOP,,MONGODB,SMS_API,
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import pymongo
import os
# this is the class
class work:
    def __init__(self):
        self.user=""
        self.password=""
        self.name=""
        self.contact_number=""
        self.email_address=""
        self.gender=""
        self.data_of_birth=""
        self.stream=""
        self.delname=""
        self.delemail=""
        self.askname=""
        self.askeemail=""
        #data base connection
        self.myclient=pymongo.MongoClient("mongodb://localhost:27017")
        self.datbase=self.myclient["school_managment"]
        self.collections=self.datbase["school"]


    #check update
    def check_update(self):
        a=u_name.get()
        b=u_email.get()
        self.askname=a
        self.askeemail=b

        # fill or not
        if (len(self.askname) == 0 and len(self.askeemail) == 0):
            messagebox.showwarning(title="war", message="must fill all recored")
        elif (len(self.askname) == 0 or len(self.askeemail) == 0):
            messagebox.showwarning(title="war", message="fill all the field")
        else:
            v = self.collections.find_one({'$and': [{"name": a}, {"email": b}]})
            if (bool(v) == True):
                messagebox.showinfo(title="find", message="your data succefully find process next step")
                self.update()
            else:
                messagebox.showwarning(title="not find", message="your data is not in database")

    #ask update
    def ask_update(self):
        global screen3
        screen3 = Toplevel(screen)
        screen3.title("which filed you want update")
        screen3.geometry("300x300")
        screen3.configure(background="light blue")
        screen3.resizable(False, False)
        lbl = Label(screen3, text="fill the field", bg='red', fg="white",
                    font=("Cursive", 20, "bold"))
        lbl.pack()

        name_lbl = Label(screen3, text="enter name", bg="yellow", fg="black",
                         font=("Cursive", 12, "bold"))
        name_lbl.place(x=0, y=20)

        global u_name
        u_name = StringVar()
        u_name = Entry(screen3, width=35, bg='white', fg="black", bd=3, textvariable=u_name)
        u_name.place(x=0, y=40)

        email_lbl = Label(screen3, text="enter email", bg="yellow", fg="black",
                          font=("Cursive", 12, "bold"))
        email_lbl.place(x=0, y=80)

        global u_email

        u_email = StringVar()
        u_email = Entry(screen3, width=35, bg='white', fg="black", bd=3, textvariable=u_email)
        u_email.place(x=0, y=100)

        # this is the button
        ex = Button(screen3, text="search you data", fg="white", bg="red", command=self.check_update)
        ex.place(x=70, y=140)





    # update
    # complete update
    def update_complete(self):
        c_name=name4.get()
        c_contact=contact4.get()
        c_mail=email4.get()
        c_stream=stream4.get()
        c_gender=gender4.get()
        c_birth=birth4.get()
        if (len(c_name) == 0 and len(c_contact) == 0 and len(c_mail) and len(c_stream) and len(c_gender)and len(c_birth)):
            messagebox.showwarning(title="war", message="must fill all recored")
        elif (len(c_name) == 0 or len(c_contact) == 0 or len(c_mail)== 0 or len(c_stream)== 0 or len(c_gender)== 0 or len(c_birth)== 0):
             messagebox.showwarning(title="war", message="fill all the field")
        else:
            newvalue={"$set":{"name":c_name,"contact":c_contact,"email":c_mail,"gender":c_gender,"date_of_birth":c_birth,"stream":c_stream}}
            self.collections.update_one({'$and': [{"name": self.askname}, {"email": self.askeemail}]},newvalue)
            screen3.destroy()
            screen2.destroy()
            messagebox.showinfo(title="complete",message="succefully update your profile")





    def update(self):
        global screen2
        screen2 = Toplevel(screen)
        screen2.title("update record")
        screen2.geometry("1270x380")
        screen2.configure(background="light blue")
        screen2.resizable(False, False)
        #this is the input and button



        one = Frame(screen2, bg="#f1d488", borderwidth=6)
        # one.pack(side=TOP,fill="x")
        one.place(x=0, y=0, width=1300, height=350)

        # this is label inside frame
        lbl = Label(one, text="UPDATE Panel", bg='#f1d488', fg="white",
                    font=("Cursive", 40, "bold"))
        lbl.place(x=10, y=8)

        # --------------------------this is add input
        # name
        name = Label(one, text="Name", bg="#f1d488", fg="black")
        name.place(x=30, y=80)
        # input
        global name4
        name4 = StringVar()
        name4 = Entry(one, width=35, bg='white', fg="black", bd=3, textvariable=name4)
        name4.place(x=90, y=72)

        # contact number

        contact = Label(one, text="contact", bg="#f1d488", fg="black")
        contact.place(x=30, y=160)
        # input contact number
        global contact4
        contact4 = StringVar()
        contact4 = Entry(one, width=35, bg='white', fg="black", bd=3, textvariable=contact4)
        contact4.place(x=90, y=160)

        # email address
        email = Label(one, text="email", bg="#f1d488", fg="black")
        email.place(x=400, y=160)

        # input email address =
        global email4
        email4 = StringVar()
        email4 = Entry(one, width=35, bg='white', fg="black", bd=3, textvariable=email4)
        email4.place(x=460, y=160)
        # stream ..................
        stream = Label(one, text="stream", bg="#f1d488", fg="black")
        stream.place(x=30 + 370, y=80)
        # stream
        global stream4
        stream4 = StringVar()
        stream4 = Entry(one, width=35, bg='white', fg="black", bd=3, textvariable=stream4)
        stream4.place(x=90 + 370, y=72)
        #button
        ex = Button(screen2, text="Update your information", fg="white", bg="green", command=self.update_complete)
        ex.place(x=140, y=290)



        # stream ..................

        # gender

        gender = Label(one, text="gender", bg="#f1d488", fg="black")
        gender.place(x=30 + 370 + 370, y=80)
        # stream
        global gender4
        gender4 = StringVar()
        opt = ["Male", "Female", "Other"]
        gender4 = StringVar()
        gender4 = ttk.Combobox(one, values=opt, width=10, textvariable=gender4)
        gender4.place(x=90 + 370 + 370, y=72)

        # gender
        # data_of birth
        birth = Label(one, text="birth", bg="#f1d488", fg="black")
        birth.place(x=400 + 370, y=160)

        # birth birth birth
        global birth4
        birth4 = StringVar()
        birth4 = DateEntry(one, selectmode='day', textvariable=birth4)
        birth4.place(x=460 + 370, y=160)






        #.................................







    def delete1(self):
        self.delname = del_name.get()
        self.delemail = del_email.get()
        if(len(self.delname)==0 and len(self.delemail)==0):
            messagebox.showwarning(title="war",message="must fill all recored")
        elif(len(self.delname)==0 or len(self.delemail)==0):
            messagebox.showwarning(title="war", message="fill all the field")
        else:
            re = self.collections.find()
            t = 0
            for r in re:
                t = t + 1
            if (t == 0):
                messagebox.showwarning(title="not", message="not enough data in database")
                screen1.destroy()
            else:
                result = self.collections.delete_one({"name": self.delname} and {"email": self.delemail})
                screen.destroy()
                messagebox.showinfo(title="complete",message="delete succefully")
                self.next_screen()
                print(bool(result))


    def delete_record(self):
        global screen1
        screen1 = Toplevel(screen)
        screen1.title("delete record")
        screen1.geometry("300x300")
        screen1.configure(background="light blue")
        screen1.resizable(False, False)
        lbl = Label(screen1, text="fill the field", bg='red', fg="white",
                    font=("Cursive", 20, "bold"))
        lbl.pack()

        name_lbl = Label(screen1, text="enter name",bg="yellow",fg="black",
                    font=("Cursive", 12, "bold"))
        name_lbl.place(x=0,y=20)

        global del_name
        del_name = StringVar()
        del_name = Entry(screen1, width=35, bg='white', fg="black", bd=3, textvariable=del_name)
        del_name.place(x=0,y=40)

        email_lbl = Label(screen1, text="enter email",bg="yellow", fg="black",
                         font=("Cursive", 12, "bold"))
        email_lbl.place(x=0,y=80)

        global del_email

        del_email = StringVar()
        del_email = Entry(screen1, width=35, bg='white', fg="black", bd=3, textvariable=del_email)
        del_email.place(x=0,y=100)



        # this is the button
        ex = Button(screen1, text="delete record", fg="white", bg="red",command=self.delete1)
        ex.place(x=70, y=140)






    #insert data in database mongodb
    def collect(self):
        self.name=name1.get()
        self.contact_number=contact1.get()
        self.email_address=email1.get()
        self.gender=gender1.get()
        self.data_of_birth=birth1.get()
        self.stream=stream1.get()
        a=self.name
        b=self.contact_number
        c=self.email_address
        d=self.gender
        e=self.data_of_birth
        f=self.stream
        if(len(a)<=0 and len(b)<=0 and len(c)<=0 and len(d)<=0 and len(e)<=0 and len(f)<=0):
            messagebox.showwarning(title="blank",message="cant be blank")
        elif(len(a)<=0 or len(b)<=0 or len(c)<=0 or len(d)<=0 or len(e)<=0 or len(f)<=0):
            messagebox.showwarning(title="blank",message="fill all field")
        else:
            print("the name is", self.name, "\ncontact", self.contact_number, "\nemail", self.email_address, "\ngender",
                  self.gender, "\nbirth", self.data_of_birth, "\nstream", self.stream)
            data = {"name": a, "contact": b, "email": c, "gender": d, "date_of_birth": e, "stream": f}
            desci = self.collections.insert_one(data)
            if (bool(desci) == True):
                contact1.delete(0, END)
                name1.delete(0, END)
                email1.delete(0, END)
                stream1.delete(0, END)
                gender1.delete(0, END)
                birth1.delete(0, END)
                messagebox.showinfo(title="complete", message="succefully Insert data in database")
            else:
                messagebox.showwarning(title="something_wrong", message="something is wrong")
    #...........................................................................................
    def finalsms(self):
        ph=phone.get()
        if(len(phone.get())==10):
            from twilio.rest import Client
            account_sid = ""
            auth_token = password_api
            client = Client(account_sid, auth_token)
            t = self.collections.find({}, {"_id": 0})
            data=[]
            for i in t:
                data.append(i)
            message = client.messages.create(
                body=str(data),
                from_="",
                to="+91"+ph
            )
            messagebox.showinfo("sms","SMS send Succefully")
            print(message.sid)


        else:
            messagebox.showwarning(title="wrong",message="wrong number")

    def smsapi(self):
        global screen10
        screen10 = Toplevel(screen)
        screen10.title("Phone number")
        screen10.geometry("300x300")
        screen10.configure(background="light blue")
        screen10.resizable(False, False)
        smsap=Label(screen10, text="fill the Phone number", bg='pink', fg="black",
                    font=("Cursive", 20, "bold"))
        global phone
        smsap.pack()
        phone=StringVar()
        phone_number = Entry(screen10, width=35, bg='white', fg="black", bd=3, textvariable=phone)
        phone_number.pack()

        exs = Button(screen10, text="SEND", fg="white", bg="green", command=self.finalsms)
        exs.pack()








    # ...........................................................................................



    #this is the new screen
    def next_screen(self):
        global screen
        screen=Toplevel(win)
        screen.title("main page")
        # screen.maxsize(width=900, height=300)
        # screen.minsize(width=600, height=600)
        screen.geometry("1300x700")
        screen.configure(background="light blue")
        screen.resizable(False, False)
        #first frame
        one=Frame(screen,bg="#be2ed6",borderwidth=6)
        # one.pack(side=TOP,fill="x")
        one.place(x=0,y=0,width=1300,height=350)


        # sms button
        sms = Button(one, text="SEND SMS", fg="Green", bg="light blue", command=self.smsapi)
        sms.place(x=80, y=200)


        #this is label inside frame
        lbl = Label(one, text="Control Panel", bg='#be2ed6', fg="white",
                    font=("Cursive", 40, "bold"))
        lbl.place(x=10,y=8)
        #button exit.................................
        ex=Button(one,text="EXIT",fg="white",bg="red",command=first.close)
        ex.place(x=1200,y=0)


        # --------------------------this is add input
        #name
        name=Label(one,text="Name",bg="#be2ed6",fg="black")
        name.place(x=30,y=80)
        #input
        global name1
        name1 = StringVar()
        name1= Entry(one, width=35, bg='white', fg="black", bd=3, textvariable=name1)
        name1.place(x=90, y=72)




        #contact number

        contact = Label(one, text="contact", bg="#be2ed6", fg="black")
        contact.place(x=30, y=160)
        #input contact number
        global contact1
        contact1 = StringVar()
        contact1 = Entry(one, width=35, bg='white', fg="black", bd=3, textvariable=contact1)
        contact1.place(x=90, y=160)

        # email address
        email = Label(one, text="email", bg="#be2ed6", fg="black")
        email.place(x=400, y=160)

        # input email address =
        global email1
        email1 = StringVar()
        email1 = Entry(one, width=35, bg='white', fg="black", bd=3, textvariable=email1)
        email1.place(x=460, y=160)
        #stream ..................
        stream = Label(one, text="stream", bg="#be2ed6", fg="black")
        stream.place(x=30+370, y=80)
        #stream
        global stream1
        stream1 = StringVar()
        stream1 = Entry(one, width=35, bg='white', fg="black", bd=3, textvariable=stream1)
        stream1.place(x=90+370, y=72)

        # stream ..................

        #gender

        gender = Label(one, text="gender", bg="#be2ed6", fg="black")
        gender.place(x=30 + 370+370, y=80)
        # stream
        global gender1
        gender1 = StringVar()
        opt=["Male","Female","Other"]
        gender1 = StringVar()
        gender1 = ttk.Combobox(one,values=opt,width=10,textvariable=gender1)
        gender1.place(x=90 + 370+370, y=72)

        #gender
        #data_of birth
        birth = Label(one, text="birth", bg="#be2ed6", fg="black")
        birth.place(x=400+370, y=160)

        # birth birth birth
        global birth1
        birth1 = StringVar()
        birth1 = DateEntry(one,selectmode='day',textvariable=birth1)
        birth1.place(x=460+370, y=160)




        # data_of birth




        # --------------------------this is add input

        # middle frame
        mid=Frame(screen,bg="#da8ee7")
        mid.place(x=160,y=300,width=1000,height=80)

        # add recored button..
        add_record=Button(mid,text="Add Record",bg="#FFFFFF",borderwidth=2,fg="black",border=3,command=first.collect)
        add_record.place(x=100,y=8)
        #delete record button
        del_record = Button(mid, text="Delete Record", bg="#FFFFFF", borderwidth=2, fg="black", border=3,command=first.delete_record)
        del_record.place(x=330, y=8)
        #view record
        v_record = Button(mid, text="View Record", bg="#FFFFFF", borderwidth=2, fg="black", border=3,command=first.show_data)
        v_record.place(x=560, y=8)
        #update record
        u_record = Button(mid, text="update Record", bg="#FFFFFF", borderwidth=2, fg="black", border=3,command=first.ask_update)
        u_record.place(x=465+300, y=8)




        #second frame
        global two
        two = Frame(screen, bg="#FFFFFF", borderwidth=6)
        # two.pack(side=BOTTOM,fill="x")

        #this is the second frame scroll
        # scroll_y=Scrollbar(two,orient=VERTICAL)
        # scroll_y.grid(side=RIGHT,fill=Y)


        two.place(x=0, y=350, width=1300, height=350)
        #first
        p1=Label(two,text="Name",width=30)
        p1.grid(row=1,column=0,padx=3)
        #second
        p2 = Label(two, text="Contact",width=25)
        p2.grid(row=1, column=1,padx=3)
        #thired
        p3 = Label(two, text="Email",width=25)
        p3.grid(row=1, column=2,padx=3)
        #fourth
        p4 = Label(two, text="Gender",width=25)
        p4.grid(row=1, column=3,padx=3)
        # fifth
        p5 = Label(two, text="Birth",width=25)
        p5.grid(row=1, column=4,padx=3)
        #sixth
        p6 = Label(two, text="Stream",width=25)
        p6.grid(row=1, column=5,padx=3)

    # show database in mongobd to tikinter ui

    def show_data(self):
        # new collection retrive
        num = 2
        a=2
        b=2
        c=2
        d=2
        e=2

        # data check
        re = self.collections.find()
        t = 0
        for r in re:
            t = t + 1
        if (t == 0):
            messagebox.showwarning(title="not", message="not enough data in database")
        else:
            for i in self.collections.find({}, {"name": 1, "_id": 0}):
                # print(*i.values(), sep=" ,")
                p1 = Label(two, text=str(",".join((i.values()))), width=30)
                p1.grid(row=num, column=0, padx=3)
                num = num + 1

            for j in self.collections.find({}, {"contact": 1, "_id": 0}):
                p2 = Label(two, text=str(",".join((j.values()))), width=25)
                p2.grid(row=a, column=1, padx=3)
                a = a + 1

            for k in self.collections.find({}, {"email": 1, "_id": 0}):
                p3 = Label(two, text=str(",".join((k.values()))), width=25)
                p3.grid(row=b, column=2, padx=3)
                b = b + 1

            for l in self.collections.find({}, {"gender": 1, "_id": 0}):
                p4 = Label(two, text=str(",".join((l.values()))), width=25)
                p4.grid(row=c, column=3, padx=3)
                c = c + 1
            #
            for m in self.collections.find({}, {"date_of_birth": 1, "_id": 0}):
                p5 = Label(two, text=str(",".join((m.values()))), width=25)
                p5.grid(row=d, column=4, padx=3)
                d = d + 1

            for o in self.collections.find({}, {"stream": 1, "_id": 0}):
                p6 = Label(two, text=str(",".join((o.values()))), width=25)
                p6.grid(row=e, column=5, padx=3)
                e = e + 1

                # name_one = Label(two, )

    #that is user data get
    def userget(self):
        x=user.get()
        y=password.get()
        self.user=x
        self.password=y
        if(len(x)<=0 and len(y)<=0):
            messagebox.showwarning(title="field required",message="fill all the field")
            print("fild required")
        elif(len(x)>0 and len(y)<=0):
            messagebox.showwarning(title="password", message="Not Empty The Password")
            print("not empty the password")

        elif(len(x)<=0 and len(y)>0):
            messagebox.showwarning(title="username", message="Not Empty The username")
            print("not empty username")
        else:
            if(self.user=="admin" and self.password=="100"):
                messagebox.showinfo(title="username", message="you have succefully Login")
                first.next_screen()

            else:
                messagebox.showwarning(title="username", message="username password wrong")
    def close(self):
        v=messagebox.askyesno(title="thanks",message="Are you sure to exit")
        if(bool(v)==True):
            win.destroy()
        else:
            print("ok")








    def placeholder(self,event):
        ent.config(state=NORMAL)
        ent.delete(0, END)

    def placeholder1(self,event):
        ent1.config(state=NORMAL)
        ent1.delete(0,END)





first=work()
win=Tk()
win.title("School Managment System")
win.maxsize(width=900,height=300)
win.minsize(width=600,height=600)


lbl=Label(win,text="\n \nThe School Managemnet System",bg='#e5de00',fg="red",width=100,font=("",13,"bold"))
lbl.pack(pady=1)
win.configure(background="light blue")
win.resizable(False,False)

#this is the label
lbl=Label(win,text="\n \nADMIN LOGIN \nPAGE",bg='light blue',fg="black",font=("Times",30,"bold"),)
lbl.place(x=90,y=100)
lbl=Label(win,text="\nThe first mongodb base data base using with python.The first mongodb base data base using with\n python.The first mongodb base data base using\n with python",bg='light blue',fg="black",font=("",6,),)
lbl.place(x=40,y=300)


# first input
user=StringVar()
ent=Entry(win,width=35,bg='light grey',fg="purple",bd=3,textvariable=user)
ent.place(x=460,y=200)
ent.insert(0,"enter email here.....")
ent.config(state=DISABLED)
ent.bind('<Button-1>',first.placeholder)

# second input
password=StringVar()
ent1=Entry(win,width=35,bg='light grey',fg="purple",bd=3,textvariable=password)
ent1.place(x=460,y=265)
ent1.insert(0,"enter password  here.....",)
ent1.config(state=DISABLED)
ent1.bind('<Button-1>',first.placeholder1)

# there is first button
login=Button(win,text="LOGIN",fg="black",bg="yellow",command=first.userget,font=("",9,"bold"))
login.place(x=600,y=320)
# there is second  button
login=Button(win,text="EXIT",fg="black",bg="yellow",font=("",9,"bold"),command=first.close)
login.place(x=470,y=320)



win.mainloop()








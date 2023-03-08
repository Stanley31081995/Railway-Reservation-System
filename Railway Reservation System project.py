import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import time
import datetime
from tkcalendar import Calendar
import pymysql

root=tk.Tk()

class Train:
    def __init__(self,root):
        self.root=root
        self.Login_page()
    def Login_page(self):
        self.login_frame2=Frame(self.root,bg='skyblue')
        self.login_frame2.place(x=0,y=0,width=1700,height=1000)
        self.login_frame=Frame(self.root,bg='skyblue')
        self.login_frame.place(x=500,y=100,width=400,height=1000)
        login_label=Label(self.login_frame,text='LOGIN',bg='white',fg='blue')
        login_label.place(x=110,y=10)
        username_label=Label(self.login_frame,text='Username')
        username_label.place(x=20,y=30)
        self.username=Entry(self.login_frame,width=40)
        self.username.place(x=85,y=30)
        password_label=Label(self.login_frame,text='Password')
        password_label.place(x=20,y=60)
        self.password=Entry(self.login_frame,width=40)
        self.password.place(x=85,y=60)
        ##
        self.otp_frame=Frame(self.login_frame,bg='skyblue',width=1000,height=200)
        self.otp_frame.place(x=20,y=100)
        self.otp_img=ImageTk.PhotoImage(Image.open('otp_image.jpg'))
        self.label_=Label(self.otp_frame,image=self.otp_img)
        self.label_.pack()
        import string
        import random
        self.res=''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase,k=4))
        otp_message_label=Label(self.login_frame,text='Type in the box below:'+str(self.res))
        otp_message_label.place(x=80,y=370)
        self.otp_message_entry=Entry(self.login_frame)
        self.otp_message_entry.place(x=80,y=400)
        #self.otp_message_entry.insert(END,'Type here ...')
        sign_in_button=Button(self.login_frame,bg='green',fg='white',text='Sign in',width=40,command=self.sign_in)
        sign_in_button.place(x=50,y=450)
        register_button=Button(self.login_frame,bg='blue',fg='white',text='Register',width=30,command=self.Register)
        register_button.place(x=50,y=480)
    def sign_in(self):
        if (self.username.get()=='') or (self.password.get()=='') or (self.otp_message_entry.get()==''):
            messagebox.showerror('error','All fields must be filled')
        elif (self.res!=self.otp_message_entry.get()):
            messagebox.showerror('error','Please enter the valid captcha')
        else:    
           con=pymysql.connect(host='localhost',user='root',password='',database='arunachalam')
           cur=con.cursor()
           cur.execute('select * from login_details')
           self.row=cur.fetchall()
           a=0
           for i in range(0,len(self.row)):
               if (self.row[i][0]==self.username.get() and self.row[i][1]==self.password.get()):
                   a=i+1
                   break
               else:
                   a=0
                   pass
           if a==0:
               messagebox.showinfo('error','Invalid username/password')
           else:
               messagebox.showinfo('info','logged in successfully')
               self.b=a
               self.passenger_detail=self.row
               self.home_page2()
               cur.execute('select * from login_details where user_name=%s and password=%s',(self.username.get(),self.password.get()))
               self.detail=cur.fetchall()
            
    def home_page2(self):
        #variables#
        self.from_var=StringVar()
        self.to_var=StringVar()
        b=self.b
        # bg home page#
        self.f3=Frame(self.root,bg='skyblue',width=1600,height=1000)
        self.f3.place(x=0,y=90)
        self.img3=ImageTk.PhotoImage(Image.open('image4.jpg'))
        self.label3=Label(self.f3,image=self.img3)
        self.label3.pack(side=RIGHT,fill=X,expand=1)
        #top icon frame#
        self.icon_frame=LabelFrame(self.root,bg='white')
        self.icon_frame.place(x=1,y=0,width=1700,height=85)
        self.login=Label(self.icon_frame,text='Logout',bg='yellow',fg='white',font=('calibri',15))
        self.login.place(x=200,y=40)
        self.login.bind('<ButtonRelease-1>',self.Logout)
        self.login=Label(self.icon_frame,text='Welcome'+self.passenger_detail[b-1][4]+' '+self.passenger_detail[b-1][5]+' '+self.passenger_detail[b-1][6]+'('+self.passenger_detail[b-1][0]+')',bg='yellow',fg='white',font=('calibri',15))
        self.login.place(x=400,y=40)
        #TOP LEFT ICON#
        self.f1=Frame(self.icon_frame,bg='skyblue',width=100,height=100)
        self.f1.grid(row=1,column=0)
        self.img1=ImageTk.PhotoImage(Image.open('image2.png'))
        self.label1=Label(self.f1,image=self.img1)
        self.label1.pack()
        #TOP RIGHT ICON#
        self.f2=Frame(self.icon_frame,bg='skyblue',width=150,height=150)
        self.f2.place(x=1460,y=1)
        self.img2=ImageTk.PhotoImage(Image.open('image1.png'))
        self.label2=Label(self.f2,image=self.img2)
        self.label2.pack()
        #entry page in home page#
        self.f4=Frame(self.f3,bg='white',width=600,height=500)
        self.f4.place(x=100,y=100)
        #book ticket frame#
        self.f5=Frame(self.f4,bg='blue',width=600,height=100)
        self.f5.place(x=0,y=0)
         #left icon#
        self.f6=Frame(self.f5,bg='yellow',width=150,height=100)
        self.f6.place(x=0,y=0)
        self.img4=ImageTk.PhotoImage(Image.open('image6.jpg'))
        self.label4=Label(self.f6,image=self.img4)
        self.label4.pack()
        self.label5=Label(self.f5,text='BOOK TICKET',bg='blue',fg='white',font=('calibri',30))
        self.label5.place(x=200,y=25)
         
        #from place#
        self.from_place=ttk.Combobox(self.f4,width=30,font=('arial',15),textvariable=self.from_var,state='readonly')
        self.from_place.place(x=25,y=120)
        self.from_place['values']=('MGR CHENNAI CTL','NEW DELHI')
        self.from_place.set('From')
        #to place#
        self.to_place=ttk.Combobox(self.f4,width=30,font=('arial',15),textvariable=self.to_var,state='readonly')
        self.to_place.place(x=25,y=180)
        self.to_place['values']=('MGR CHENNAI CTL','NEW DELHI')
        self.to_place.set('To')
        
        # date entry #
        self.date_entry=Entry(self.f4,width=15,font=('arial',15))
        self.date_entry.place(x=400,y=120)
        self.today=time.strftime('%d/%m/%y')
        self.date_entry.insert(END,self.today)
        self.b=self.today
        b=self.b.replace('/',' ')
        self.day,self.month,self.year=b.split(' ')
        self.selected_date=self.today
        
        self.date_entry.bind('<ButtonRelease-1>',self.add_date)
         #  combo box for class#
        self.combo1=ttk.Combobox(self.f4,state='readonly')
        self.combo1.place(x=400,y=180)
        self.combo1['values']=('All Classes','AC First Class(1A)','AC 2 Tier(2A)','AC 3 Tier(3A)','Sleeper(SL)','Second sitting(2S)')
        self.combo1.set('All Classes')
        
        
        #  combo box for general#
        self.combo2=ttk.Combobox(self.f4,width=48,state='readonly')
        self.combo2.place(x=25,y=250)
        self.combo2['values']=('GENERAL','LADIES','LOWER BERTH/SR.CITIZEN','PERSON WITH DISABILITY','TATKAL','PREMIUM TATKAL')
        self.combo2.set('GENERAL')

        # search button on home page #
        self.search=Label(self.f4,text='Search',bg='green',fg='white',width=15)
        self.search.place(x=25,y=400)
        self.search.bind('<ButtonRelease-1>',self.page21)
    def Register(self):
        self.register_frame=Frame(self.root,bg='skyblue',width=1600,height=1000)
        self.register_frame.place(x=0,y=90)
        self.account_frame=Frame(self.register_frame,bg='white')
        self.account_frame.place(x=20,y=20,width=1400,height=700)
        account_label=Label(self.account_frame,text='Create Your Account',font=('calibri',15))
        account_label.grid(row=0,column=0,padx=40,pady=20)
        basic_detail_label=Label(self.account_frame,text='Basic detail',bg='green',fg='black',font=('calibri',15))
        basic_detail_label.grid(row=1,column=1,padx=40,pady=20)
        personal_detail_label=Label(self.account_frame,text='Personal detail',bg='white',fg='black',font=('calibri',15))
        personal_detail_label.grid(row=1,column=2,padx=40,pady=20)
        address_label=Label(self.account_frame,text='Address',bg='white',fg='black',font=('calibri',15))
        address_label.grid(row=1,column=3,padx=40,pady=20)

        info_label=Label(self.account_frame,font=('calibri',15),text='GARBAGE/JUNK VALUES IN PROFILE MAY LEAD TO DEACTIVATION \n Please use a valid E-Mail ID and mobile number in registration.')
        info_label.grid(row=2,column=2,padx=40,pady=20)
        user_name_label=Label(self.account_frame,font=('calibri',15),text='User Name:')
        user_name_label.place(x=260,y=250)
        self.user_name_entry=Entry(self.account_frame,font=('calibri',15),width=40)
        self.user_name_entry.place(x=460,y=250)
        password_label=Label(self.account_frame,font=('calibri',15),text='Password:')
        password_label.place(x=260,y=300)
        self.password_entry=Entry(self.account_frame,font=('calibri',15),width=40)
        self.password_entry.place(x=460,y=300)
        self.confirm_password_label=Label(self.account_frame,font=('calibri',15),text='Confirm Password:')
        self.confirm_password_label.place(x=260,y=350)
        self.confirm_password_entry=Entry(self.account_frame,font=('calibri',15),width=40)
        self.confirm_password_entry.place(x=460,y=350)
        cancel_button=Button(self.account_frame,font=('calibri',15),text='Cancel',command=self.back_register_1)
        cancel_button.place(x=260,y=550)

        continue_button=Button(self.account_frame,font=('calibri',15),text='Continue',command=self.register_page_2)
        continue_button.place(x=350,y=550)
    def back_register_1(self):
        self.Login_page()
    def register_page_2(self):
        if (self.user_name_entry.get()=='' or self.password_entry.get()=='' or self.confirm_password_entry.get()==''):
            messagebox.showerror('error','All fields must be filled')
        elif (self.password_entry.get()!=self.confirm_password_entry.get()):
            messagebox.showerror('error','Password need to be same in both the fields')
        else:   
           self.register_frame=Frame(self.root,bg='skyblue',width=1600,height=1000)
           self.register_frame.place(x=0,y=90)
           self.account_frame=Frame(self.register_frame,bg='white')
           self.account_frame.place(x=20,y=20,width=1400,height=700)
           account_label=Label(self.account_frame,text='Create Your Account',font=('calibri',15))
           account_label.grid(row=0,column=0,padx=40,pady=20)
           basic_detail_label=Label(self.account_frame,text='Basic detail',bg='white',fg='black',font=('calibri',15))
           basic_detail_label.grid(row=1,column=1,padx=40,pady=20)
           personal_detail_label=Label(self.account_frame,text='Personal detail',bg='green',fg='black',font=('calibri',15))
           personal_detail_label.grid(row=1,column=2,padx=40,pady=20)
           address_label=Label(self.account_frame,text='Address',bg='white',fg='black',font=('calibri',15))
           address_label.grid(row=1,column=3,padx=40,pady=20)
           first_name_label=Label(self.account_frame,fg='blue',text='First name:')
           first_name_label.place(x=240,y=160)
           self.first_name_entry=Entry(self.account_frame,fg='blue',width=25)
           self.first_name_entry.place(x=310,y=160)
           middle_name_label=Label(self.account_frame,fg='blue',text='Middle name:')
           middle_name_label.place(x=500,y=160)
           self.middle_name_entry=Entry(self.account_frame,fg='blue',width=25)
           self.middle_name_entry.place(x=600,y=160)
           last_name_label=Label(self.account_frame,fg='blue',text='Last name[Optional]')
           last_name_label.place(x=800,y=160)
           self.last_name_entry=Entry(self.account_frame,fg='blue',width=25)
           self.last_name_entry.place(x=950,y=160)
           #combobox for occupation#
           self.occupation_combo=ttk.Combobox(self.account_frame,width=48,state='readonly')
           self.occupation_combo.place(x=240,y=200)
           self.occupation_combo['values']=('GOVERNMENT','PUBLIC','PRIVATE','PROFESSIONAL','SELF EMPLOYED','STUDENT','OTHER')
           self.occupation_combo.set('Select Occupation')
           #date of birth#
           date_label=Label(self.account_frame,font=('arial',15),text='Date Of Birth')
           date_label.place(x=620,y=200)
           self.date_entry=Entry(self.account_frame,width=15,font=('arial',15))
           self.date_entry.place(x=800,y=200)
           self.today=time.strftime('%d/%m/%y')
           self.date_entry.insert(END,'Date Of Birth')
           self.b=self.today
           b=self.b.replace('/',' ')
           self.day,self.month,self.year=b.split(' ')
           self.selected_date=self.today
           self.date_entry.bind('<ButtonRelease-1>',self.add_date_register_page)
           self.marriage_combo=ttk.Combobox(self.account_frame,width=48,state='readonly')
           self.marriage_combo.place(x=240,y=250)
           self.marriage_combo['values']=('Married','Unmarried')
           self.marriage_combo.set('Marriage Status')
        
           #male female transgender#
           self.gender_combo=ttk.Combobox(self.account_frame,width=48,state='readonly')
           self.gender_combo.place(x=240,y=300)
           self.gender_combo['values']=('Male','Female','Transgender')
           self.gender_combo.set('Select gender')
        
           #email entry#
           email_label=Label(self.account_frame,font=('calibri',15),text='Email Id:')
           email_label.place(x=650,y=350)
           self.email_entry=Entry(self.account_frame,width=30)
           self.email_entry.place(x=750,y=350)
           #mobile number#
           mobile_label=Label(self.account_frame,font=('calibri',15),text='Mobile Number:')
           mobile_label.place(x=240,y=350)
           self.mobile_entry=Entry(self.account_frame,font=('calibri',15))
           self.mobile_entry.place(x=400,y=350)
        
           #nationality combo#
           self.nationality_combo=ttk.Combobox(self.account_frame,width=48,state='readonly')
           self.nationality_combo.place(x=600,y=250)
           self.nationality_combo['values']=('India','US')
           self.nationality_combo.set('Select  Nationality')
           #back button#
           back_button=Button(self.account_frame,font=('calibri',15),text='Back',command=self.Register)
           back_button.place(x=240,y=450)

           continue_button=Button(self.account_frame,font=('calibri',15),text='Continue',command=self.register_page_3)
           continue_button.place(x=350,y=450)
    def register_page_3(self):
        if (self.first_name_entry.get()=='' or self.middle_name_entry.get()=='' or self.occupation_combo.get()=='Select Occupation' or self.date_entry.get()=='' or   self.marriage_combo.get()=='Marriage Status' or self.gender_combo.get()=='Select gender' or self.email_entry.get()=='' or self.nationality_combo.get()=='Select  Nationality' or self.mobile_entry.get()==''):
            messagebox.showerror('error','All fields must be filled')
        elif (self.mobile_entry.get().isnumeric()=='False'):
            messagebox.showerror('error','All characters need to be numeric only in the mobile number')
        elif (len(self.mobile_entry.get())!=10) :
            messagebox.showerror('error','Length of mobile number need to be in 10 characters')
        else:   
            self.register_frame=Frame(self.root,bg='skyblue',width=1600,height=1000)
            self.register_frame.place(x=0,y=90)
            self.account_frame=Frame(self.register_frame,bg='white')
            self.account_frame.place(x=20,y=20,width=1400,height=700)
            account_label=Label(self.account_frame,text='Create Your Account',font=('calibri',15))
            account_label.grid(row=0,column=0,padx=40,pady=20)
            basic_detail_label=Label(self.account_frame,text='Basic detail',bg='white',fg='black',font=('calibri',15))
            basic_detail_label.grid(row=1,column=1,padx=40,pady=20)
            personal_detail_label=Label(self.account_frame,text='Personal detail',bg='white',fg='black',font=('calibri',15))
            personal_detail_label.grid(row=1,column=2,padx=40,pady=20)
            address_label=Label(self.account_frame,text='Address',bg='green',fg='black',font=('calibri',15))
            address_label.grid(row=1,column=3,padx=40,pady=20)
            #address #
            flat_no_label=Label(self.account_frame,font=('calibri',15),text='Flat/Door/Block No.')
            flat_no_label.place(x=140,y=160)
            self.flat_no_entry=Entry(self.account_frame,font=('calibri',15),width=25)
            self.flat_no_entry.place(x=340,y=160)
            street_label=Label(self.account_frame,font=('calibri',15),text='Street/Lane')
            street_label.place(x=650,y=160)
            self.street_entry=Entry(self.account_frame,font=('calibri',15),width=25)
            self.street_entry.place(x=800,y=160)
            area_label=Label(self.account_frame,font=('calibri',15),text='Street/Lane')
            area_label.place(x=140,y=200)
            self.area_entry=Entry(self.account_frame,font=('calibri',15),width=25)
            self.area_entry.place(x=340,y=200)
            pincode_label=Label(self.account_frame,font=('calibri',15),text='Pincode')
            pincode_label.place(x=650,y=200)
            self.pincode_entry=Entry(self.account_frame,font=('calibri',15),width=25)
            self.pincode_entry.place(x=800,y=200)
            state_label=Label(self.account_frame,font=('calibri',15),text='State')
            state_label.place(x=140,y=250)
            self.state_entry=Entry(self.account_frame,font=('calibri',15),width=25)
            self.state_entry.place(x=340,y=250)
            city_label=Label(self.account_frame,font=('calibri',15),text='City')
            city_label.place(x=650,y=250)
            self.city_entry=Entry(self.account_frame,font=('calibri',15),width=25)
            self.city_entry.place(x=800,y=250)
            import string
            import random
            self.res=''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase,k=4))
            otp_message_label=Label(self.account_frame,text='Type "Captcha"in the box below:'+str(self.res),font=('calibri',15))
            otp_message_label.place(x=400,y=400)    
            self.otp_message_entry=Entry(self.account_frame,font=('calibri',15))
            self.otp_message_entry.place(x=400,y=440)
            #back button#
            back_register_2=Button(self.account_frame,text='back',font=('calibri',15),command=self.register_page_2)
            back_register_2.place(x=180,y=635)
            register_button=Button(self.account_frame,text='Register',bg='green',fg='white',font=('calibri',15),command=self.register_passenger)
            register_button.place(x=500,y=635)
    def register_passenger(self):
        if (self.flat_no_entry.get()=='' or self.street_entry.get()=='' or self.area_entry.get()=='' or self.pincode_entry.get()=='' or self.state_entry.get()=='' or self.city_entry.get()==''):
            messagebox.showerror('error','All fields must be filled')
        elif(self.otp_message_entry.get()==''):
            messagebox.showerror('error','Enter the captcha and then press Register button')
        elif(self.res!=self.otp_message_entry.get() or self.otp_message_entry.get()==''):
            messagebox.showerror('error','The captcha is incorrect')
        elif (self.res==self.otp_message_entry.get()):
               con=pymysql.connect(host='localhost',user='root',password='',database='arunachalam')
               cur=con.cursor()
               cur.execute('insert into login_details values(%s,%s,%s,%s,%s,%s,%s)',(self.user_name_entry.get(),self.password_entry.get(),self.mobile_entry.get(),self.email_entry.get(),self.first_name_entry.get(),self.middle_name_entry.get(),self.last_name_entry.get()))
               messagebox.showinfo('info','Registeration completed successfully')
               self.Login_page()
        

            
    def add_date_register_page(self,event):
        self.cal=Calendar(self.account_frame,selectmode='day',day=int(self.day),month=int(self.month),year=int(self.year))
        self.cal.place(x=800,y=240)
        self.date_entry.delete(0,'end')
        self.cal.bind('<ButtonRelease-1>',self.insert_date)
        self.date_ok=Button(self.account_frame,text='Insert',command=self.insert_date)
        self.date_ok.place(x=900,y=430)
    
        
        
        #all user defined function for date entry#
    def add_date(self,event):
        self.cal=Calendar(self.root,selectmode='day',day=int(self.day),month=int(self.month),year=int(self.year))
        self.cal.place(x=500,y=340)
        self.date_entry.delete(0,'end')
        self.cal.bind('<ButtonRelease-1>',self.insert_date)
        self.date_ok=Button(self.root,text='insert',command=self.insert_date)
        self.date_ok.place(x=600,y=530)
    def insert_date(self):
        self.cal.destroy()
        self.date_ok.destroy()
        a=self.cal.get_date().replace('/',' ')
        month,day,year=a.split(' ')
        self.b=day+'/'+month+'/'+year
        self.date_entry.insert(END,self.b)
        self.selected_date=self.b
        #page 2#
    def page21(self,event):
        self.class_=self.combo1.get()
        self.general_=self.combo2.get()
        self.from_=self.from_place.get()
        self.to_=self.to_place.get()
        if (self.from_place.get()=='From' or self.to_place.get=='To'):
            messagebox.showerror('error','All fields must be filled')
        elif (self.from_place.get()==self.to_place.get()):
            messagebox.showerror('error','From  place and TO place should not be same')
        else:    
            self.train_schedule()
    def train_schedule(self):
        self.count=1
        self.f8=Frame(self.root,bg='white',width=1600,height=1000)
        self.f8.place(x=0,y=90)
        self.f9=Frame(self.f8,width=1500,height=120,bg='blue')
        self.f9.place(x=20,y=1)  
        #from place #
        self.from_place=ttk.Combobox(self.f9,font=('arial',15))
        self.from_place['values']=('MGR CHENNAI CTL','NEW DELHI')
        self.from_place.set(self.from_) 
        self.from_place.place(x=50,y=20)
        #to place#
        self.to_place=ttk.Combobox(self.f9,font=('arial',15))
        self.to_place.place(x=300,y=20)
        self.to_place['values']=('MGR CHENNAI CTL','NEW DELHI')
        self.to_place.set(self.to_)
        #date#   
        self.date_entry=Entry(self.f9,font=('arial',15))
        self.today=time.strftime('%d/%m/%y')
        self.date_entry.insert(END,self.selected_date)
        self.b=self.today
        b=self.b.replace('/',' ')
        self.day,self.month,self.year=b.split(' ')
        self.date_entry.bind('<ButtonRelease-1>',self.add_date2)
        self.date_entry.place(x=550,y=20)
        #class#
        self.combo1=ttk.Combobox(self.f9,state='readonly')
        self.combo1.set(self.class_)
        self.combo1['values']=('All Classes','AC First Class(1A)','AC 2 Tier(2A)','AC 3 Tier(3A)','Sleeper(SL)','Second sitting(2S)')
        self.combo1.place(x=800,y=20)
        #  combo box for general#
        self.combo2=ttk.Combobox(self.f9,width=48,state='readonly')
        self.combo2.place(x=950,y=20)
        self.combo2['values']=('GENERAL','LADIES','LOWER BERTH/SR.CITIZEN','PERSON WITH DISABILITY','TATKAL','PREMIUM TATKAL')
        self.combo2.set(self.general_)
        #modify search_button#
        self.modify_button=Button(self.f9,text='Modify Search',command=self.modify_search)
        self.modify_button.place(x=1300,y=20)
        #schedule frame#
        self.schedule_frame=Frame(self.f8,bg='white',highlightbackground='blue',highlightthickness=2)
        self.schedule_frame.place(x=550,y=155,width=950,height=200)
        #get details of 1st train#
        con=pymysql.connect(host='localhost',user='root',password='',database='arunachalam')
        cur=con.cursor()
        cur.execute('select * from train where dept_station=%s and station=%s',(self.from_,self.to_))
        self.row=cur.fetchall()
        
        self.train_name=self.row[0][0]
        self.train_no=self.row[0][1]
        self.train_depart=self.row[0][2]
        self.train_arrive=self.row[0][3]
        self.dept_station=self.row[0][4]
        self.station=self.row[0][5]
        self.travel_interval=self.row[0][6]
        self.AC_First_Class_rupee=self.row[0][7]
        self.AC_2_Tier_rupee=self.row[0][8]
        self.AC_3_Tier_rupee=self.row[0][9]
        self.Sleeper_rupee=self.row[0][10]
        self.Second_sitting_rupee=self.row[0][11]
        #get new date#
        get_new_date=self.selected_date
        
        get_new_date=get_new_date.replace('/',' ')
        day,month,year=get_new_date.split(' ')
        
        day_name=datetime.date(int(year),int(month),int(day))
        self.day_name_day=day_name.strftime('%a')
        self.day_name_date=day_name.strftime('%d')
        self.day_name_month=day_name.strftime('%b')
        day_name_year=day_name.strftime('%Y')
    
         
        self.selected_date_=self.selected_date.replace('/','-')+' '+self.train_depart
        new_day_name=datetime.datetime.strptime(self.selected_date_,'%d-%m-%y %H:%M')+datetime.timedelta(hours=33,minutes=40)
        self.new_day_name_day=new_day_name.strftime('%a')
        self.new_day_name_date=new_day_name.strftime('%d')
        self.new_day_name_month=new_day_name.strftime('%b')
        self.show_label=Label(self.f8,bg='skyblue',fg='black',font=('arial',15),text=' 2 results for    '+self.from_+'------>'+self.to_+'|'+self.day_name_day+','+self.day_name_date+self.day_name_month+'     For Quota    '+self.general_+'             ').place(x=550,y=125)
        ##
        label=Label(self.schedule_frame,font=('arial',15),bg='skyblue',fg='black',text=self.train_name+'('+self.train_no+')'+'                                             Runs on M T W T F S S                                      ')
        label.place(x=0,y=0)         
        label=Label(self.schedule_frame,bg='white',fg='black',font=('arial',15),text=self.train_depart+'|'+self.dept_station+'|'+self.day_name_day+','+ self.day_name_date + self.day_name_month+'               -------'+self.travel_interval+'-------             '+self.train_arrive+'|'+self.station+'|'+self.new_day_name_day+','+self.new_day_name_date+self.new_day_name_month)
        label.place(x=0,y=30)
        ##
        class_label=Label(self.schedule_frame,font=('arial',10),text='Class:')
        class_label.place(x=10,y=100)
        self.class_combo=ttk.Combobox(self.schedule_frame,font=('arial',10),state='readonly',width=40)
        self.class_combo.place(x=60,y=100)
        self.class_combo['values']=('AC First Class(1A)  ₹'+self.AC_First_Class_rupee,'AC 2 Tier(1A)  ₹'+self.AC_2_Tier_rupee,'AC 3 Tier(1A)  ₹'+self.AC_3_Tier_rupee,'Sleeper(SL)  ₹'+self.Sleeper_rupee,'Second sitting(2S)  ₹'+self.Second_sitting_rupee)
        #
        self.btn1=Label(self.schedule_frame,font=('arial',10),text='Book Now',bg='orange',width=12,height=2)
        self.btn1.place(x=5,y=150)
        self.btn1.bind('<ButtonRelease-1>',self.book_now1)
        #get details of 2nd train#
        self.schedule_frame2=Frame(self.f8,width=950,height=200,bg='white',highlightbackground='blue',highlightthickness=2)
        self.schedule_frame2.place(x=550,y=357)
        self.train_name2=self.row[1][0]
        self.train_no2=self.row[1][1]
        self.train_depart2=self.row[1][2]
        self.train_arrive2=self.row[1][3]
        self.dept_station2=self.row[1][4]
        self.station2=self.row[1][5]
        self.travel_interval2=self.row[1][6]
        self.AC_First_Class_rupee2=self.row[1][7]
        self.AC_2_Tier_rupee2=self.row[1][8]
        self.AC_3_Tier_rupee2=self.row[1][9]
        self.Sleeper_rupee2=self.row[1][10]
        self.Second_sitting_rupee2=self.row[1][11]
        #get new date#
        new_day_name2=datetime.datetime.strptime(self.selected_date_,'%d-%m-%y %H:%M')+datetime.timedelta(hours=35,minutes=45)

        self.new_day_name_day2=new_day_name2.strftime('%a')
        self.new_day_name_date2=new_day_name2.strftime('%d')
        self.new_day_name_month2=new_day_name2.strftime('%b')
        #schedule frame#
        label=Label(self.schedule_frame2,bg='skyblue',fg='black',font=('arial',15),text=self.train_name2+'('+self.train_no2+')'+'                                        Runs on M T W T F S S                                      ')
        label.place(x=0,y=0)          
        label=Label(self.schedule_frame2,bg='white',fg='black',font=('arial',15),text=self.train_depart2+'|'+self.dept_station2+'|'+self.day_name_day+','+ self.day_name_date + self.day_name_month+'             -------'+self.travel_interval2+'-------               '+self.train_arrive2+'|'+self.station2+'|'+self.new_day_name_day2+','+self.new_day_name_date2+self.new_day_name_month2)
        label.place(x=0,y=30)
        ##
        class_label=Label(self.schedule_frame2,font=('arial',10),text='Class:')
        class_label.place(x=10,y=100)
        self.class_combo2=ttk.Combobox(self.schedule_frame2,font=('arial',10),state='readonly',width=40)
        self.class_combo2.place(x=60,y=100)
        self.class_combo2['values']=('AC First Class(1A)  ₹'+self.AC_First_Class_rupee2,'AC 2 Tier(1A)  ₹'+self.AC_2_Tier_rupee2,'AC 3 Tier(1A)  ₹'+self.AC_3_Tier_rupee2,'Sleeper(SL)  ₹'+self.Sleeper_rupee2,'Second sitting(2S)  ₹'+self.Second_sitting_rupee2)
        #
        self.btn2=Label(self.schedule_frame2,font=('arial',10),text='Book Now',bg='orange',width=12,height=2)
        self.btn2.place(x=5,y=150)
        self.btn2.bind('<ButtonRelease-1>',self.book_now2)
        #show label#
    def modify_search(self):
        self.from_=self.from_place.get()
        self.to_=self.to_place.get()
        self.selected_date=self.date_entry.get()
        if (self.from_place.get()==self.to_place.get()):
            messagebox.showerror('error','Both From place and To place should not be same')
        else:    
            self.train_schedule()
    def add_date2(self,event):
        self.cal=Calendar(self.f8,selectmode='day',day=int(self.day),month=int(self.month),year=int(self.year))
        self.cal.place(x=570,y=50)
        self.date_entry.delete(0,'end')
        self.cal.bind('<ButtonRelease-1>',self.insert_date2)
        self.date_insert=Button(self.f8,text='Insert',command=self.insert_date2)
        self.date_insert.place(x=670,y=240)
    def insert_date2(self):
        self.cal.destroy()
        self.date_insert.destroy()
        a=self.cal.get_date().replace('/',' ')
        month,day,year=a.split(' ')
        self.b=day+'/'+month+'/'+year
        self.date_entry.insert(END,self.b)
        self.selected_date=self.b             
        
    def book_now1(self,event):
        if self.class_combo.get()=='':
            messagebox.showerror('error','Select a class and then press the Book Now Button')
        else:
            self.a=self.row[0][1]
            self.b=self.class_combo.get()[:-5]
            self.c=self.new_day_name_day
            self.d=self.new_day_name_date
            self.e=self.new_day_name_month
            self.f=self.class_combo.get()[-5:]
            self.Passenger_Details()     
 
    def book_now2(self,event):
        if self.class_combo2.get()=='':
            messagebox.showerror('error','Select a class and then press the Book Now Button')
        else:
            self.a=self.row[1][1]
            self.b=self.class_combo.get()[:-5]
            self.c=self.new_day_name_day2
            self.d=self.new_day_name_date2
            self.e=self.new_day_name_month2
            self.f=self.class_combo.get()[-5:]
            self.Passenger_Details()
        
    
     #page 3 passenger details#
    def Passenger_Details(self):
        self.f10=Frame(self.root,bg='sky blue',width=1600,height=55)
        self.f10.place(x=0,y=90)
        Passenger_details_label=Label(self.f10,font=('arial',15),text='Passenger details',bg='green',fg='white')
        Passenger_details_label.place(x=55,y=10)
        Review_Journey_label=Label(self.f10,font=('arial',15),text='Review Journey',bg='sky blue',fg='white')
        Review_Journey_label.place(x=455,y=10)
        Payment_label=Label(self.f10,text='Payment',bg='sky blue',font=('arial',15),fg='white')
        Payment_label.place(x=855,y=10)
        
        
        self.f11=Frame(self.root,bg='skyblue',width=1600,height=1000)
        self.f11.place(x=0,y=140)
        self.Passenger_details_frame=Frame(self.f11,width=1200,highlightbackground='blue',highlightthickness=2,height=100)
        self.Passenger_details_frame.place(x=0,y=0)
        #get details of selected train#
        con=pymysql.connect(host='localhost',user='root',password='',database='arunachalam')
        cur=con.cursor()
        cur.execute('select * from train where  train_no ='+self.a)
        self.row=cur.fetchall()
        
        
        label=Label(self.Passenger_details_frame,font=('arial',15),text=self.row[0][0]+'('+self.row[0][1]+')'+'                                                                                                             ')
        label.place(x=0,y=0)                                          
        label=Label(self.Passenger_details_frame,font=('arial',15),text=self.row[0][2]+'|'+self.row[0][4]+'                -------'+self.travel_interval2+'-------                     '+self.row[0][3]+'|'+self.row[0][5]+'|')
        label.place(x=0,y=25)
        label=Label(self.Passenger_details_frame,font=('arial',15),text=self.day_name_day+','+self.day_name_date+self.day_name_month)
        label.place(x=10,y=55)
        label=Label(self.Passenger_details_frame,font=('arial',15),text=self.c+','+self.d+self.e)
        label.place(x=680,y=55)
        label=Label(self.Passenger_details_frame,font=('arial',15),text=self.f+'|'+self.combo2.get())
        label.place(x=310,y=55)
         
        #passenger details frame#
        self.Passenger_details_frame2=Frame(self.f11,bg='skyblue',width=1200,height=500)
        self.Passenger_details_frame2.place(x=0,y=105)
        self.Passenger_details_frame3=Frame(self.Passenger_details_frame2,highlightbackground='blue',highlightthickness=2,width=1200,height=130)
        self.Passenger_details_frame3.place(x=0,y=50)
        self.passenger_label=Label(self.Passenger_details_frame2,font=('arial',15),text='Passenger details')
        self.passenger_label.place(x=3,y=2)
        self.passenger_name_label=Label(self.Passenger_details_frame3,font=('arial',15),text='Passenger Name:')
        self.passenger_name_label.place(x=0,y=30)    
        self.passenger_name=Entry(self.Passenger_details_frame3,width=25,font=('arial',15))
        self.passenger_name.place(x=190,y=30)
        
        self.passenger_age=Spinbox(self.Passenger_details_frame3,from_=1,to=125,font=('arial',15))
        self.passenger_age.delete(0,END)
        self.passenger_age.insert(END,'Age')
        self.passenger_age.place(x=0,y=60)
        
        # Combobox Gender#
        self.Gender_combo=ttk.Combobox(self.Passenger_details_frame3,state='readonly',font=('arial',15))
        self.Gender_combo.place(x=550,y=30)
        self.Gender_combo['values']=('Male','Female','Transgender')
        self.Gender_combo.set('Gender')
        #Combobox for seat preference#
        self.Preference_combo=ttk.Combobox(self.Passenger_details_frame3,state='readonly',font=('arial',15))
        self.Preference_combo.place(x=550,y=60)
        self.Preference_combo['values']=('Lower','Upper','Side Lower','Side Upper')
        self.Preference_combo.set('No Preference')
        #Combobox for food choice#
        self.Food_combo=ttk.Combobox(self.Passenger_details_frame3,state='readonly',font=('arial',15))
        self.Food_combo.place(x=300,y=60)
        self.Food_combo['values']=('Veg','Non Veg','No food')
        self.Food_combo.set('Food Choice*')
        #Add passenger button
        self.add_passenger_button=Button(self.Passenger_details_frame3,font=('arial',10),text='Add Passenger',command=self.Add_Passenger)
        self.add_passenger_button.place(x=10,y=90)
        #contact details#
        self.Passenger_details_frame6=Frame(self.f11,highlightbackground='blue',highlightthickness=2,width=1200,height=70)
        self.Passenger_details_frame6.place(x=0,y=520)
        #contact label#
        contact_label=Label(self.Passenger_details_frame6,text='Contact Details',font=('arial',15))
        contact_label.place(x=0,y=0)
        inform_label=Label(self.Passenger_details_frame6,font=('arial',15),text='Tickets will be sent to email:'+self.detail[0][3]+'and Registered Number:'+self.detail[0][2])
        inform_label.place(x=0,y=30)
        self.continue_page3=Button(self.f11,text='Continue',font=('arial',15),bg='green',fg='white',command=self.continue_page3)
        self.continue_page3.place(x=100,y=610)
        #ticket fare#
        self.Passenger_details_frame8=Frame(self.f11,highlightbackground='blue',highlightthickness=2,width=300,height=100)
        self.Passenger_details_frame8.place(x=1225,y=0)
        ticket_fare_label=Label(self.Passenger_details_frame8,font=('arial',15),text='       Fare Summary        ')
        ticket_fare_label.pack()
        
        ticket_fare_label=Label(self.Passenger_details_frame8,font=('arial',15),text='Ticket fare                     '+self.f)
        ticket_fare_label.pack()
        ticket_fare_label=Label(self.Passenger_details_frame8,font=('arial',15),text='Total fare                     '+self.f)
        ticket_fare_label.pack()
        
    def Add_Passenger(self):
        if self.count==2:
            messagebox.showerror('error','You Have Selected Maximum number of Passengers, \n You cannot select more.')
    
        else:
            self.Passenger_details_frame4=Frame(self.Passenger_details_frame2,highlightbackground='blue',highlightthickness=2)
            self.Passenger_details_frame4.place(x=0,y=235,width=1200,height=130)
            self.passenger_name_label=Label(self.Passenger_details_frame4,font=('arial',15),text='Passenger Name:')
            self.passenger_name_label.place(x=0,y=30)
            self.passenger_name2=Entry(self.Passenger_details_frame4,width=25,font=('arial',15))
            self.passenger_name2.place(x=190,y=30)
            self.passenger_age2=Spinbox(self.Passenger_details_frame4,from_=1,to=125,font=('arial',15))
            self.passenger_age2.delete(0,END)
            self.passenger_age2.insert(END,'Age')
            self.passenger_age2.place(x=0,y=60)
            #Button close#
            self.close_button2=Button(self.Passenger_details_frame4,text='X',font=('arial',10),command=self.close_button)
            self.close_button2.place(x=1100,y=0)
            #Combobox Gender#
            self.Gender_combo2=ttk.Combobox(self.Passenger_details_frame4,state='readonly',font=('arial',15))
            self.Gender_combo2.place(x=550,y=30)
            self.Gender_combo2['values']=('Male','Female','Transgender')
            self.Gender_combo2.set('Gender')
            #Combobox for seat preference#
            self.Preference_combo2=ttk.Combobox(self.Passenger_details_frame4,state='readonly',font=('arial',15))
            self.Preference_combo2.place(x=550,y=60)
            self.Preference_combo2['values']=('Lower','Upper','Side Lower','Side Upper')
            self.Preference_combo2.set('No Preference')
            #Combobox for food choice#
            self.Food_combo2=ttk.Combobox(self.Passenger_details_frame4,state='readonly',font=('arial',15))
            self.Food_combo2.place(x=300,y=60)
            self.Food_combo2['values']=('Veg','Non Veg','No food')
            self.Food_combo2.set('Food Choice*')
            self.count=2
            self.add_passenger_button_hide=Label(self.Passenger_details_frame3,height=2,width=30,text='                                    ')
            self.add_passenger_button_hide.place(x=10,y=90)
            self.add_passenger_button=Button(self.Passenger_details_frame4,text='+Add Passenger',font=('arial',10),command=self.Add_Passenger)
            self.add_passenger_button.place(x=0,y=90)
            
    def close_button(self):
        self.Passenger_details_frame41=Frame(self.Passenger_details_frame2,bg='skyblue')
        self.Passenger_details_frame41.place(x=0,y=235,width=1200,height=130)
        self.add_passenger_button=Button(self.Passenger_details_frame3,font=('arial',10),text='+Add Passenger',command=self.Add_Passenger)
        self.add_passenger_button.place(x=10,y=90)
        '''self.add_passenger_button_hide=Label(self.Passenger_details_frame3,height=4,width=10,text='  ',bg='skyblue')
        self.add_passenger_button_hide.place(x=0,y=20)'''
        self.count=1    
    def Back_page2(self):
        self.train_schedule()
    def continue_page3(self):
        if (self.count==1) and (self.passenger_name.get()=='' or self.passenger_age.get()=='Age' or self.Gender_combo.get()=='Gender' or self.Preference_combo.get()=='No Preference' or self.Food_combo.get()=='Food Choice*'):
            messagebox.showerror('error','All fields must be filled')
            
        elif (self.count==2) and (self.passenger_name2.get()=='' or self.passenger_age2.get()=='Age' or self.Gender_combo2.get()=='Gender' or self.Preference_combo2.get()=='No Preference' or self.Food_combo2.get()=='Food Choice*'): 
           messagebox.showerror('error','All fields must be filled')

        if (self.count==1) and (self.passenger_name.get()!='' and self.passenger_age.get()!='Age' and self.Gender_combo.get()!='Gender' and self.Preference_combo.get()!='No Preference' and self.Food_combo.get()!='Food Choice*'):
            self.passenger_name1_get=self.passenger_name.get()
            self.passenger_age1_get=self.passenger_age.get()
            self.Gender_combo1_get=self.Gender_combo.get()
            self.Preference_combo1_get=self.Preference_combo.get()
            self.Food_combo1_get=self.Food_combo.get()
            self.view_journey()
        elif (self.count==2) and (self.passenger_name2.get()!='' and self.passenger_age2.get()!='Age' and self.Gender_combo2.get()!='Gender' and self.Preference_combo2.get()!='No Preference' and self.Food_combo2.get()!='Food Choice*'): 
           self.passenger_name1_get=self.passenger_name.get()
           self.passenger_age1_get=self.passenger_age.get()
           self.Gender_combo1_get=self.Gender_combo.get()
           self.Preference_combo1_get=self.Preference_combo.get()
           self.Food_combo1_get=self.Food_combo.get()
      

           self.passenger_name2_get=self.passenger_name2.get()
           self.passenger_age2_get=self.passenger_age2.get()
           self.Gender_combo2_get=self.Gender_combo2.get()
           self.Preference_combo2_get=self.Preference_combo2.get()
           self.Food_combo2_get=self.Food_combo2.get()
           self.view_journey()
           
        
     #page 4 view journey#
    def view_journey(self):
        self.f12=Frame(self.root,bg='skyblue',width=1600,height=1000)
        self.f12.place(x=0,y=140)
        
        Payment_label=Label(self.f10,text='Review Journey',bg='green',fg='white',font=('arial',15))
        Payment_label.place(x=455,y=10)
        self.Passenger_details_frame=Frame(self.f12,highlightbackground='blue',highlightthickness=2,width=1200,height=100)
        self.Passenger_details_frame.place(x=0,y=0)
        #get details of selected train#
        con=pymysql.connect(host='localhost',user='root',password='',database='arunachalam')
        cur=con.cursor()
        cur.execute('select * from train where  train_no ='+self.a)
        self.row=cur.fetchall()
        
        
        label=Label(self.Passenger_details_frame,font=('arial',15),text=self.row[0][0]+'('+self.row[0][1]+')'+'                                                                                                                                                                                                                                ')
        label.place(x=0,y=0)                                          
        label=Label(self.Passenger_details_frame,font=('arial',15),text=self.row[0][2]+'|'+self.row[0][4]+'                -------'+self.travel_interval2+'-------                     '+self.row[0][3]+'|'+self.row[0][5]+'|')
        label.place(x=0,y=25)
        label=Label(self.Passenger_details_frame,font=('arial',15),text=self.day_name_day+','+self.day_name_date+self.day_name_month)
        label.place(x=10,y=55)
        label=Label(self.Passenger_details_frame,font=('arial',15),text=self.c+','+self.d+self.e)
        label.place(x=680,y=55)
        label=Label(self.Passenger_details_frame,font=('arial',15),text=self.f+'|'+self.combo2.get())
        label.place(x=310,y=55)
        #ticket fare frame#
        self.Passenger_details_frame8=Frame(self.f12,highlightbackground='blue',highlightthickness=2,width=300,height=100)
        self.Passenger_details_frame8.place(x=1225,y=0)
        ticket_fare_label=Label(self.Passenger_details_frame8,font=('arial',15),text='       Fare Summary        ')
        ticket_fare_label.grid(row=0,column=0,padx=10,pady=10)
        
        ticket_fare_label=Label(self.Passenger_details_frame8,text='Ticket fare                     '+str(float(self.f[1:])*self.count))
        ticket_fare_label.grid(row=1,column=0,padx=10,pady=10)
        ticket_fare_label=Label(self.Passenger_details_frame8,text='Convenience Fee            '+'₹'+str((float(self.f[1:])*self.count)/10))
        ticket_fare_label.grid(row=2,column=0,padx=10,pady=10)
        ticket_fare_label=Label(self.Passenger_details_frame8,text='Total fare                     '+'₹'+str((float(self.f[1:])*self.count)+(float(self.f[1:]))*self.count/10))
        ticket_fare_label.grid(row=3,column=0,padx=10,pady=10)
        
        
        Payment_frame=Frame(self.f12,highlightbackground='blue',highlightthickness=2,width=1000,height=200)
        Payment_frame.place(x=10,y=100)
        label1=Label(Payment_frame,text='Payment Details',font=('arial',15))
        label1.place(x=0,y=0)
        if self.count==1:
            name_label=Label(Payment_frame,font=('arial',15),text='1.'+self.passenger_name1_get+'|'+self.passenger_age1_get+'yrs  |'+self.Gender_combo1_get+'|'+self.Preference_combo1_get+'|'+self.Food_combo1_get)
            name_label.place(x=10,y=40)
        elif self.count==2:
            name_label=Label(Payment_frame,font=('arial',15),text='1.'+self.passenger_name1_get+'|'+self.passenger_age1_get+'yrs  |'+self.Gender_combo1_get+'|'+self.Preference_combo1_get+'|'+self.Food_combo1_get)
            name_label.place(x=10,y=40)
            name_label2=Label(Payment_frame,font=('arial',15),text='2.'+self.passenger_name2_get+'|'+self.passenger_age2_get+'yrs  |'+self.Gender_combo2_get+'|'+self.Preference_combo2_get+'|'+self.Food_combo2_get)
            name_label2.place(x=10,y=80)
        
        contact_frame=Frame(self.f12,highlightbackground='blue',highlightthickness=2,width=1000,height=30)
        contact_frame.place(x=10,y=250)
        con=pymysql.connect(host='localhost',user='root',password='',database='arunachalam')
        cur=con.cursor()
        cur.execute('select * from login_details where user_name=%s and password=%s',(self.username.get(),self.password.get()))
        self.detail=cur.fetchall()
            
        label2=Label(contact_frame,font=('arial',15),text='Your ticket will be issued to '+self.detail[0][3]+'/'+self.detail[0][2])
        label2.place(x=0,y=0)
        import string
        import random
        self.otp=''.join(random.choices(string.ascii_lowercase + string.digits,k=4))

        otp_message_label=Label(self.f12,font=('arial',15),text='Type "Captcha" in the box below:'+str(self.otp))
        otp_message_label.place(x=300,y=450)
        self.otp_message_entry=Entry(self.f12,font=('arial',15))
        self.otp_message_entry.place(x=300,y=480)
        payment_button=Button(self.f12,font=('arial',15),text='Payment',command=self.Payment)
        payment_button.place(x=150,y=550)
            
    def clear_otp_label():
        self.otp_message_entry.delete(0,END)
    def Payment(self):
        if self.otp_message_entry.get()!=str(self.otp):
           messagebox.showerror('error','OTP you have typed is incorrect')
        else:
            messagebox.showinfo('Payment has been done','Your ticket has been booked successfully')
    def Logout(self,event):
        self.Login_page()
        messagebox.showinfo('Logout','Account has been Logged out successfully')
        
        
        

 
    
         
         
         

        





        
obj=Train(root)
root.mainloop()

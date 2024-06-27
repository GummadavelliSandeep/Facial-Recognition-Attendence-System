from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1830x790+0+0")
        self.root.title("face Recognition System")

        # variables
        self.var_dep=StringVar();
        self.var_course=StringVar();
        self.var_year=StringVar();
        self.var_sem=StringVar();
        self.var_id=StringVar();
        self.var_name=StringVar(); 
        self.var_section=StringVar();
        self.var_gender=StringVar();
        self.var_dob=StringVar();
        self.var_phone=StringVar();
        self.var_email=StringVar();
        self.var_address=StringVar();



        #first image
        img1=Image.open(r"C:\Users\DELL\OneDrive\Desktop\Face Recognition Attendence System\Images\front imageW.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_img=Label(self.root,image=self.photoimg1)
        f_img.place(x=30,y=0,width=500,height=130)

        #second image
        img2=Image.open(r"C:\Users\DELL\OneDrive\Desktop\Face Recognition Attendence System\Images\studentimage.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_img=Label(self.root,image=self.photoimg2)
        f_img.place(x=500,y=0,width=500,height=130)


        #third image
        img3=Image.open(r"C:\Users\DELL\OneDrive\Desktop\Face Recognition Attendence System\Images\front imageW.jpg")
        img3=img3.resize((500,130),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_img=Label(self.root,image=self.photoimg1)
        f_img.place(x=1000,y=0,width=500,height=130)


        # bg image
        img4=Image.open(r"C:\Users\DELL\OneDrive\Desktop\Face Recognition Attendence System\Images\background image.jpg")
        img4=img4.resize((1530,710),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)


        # title of the project
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="White",fg="Black")
        title_lbl.place(x=-3,y=-3,width=1533,height=60)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=-2,y=50,width=1530,height=710)

        # left Label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)


        # Current Course Information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=10,width=720,height=200)

        # Department

        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)


        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        # course

        dep_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=2,padx=10,sticky=W)


        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Course","CSE","IT","ECE","EEE","MECH")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        # year

        dep_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=0,padx=10,sticky=W)


        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Year","First Year","Second Year","Third Year","Final Year")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        
        # Semester

        dep_label=Label(current_course_frame,text="Sem",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10,sticky=W)


        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Semester","First Sem","Second Sem")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Class Student Information

        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=300)

        # studentID
        studentId_label=Label(class_student_frame,text="StudentID",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_id,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10, pady=5,sticky=W)

        # student Name
        studentId_label=Label(class_student_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=2,padx=10,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_name,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10, pady=5,sticky=W)

        # student section
        student_label=Label(class_student_frame,text="Student Section",font=("times new roman",12,"bold"),bg="white")
        student_label.grid(row=1,column=0,padx=10,sticky=W)

        student_combo=ttk.Combobox(class_student_frame,textvariable=self.var_section,font=("times new roman",12,"bold"),state="readonly",width=20)
        student_combo["values"]=("Select","A","B","C","D","E","F")
        student_combo.current(0)
        student_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Gender
        student_label=Label(class_student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        student_label.grid(row=1,column=2,padx=10,sticky=W)

        student_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=20)
        student_combo["values"]=("Select","Male","Female","Others")
        student_combo.current(0)
        student_combo.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        
        # DOB
        studentId_label=Label(class_student_frame,text="Date Of Birth",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=2,column=0,padx=10,sticky=W)

        studentSection_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_dob,font=("times new roman",13,"bold"))
        studentSection_entry.grid(row=2,column=1,padx=10, pady=5,sticky=W)
        
        
        # Phone No
        studentId_label=Label(class_student_frame,text="Phone No",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=2,column=2,padx=10,sticky=W)

        studentSection_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_phone,font=("times new roman",13,"bold"))
        studentSection_entry.grid(row=2,column=3,padx=10, pady=5,sticky=W)


        # Email
        studentId_label=Label(class_student_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=3,column=0,padx=10,sticky=W)

        studentSection_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_email,font=("times new roman",13,"bold"))
        studentSection_entry.grid(row=3,column=1,padx=10, pady=5,sticky=W)

        # Address
        studentId_label=Label(class_student_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=3,column=2,padx=10,sticky=W)

        studentSection_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_address,font=("times new roman",13,"bold"))
        studentSection_entry.grid(row=3,column=3,padx=10, pady=5,sticky=W)


        # radiobuttons
        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="yes")
        radiobutton1.grid(row=6,column=0)

        self.var_radio2=StringVar()
        radiobutton1=ttk.Radiobutton(class_student_frame,variable=self.var_radio2,text="No Photo Sample",value="yes")
        radiobutton1.grid(row=6,column=1)

        # buttonsFrames
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=180,width=715,height=35)

        save_btn=Button(btn_frame,text="Save", command=self.add_data,font=("times new roman",13,"bold"),width=17,bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update", command=self.update_data,font=("times new roman",13,"bold"),width=17,bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,font=("times new roman",13,"bold"),width=17,bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",13,"bold"),width=17,bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        # buttonsFrames1
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=220,width=715,height=35)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,font=("times new roman",13,"bold"),width=35,bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=1)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",font=("times new roman",13,"bold"),width=35,bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=2)










        # right Label frame
        RIGHT_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student Details",font=("times new roman",12,"bold"))
        RIGHT_frame.place(x=780,y=10,width=660,height=580)


        search_frame=LabelFrame(RIGHT_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=5,width=640,height=70)

        studentId_label=Label(search_frame,text="Search By",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=2,column=0,padx=2,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=20)
        search_combo["values"]=("Select","StudentID","Student Name","Phone No")
        search_combo.current(0)
        search_combo.grid(row=2,column=1,padx=2,pady=2,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=2,column=2,padx=5, pady=5,sticky=W)

        update_btn=Button(search_frame,text="Search",font=("times new roman",13,"bold"),width=9,bg="blue",fg="white")
        update_btn.grid(row=2,column=4,padx=2)

        delete_btn=Button(search_frame,text="Search All",font=("times new roman",13,"bold"),width=9,bg="blue",fg="white")
        delete_btn.grid(row=2,column=5,padx=2)


        # TableFrame
        table_frame=LabelFrame(RIGHT_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=100,width=640,height=350)
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","section","gender","dob","phone","email","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)   
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview) 

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("section",text="Section")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="Date Of Birth")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="Photo Status")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("section",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # function declarations
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="facial_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_dep.get(),
                                                                                                    self.var_course.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_sem.get(),
                                                                                                    self.var_id.get(),
                                                                                                    self.var_name.get(),
                                                                                                    self.var_section.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_dob.get(),
                                                                                                    self.var_phone.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_address.get(),
                                                                                                    self.var_radio1.get()
                    

                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showinfo("Error",f"Due To :{str(es)}",parent=self.root)


    # fetch data
    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="facial_recognition")
            my_cursor=conn.cursor()
            my_cursor.execute("select*from student")
            data=my_cursor.fetchall()

            if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)
                conn.commit()
            conn.close()

    # get cursor
    def get_cursor(self,even=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_id.set(data[4])
        self.var_name.set(data[5])
        self.var_section.set(data[6])
        self.var_gender.set(data[7])
        self.var_dob.set(data[8])
        self.var_phone.set(data[9])
        self.var_email.set(data[10])
        self.var_address.set(data[11])
        self.var_radio1.set(data[12])

    # Update Data
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name=="" or self.var_id=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do You want to Update this student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="facial_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Student_Name=%s,Section=%s,Gender=%s,DOB=%s,Phone_No=%s,Email=%s,Address=%s,Photo_Sample=%s where Student_Id=%s",(
                                                                                                                            self.var_dep.get(),
                                                                                                                            self.var_course.get(),
                                                                                                                            self.var_year.get(),
                                                                                                                            self.var_sem.get(),
                                                                                                                            self.var_name.get(),
                                                                                                                            self.var_section.get(),
                                                                                                                            self.var_gender.get(),
                                                                                                                            self.var_dob.get(),
                                                                                                                            self.var_phone.get(),
                                                                                                                            self.var_email.get(),
                                                                                                                            self.var_address.get(),
                                                                                                                            self.var_radio1.get(),
                                                                                                                            self.var_id.get()

                                                                                                                            ))
                else:
                    if not update:
                        return
                messagebox.showinfo("sucess","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # Delete Data
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to Delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="facial_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_Id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","successfully deleted the student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # reset
    def reset_data(self):
         self.var_dep.set("Select Department"),
         self.var_course.set("Select Course"),
         self.var_year.set("Select Year"),
         self.var_sem.set("Select Semester"),
         self.var_id.set(""),
         self.var_name.set(""),
         self.var_section.set("Select"),
         self.var_gender.set("Select"),
         self.var_dob.set(""),
         self.var_phone.set(""),
         self.var_email.set(""),
         self.var_address.set(""),
         self.var_radio1.set("")

    # Generate data set or Take Photo Samples
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name=="" or self.var_id=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="facial_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Student_Name=%s,Section=%s,Gender=%s,DOB=%s,Phone_No=%s,Email=%s,Address=%s,Photo_Sample=%s where Student_Id=%s",(
                                                                                                                            self.var_dep.get(),
                                                                                                                            self.var_course.get(),
                                                                                                                            self.var_year.get(),
                                                                                                                            self.var_sem.get(),
                                                                                                                            self.var_name.get(),
                                                                                                                            self.var_section.get(),
                                                                                                                            self.var_gender.get(),
                                                                                                                            self.var_dob.get(),
                                                                                                                            self.var_phone.get(),
                                                                                                                            self.var_email.get(),
                                                                                                                            self.var_address.get(),
                                                                                                                            self.var_radio1.get(),
                                                                                                                            self.var_id.get()==id+1

                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                # Load predefined data in face frontals from opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                        for(x,y,w,h) in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped
                        
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(my_frame),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            cv2.imshow("Cropped Face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed sucessfully!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                


                                                                                                                            
                

        
                    




        












if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
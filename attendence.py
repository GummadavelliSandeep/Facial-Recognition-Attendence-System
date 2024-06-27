from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1830x790+0+0")
        self.root.title("face Recognition System")

        #variables
        self.var_id=StringVar()
        self.var_student_id=StringVar()
        self.var_student_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_atten_attendence=StringVar()
        


        #first image
        img1=Image.open(r"C:\Users\DELL\OneDrive\Desktop\Face Recognition Attendence System\Images\front imageW.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_img=Label(self.root,image=self.photoimg1)
        f_img.place(x=30,y=0,width=500,height=130)

        #second image
        img2=Image.open(r"C:\Users\DELL\OneDrive\Desktop\Face Recognition Attendence System\Images\front imageW.jpg")
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
        title_lbl=Label(bg_img,text="STUDENT ATTENDENCE",font=("times new roman",35,"bold"),bg="White",fg="green")
        title_lbl.place(x=-3,y=-3,width=1533,height=60)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=-2,y=50,width=1530,height=710)

        # left Label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendence Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=300)



        # ID
        Id_label=Label(Left_frame,text="ID",font=("times new roman",12,"bold"),bg="white")
        Id_label.grid(row=0,column=0,padx=10,sticky=W)

        ID_entry=ttk.Entry(Left_frame,width=20,textvariable=self.var_id,font=("times new roman",13,"bold"))
        ID_entry.grid(row=0,column=1,padx=10, pady=5,sticky=W)

        # student_Id
        studentId_label=Label(Left_frame,text="Student_Id",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=2,padx=10,sticky=W)

        studentID_entry=ttk.Entry(Left_frame,width=20,textvariable=self.var_student_id,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=3,padx=10, pady=5,sticky=W)

        # student Name
        studentName_label=Label(Left_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=1,column=0,padx=10,sticky=W)

        studentName_entry=ttk.Entry(Left_frame,width=20,textvariable=self.var_student_name,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=1,column=1,padx=10, pady=5,sticky=W)
        

        # Department
        student_Department=Label(Left_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        student_Department.grid(row=1,column=2,padx=10,sticky=W)

        studentDepartment_entry=ttk.Entry(Left_frame,width=20,textvariable=self.var_dep,font=("times new roman",13,"bold"))
        studentDepartment_entry.grid(row=1,column=3,padx=10, pady=5,sticky=W)

        # Time
        time_label=Label(Left_frame,text="Time",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,sticky=W)

        time_entry=ttk.Entry(Left_frame,width=20,textvariable=self.var_time,font=("times new roman",13,"bold"))
        time_entry.grid(row=2,column=1,padx=10, pady=5,sticky=W)
        # date
        date=Label(Left_frame,text="Date",font=("times new roman",12,"bold"),bg="white")
        date.grid(row=2,column=2,padx=10,sticky=W)

        date_entry=ttk.Entry(Left_frame,width=20,textvariable=self.var_date,font=("times new roman",13,"bold"))
        date_entry.grid(row=2,column=3,padx=10, pady=5,sticky=W)


        # Attendence Status
        attendence_label=Label(Left_frame,text="Attendence Status",font=("times new roman",12,"bold"),bg="white")
        attendence_label.grid(row=3,column=0,padx=10,sticky=W)
        attendence_combo=ttk.Combobox(Left_frame,textvariable=self.var_atten_attendence,font=("times new roman",12,"bold"),state="readonly",width=20)
        attendence_combo["values"]=("Status","Present","Absent")
        attendence_combo.current(0)
        attendence_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        # buttonsFrames
        btn_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=180,width=715,height=35)

        import_btn=Button(btn_frame,text="Import csv", command=self.importCsv,font=("times new roman",13,"bold"),width=17,bg="blue",fg="white")
        import_btn.grid(row=0,column=0)

        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,font=("times new roman",13,"bold"),width=17,bg="blue",fg="white")
        export_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame, text="Update",command=self.update_data,font=("times new roman",13,"bold"),width=17,bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",13,"bold"),width=17,bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)




        
        # right Label frame
        RIGHT_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence Details",font=("times new roman",12,"bold"))
        RIGHT_frame.place(x=780,y=10,width=660,height=300)

        table_frame=LabelFrame(RIGHT_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=0,width=640,height=250)
        
        #scroll bar table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendenceReportTable=ttk.Treeview(table_frame,column=("id","studentId","studentname","dep","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)   

        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview) 



        self.AttendenceReportTable.heading("id",text="Id")
        self.AttendenceReportTable.heading("studentId",text="Student_Id")
        self.AttendenceReportTable.heading("studentname",text="Student_Name")
        self.AttendenceReportTable.heading("dep",text="Department")
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendence",text="Attendence")
        self.AttendenceReportTable["show"]="headings"

        self.AttendenceReportTable.column("id",width=100)
        self.AttendenceReportTable.column("studentId",width=100)
        self.AttendenceReportTable.column("studentname",width=100)
        self.AttendenceReportTable.column("dep",width=100)
        self.AttendenceReportTable.column("time",width=100)
        self.AttendenceReportTable.column("date",width=100)
        self.AttendenceReportTable.column("attendence",width=100)

        self.AttendenceReportTable.pack(fill=BOTH,expand=1)

        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)


    #============fetch data================
    def fetchData(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)

    # import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)

        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                    messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    def get_cursor(self, event=""):
        cursor_focus = self.AttendenceReportTable.focus()
        content = self.AttendenceReportTable.item(cursor_focus)
        rows = content['values']
        self.var_id.set(rows[0])
        self.var_student_id.set(rows[1])
        self.var_student_name.set(rows[2])
        self.var_dep.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_atten_attendence.set(rows[6])

        # Rest data
    def reset_data(self):
        self.var_id.set("")
        self.var_student_id.set("")
        self.var_student_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_atten_attendence.set("Status")


    def update_data(self):
        cursor_focus = self.AttendenceReportTable.focus()
        if not cursor_focus:
            messagebox.showerror("Error", "Please select a row to update", parent=self.root)
            return
        
        # Get the content of the selected row
        content = self.AttendenceReportTable.item(cursor_focus)
        rows = content['values']
        if not rows:
            messagebox.showerror("Error", "No data found to update", parent=self.root)
            return
        
        # Update the data based on the changes made
        rows = (
            self.var_id.get(),
            self.var_student_id.get(),
            self.var_student_name.get(),
            self.var_dep.get(),
            self.var_time.get(),
            self.var_date.get(),
            self.var_atten_attendence.get()
        )

        # Update the data in the mydata list
        index = self.AttendenceReportTable.index(cursor_focus)
        mydata[index] = rows

        # Rewrite the updated data to the CSV file
        try:
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for row in mydata:
                    exp_write.writerow(row)
            messagebox.showinfo("Data Updated", "Data updated successfully and saved to CSV file", parent=self.root)
            # Refresh the table to reflect the changes
            self.fetchData(mydata)
        except Exception as es:
            messagebox.showerror("Error", f"Error updating data: {str(es)}", parent=self.root)











if __name__=="__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()
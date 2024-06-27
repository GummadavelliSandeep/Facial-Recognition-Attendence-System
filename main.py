from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendence

class Face_Recogition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1830x790+0+0")
        self.root.title("face Recognition System")
        

        #first image
        img1=Image.open(r"C:\Users\DELL\OneDrive\Desktop\Face Recognition Attendence System\Images\front imageW.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_img=Label(self.root,image=self.photoimg1)
        f_img.place(x=30,y=0,width=500,height=130)

        #second image
        img2=Image.open(r"C:\Users\DELL\OneDrive\Desktop\Face Recognition Attendence System\Images\front image_All.jpg")
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
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM",font=("times new roman",35,"bold"),bg="White",fg="Black")
        title_lbl.place(x=-3,y=-3,width=1533,height=60)


        #student Button
        img5=Image.open(r"C:\Users\DELL\OneDrive\Desktop\Face Recognition Attendence System\Images\student Details.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(self.root,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=400,width=220,height=220)

        b1=Button(self.root,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b1.place(x=200,y=600,width=220,height=40)


        #Face Detect
        img6=Image.open(r"C:\Users\DELL\OneDrive\Desktop\Face Recognition Attendence System\Images\Detect face.jpg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b2=Button(self.root,image=self.photoimg6,cursor="hand2")
        b2.place(x=500,y=400,width=220,height=220)

        b2=Button(self.root,text="Face Detector", command=self.face_data,cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b2.place(x=500,y=600,width=220,height=40)


        #Train Data
        img7=Image.open(r"C:\Users\DELL\OneDrive\Desktop\Face Recognition Attendence System\images\Train Data.jpg")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b3=Button(self.root,image=self.photoimg7,cursor="hand2")
        b3.place(x=800,y=400,width=220,height=220)

        b3=Button(self.root,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b3.place(x=800,y=600,width=220,height=40)


        #Attendence
        img8=Image.open(r"C:\Users\DELL\OneDrive\Desktop\Face Recognition Attendence System\images\Attendence.jpg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b4=Button(self.root,image=self.photoimg8,cursor="hand2")
        b4.place(x=1100,y=400,width=220,height=220)

        b4=Button(self.root,text="Attendence", command=self.attendence_data,cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b4.place(x=1100,y=600,width=220,height=40)


# =========functions Buttons==========
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)


    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendence_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendence(self.new_window)






if __name__=="__main__":
    root=Tk()
    obj=Face_Recogition_System(root)
    root.mainloop()
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
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
        title_lbl=Label(bg_img,text="TRAIN DATASET",font=("times new roman",35,"bold"),bg="White",fg="green")
        title_lbl.place(x=-3,y=-3,width=1533,height=60)


        b1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="green",fg="white")
        b1.place(x=500,y=500,width=500,height=50)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]


        faces=[]
        ids=[]


        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        # ============Train the classifier and save=====
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!")



    








if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
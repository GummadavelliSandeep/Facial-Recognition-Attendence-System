from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognition:
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
        title_lbl=Label(bg_img,text="FACE DETECTOR",font=("times new roman",35,"bold"),bg="White",fg="green")
        title_lbl.place(x=-3,y=-3,width=1533,height=60)

        #Face Detector image
        img5=Image.open(r"C:\Users\DELL\OneDrive\Desktop\Face Recognition Attendence System\Images\Detect face Inside.jpg")
        img5=img5.resize((650,700),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        f_img=Label(bg_img,image=self.photoimg5)
        f_img.place(x=400,y=60,width=650,height=500)


        b1=Button(self.root,text="Face Detector",cursor="hand2",command=self.face_recog,font=("times new roman",30,"bold"),bg="green",fg="white")
        b1.place(x=500,y=700,width=500,height=50)



    #Mark Attendence
    #===========Attendence==================
    def mark_attendence(self,i,r,n,d):
        with open("attendence.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_List=[]
            for line in myDataList:
                entry=line.split((","))
                name_List.append(entry[0])
            if((i not in name_List)) and ((r not in name_List)) and ((n not in name_List)) and ((d not in name_List)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


    #face recognition
    
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeigbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeigbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="facial_recognition")
                my_cursor=conn.cursor()


                my_cursor.execute("select Student_Id from student where Student_Id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select Student_Name from student where Student_Id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Student_Id from student where Student_Id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_Id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                

                if confidence>77:
                    cv2.putText(img,f"Student_Id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Student_Id:{r}",(x,y-50),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Student_Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,h]

            return coord
            
        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")


        video_cap=cv2.VideoCapture(0)


        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()







    
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
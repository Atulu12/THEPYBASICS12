from tkinter import*
from tkinter.font import BOLD
import random
from tkinter import messagebox

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("LaMart(Bill)")
        self.root.geometry("1360x650+0+0")
        self.root.resizable(True,True)
        #===Frame===
        Frame_login=Frame(self.root,bg="Yellow")
        Frame_login.place(x=160,y=-100,height=3000,width=600)

        title=Label(Frame_login,text="Bill:",font=("Baskerville Old Face",30,BOLD),fg="red",bg="Yellow").place(x=60,y=40)
        desc=Label(Frame_login,text="Items:",font=("Javanese Text",20),fg="Brown",bg="Yellow").place(x=200,y=100)

        lbl_user=Label(Frame_login,text="Item 1:  Weight(opt)",font=("Times New Roman",20,BOLD),fg="Black",bg="Yellow",).place(x=70,y=160)
        self.txt_user=Entry(Frame_login,font=("Calibri",15),bg="Light Green")
        self.txt_user.place(x=70,y=200,width=350,height=35)

        lbl_user=Label(Frame_login,text="Item 2:  Weight(opt)",font=("Times New Roman",20,BOLD),fg="Black",bg="Yellow").place(x=70,y=260)
        self.txt_user=Entry(Frame_login,font=("Calibri",15),bg="Light Green")
        self.txt_user.place(x=70,y=300,width=350,height=35)
                 
        lbl_user=Label(Frame_login,text="Item 3:  Weight(opt)",font=("Times New Roman",20,BOLD),fg="Black",bg="Yellow").place(x=70,y=360)
        self.txt_user=Entry(Frame_login,font=("Calibri",15),bg="Light Green")
        self.txt_user.place(x=70,y=400,width=350,height=35)

        lbl_user=Label(Frame_login,text="Item 4:  Weight(opt)",font=("Times New Roman",20,BOLD),fg="Black",bg="Yellow").place(x=70,y=460)
        self.txt_user=Entry(Frame_login,font=("Calibri",15),bg="Light Green")
        self.txt_user.place(x=70,y=500,width=350,height=35)

        lbl_user=Label(Frame_login,text="Item 5:  Weight(opt)",font=("Times New Roman",20,BOLD),fg="Black",bg="Yellow").place(x=70,y=560)
        self.txt_user=Entry(Frame_login,font=("Calibri",15),bg="Light Green")
        self.txt_user.place(x=70,y=600,width=350,height=35)
   
        login_btn=Button(self.root,command=self.txt_user,text="Done",fg="White",bd=0,bg="Olive",font=("Algerian",20,"bold"),cursor="hand2").place(x=350,y=550)


        desc=Label(Frame_login,text="When done open Robot Verification App to finish by verifying or Login App to login",font=("Javanese Text",13),fg="Brown",bg="Yellow").place(x=-5,y=710)



        def login_btn(self):
         if self.txt_user.get()=="":
             messagebox.showinfo("Billing Done!,thankyou for visiting LaMart🙂 ",parent=self.root)
                  


        # set window size
        root.geometry("400x200")

        #set window color
        root['bg']='Orange'
    

        
         

root=Tk()
obj=Login(root)
root.mainloop()

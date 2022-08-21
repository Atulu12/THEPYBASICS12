from tkinter import*
from tkinter.font import BOLD
import random
from tkinter import messagebox
 
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Confirmation to Robot")
        self.root.geometry("1360x650+0+0")
        self.root.resizable(True,True)
        #===Frame===
        Frame_login=Frame(self.root,bg="Yellow")
        Frame_login.place(x=160,y=160,height=450,width=600)

        title=Label(Frame_login,text="ANSWER TO CONTINUE",font=("Baskerville Old Face",30,BOLD),fg="red",bg="Yellow").place(x=60,y=40)
        desc=Label(Frame_login,text="Enter Fields:",font=("Javanese Text",20),fg="Brown",bg="Yellow").place(x=200,y=100)

        lbl_user=Label(Frame_login,text="Problem:Type the number you can see on the Screen:",font=("Monotype Corsiva",20,BOLD),fg="Blue",bg="Yellow",).place(x=20,y=160)

        lbl_user=Label(Frame_login,text=random.randint(1000,10000),font=("Times New Roman",20,BOLD),fg="Black",bg="Yellow").place(x=70,y=200)
        self.txt_user=Entry(Frame_login,font=("Calibri",15),bg="Light Green")
        self.txt_user.place(x=70,y=250,width=350,height=35)

        login_btn=Button(self.root,command=self.txt_user,text="Done",fg="White",bd=0,bg="Olive",font=("Algerian",20,"bold"),cursor="hand2").place(x=350,y=550)       
        
        
       
        
        
        # set window size
        root.geometry("400x200")

        #set window color
        root['bg']='Orange'
    

        
         

root=Tk()
obj=Login(root)
root.mainloop()

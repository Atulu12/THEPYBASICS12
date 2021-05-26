from tkinter import*
from tkinter import messagebox
from tkinter.font import BOLD

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login.App")
        self.root.geometry("1360x650+0+0")
        self.root.resizable(True,True)
        #====login Frame=====
        Frame_login=Frame(self.root,bg="Grey")
        Frame_login.place(x=160,y=160,height=400,width=500)

        title=Label(Frame_login,text="LOGIN TO CONTINUE",font=("Baskerville Old Face",30,BOLD),fg="red",bg="Grey").place(x=20,y=40)
        desc=Label(Frame_login,text="Enter Fields:",font=("Javanese Text",20),fg="Blue",bg="Grey").place(x=170,y=100)

        lbl_user=Label(Frame_login,text="Email:",font=("Monotype Corsiva",20),fg="white",bg="Grey").place(x=70,y=160)
        self.txt_user=Entry(Frame_login,font=("Calibri",15),bg="Light Grey")
        self.txt_user.place(x=70,y=200,width=350,height=35)
         
        lbl_pass=Label(Frame_login,text="Password:",font=("Monotype Corsiva",20),fg="white",bg="Grey").place(x=70,y=250)
        self.txt_pass=Entry(Frame_login,font=("Calibri",15),bg="Light Grey")
        self.txt_pass.place(x=70,y=292,width=350,height=35)

        login_btn=Button(self.root,command=self.login_function,text="Login",fg="White",bd=0,bg="Olive",font=("Algerian",20,"bold"),cursor="hand2").place(x=350,y=500)
        
    def login_function(self):
         if self.txt_pass.get()==""or self.txt_user.get()=="":
             messagebox.showerror("Error","All Fields are needed",parent=self.root)
         elif self.txt_pass.get()!="1211"or self.txt_user.get()!="atulyapras@gmail.com":
             messagebox.showerror("Error","Invalid Answer",parent=self.root)
         else:messagebox.showinfo("Welcome","Welcome",parent=self.root)

root=Tk()
obj=Login(root) 
root.mainloop()

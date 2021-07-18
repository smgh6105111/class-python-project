from tkinter import*
import time as tm
from tkinter import ttk,messagebox
import time


class gh:
	def __init__(self,root):
		self.root=root
		self.root.geometry("450x700")
		self.root.config(bg="cadetblue")
		self.root.title('system')
		titleframe=Frame(self.root,bd=5,relief=RIDGE)
		titleframe.pack(side='top')
		lbltitle=Label(titleframe,text="Student Treeview Database",font="times 18 bold italic",padx=7)
		lbltitle.grid(row=0,column=0,columnspan=2)
		lblday=Label(titleframe,text="",font="times 10 bold italic")
		lblday.grid(row=1,column=0)
		lbltime=Label(titleframe,text="",font="times 10 bold italic")
		lbltime.grid(row=1,column=1)
		def displaytime():
			currenttime=tm.strftime('%H:%M:%S %p')
			lbltime['text']=currenttime
			root.after(200,displaytime)
			
		def displaydate():
			localtime=time.asctime(time.localtime(time.time()))
			lblday['text']=localtime
		displaytime()
		displaydate()
		#==================================
		infoframe=LabelFrame(self.root,text="student info",bg="cadetblue")
		infoframe.pack()
		self.lblname=Label(infoframe,text="Name",font="times 8 bold italic",bg="cadetblue")
		self.lblname.grid(row=0,column=0)
		self.enname=Entry(infoframe,font="times 8 bold italic")
		self.enname.grid(row=0,column=1)
		
		self.lblpass=Label(infoframe,text="Password",font="times 8 bold italic",bg="cadetblue")
		self.lblpass.grid(row=0,column=2)
		self.enpass=Entry(infoframe,font="times 8 bold italic",width=24)
		self.enpass.grid(row=0,column=3)
		
		self.lblemail=Label(infoframe,text="Email",font="times 8 bold italic",bg="cadetblue")
		self.lblemail.grid(row=1,column=0)
		self.enemail=Entry(infoframe,font="times 8 bold italic")
		self.enemail.grid(row=1,column=1)
		
		self.lbladdress=Label(infoframe,text="Address",font="times 8 bold italic",bg="cadetblue")
		self.lbladdress.grid(row=1,column=2)
		self.enaddress=Entry(infoframe,font="times 8 bold italic",width=24)
		self.enaddress.grid(row=1,column=3)
		
			
				
					
						
							
								
if __name__=='__main__':
	root=Tk()
	application=gh(root)
	root.mainloop()
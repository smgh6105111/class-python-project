from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import classdatabase




def exit():
    exit=messagebox.askyesno('Confirm to Exit','ARE YOU SURE?\nNOTICE:\nBe sure your work is saved')
    if exit > 0:
        root.destroy()
        return

def adddata():
	classdatabase.adddata(enuser.get(),enfirstname.get(),enlastname.get())
	list.delete(0,END)
	list.insert(END,(enuser.get(),enfirstname.get(),enlastname.get()))         
	
	                  
class gh:
    def __init__(self,root):
        self.root=root
        titlespace='  '
        self.root.title(20*titlespace+'PAYMENT SYSTEM WITH DATABASE')
        self.root.geometry('450x700')
        self.root.config(bg='green')
        self.lblf1=LabelFrame(self.root,text=('Personal Information'),width=440,height=300,bd=5,bg=('green'))
        global enuser
        enuser=StringVar()
        global enfirstname
        enfirstname=StringVar()
        global enlastname
        enlastname=StringVar()
        
        self.lblf1.pack()
        self.lblf2=LabelFrame(self.root,text=('BUTTON'),width=440,height=100,bd=5,bg=('green'))
        self.lblf2.pack()
        self.lblf3=LabelFrame(self.root,text=('VIEW INFORMATION'),width=440,height=300,bd=5,bg=('green'))
        self.lblf3.pack()
        self.lbluser=Label(self.lblf1,text=('User_id'),bg='green')
        self.lbluser.grid(row=0,column=0)
        self.enuser=Entry(self.lblf1,width=20,textvariable=enuser)
        self.enuser.grid(row=0,column=1)
        self.lblfirstname=Label(self.lblf1,text=('first_name'),                     bg='green')
        
        self.lblfirstname.grid(row=0,column=2)
        self.enfirstname=Entry(self.lblf1,width=16,textvariable=enfirstname)
        self.enfirstname.grid(row=0,column=3)
        
        self.lbllastname=Label(self.lblf1,text=('last_name'),                      bg='green')
        self.lbllastname.grid(row=1,column=0)
        self.enlastname=Entry(self.lblf1,width=20,textvariable=enlastname)
        self.enlastname.grid(row=1,column=1,pady=10)
        self.lblemail=Label(self.lblf1,text=('Email'),bg='green')
        self.lblemail.grid(row=1,column=2)
        self.enemail=Entry(self.lblf1,width=16)
        self.enemail.grid(row=1,column=3,pady=10)
        
        self.lbladdress=Label(self.lblf1,text=('address'),bg='green')
        self.lbladdress.grid(row=2,column=0)
        self.enaddress=Entry(self.lblf1,width=20)
        self.enaddress.grid(row=2,column=1)
        self.lblgender=Label(self.lblf1,text=('gender'),bg='green')
        self.lblgender.grid(row=2,column=2)
        self.combo=ttk.Combobox(self.lblf1,width=13)
        self.combo['values']=['male','female']
        self.combo.grid(row=2,column=3)
        
        self.lblcowork=Label(self.lblf1,text=('co_work'),bg='green')
        self.lblcowork.grid(row=3,column=0)
        self.encowork=Entry(self.lblf1,width=20)
        self.encowork.grid(row=3,column=1,pady=10)
        self.lblhourwork=Label(self.lblf1,text=('hour_work'),                      bg='green')
        self.lblhourwork.grid(row=3,column=2)
        self.enhourwork=Entry(self.lblf1,width=16)
        self.enhourwork.grid(row=3,column=3,pady=10)
        
        self.lblpayfor1=Label(self.lblf1,text=('pay_for_1'),bg='green')
        self.lblpayfor1.grid(row=4,column=0)
        self.enpayfor1=Entry(self.lblf1,width=20)
        self.enpayfor1.grid(row=4,column=1)
        self.lblpayhour=Label(self.lblf1,text=('pay_hour'),bg='green')
        self.lblpayhour.grid(row=4,column=2)
        self.enpayhour=Entry(self.lblf1,width=16)
        self.enpayhour.grid(row=4,column=3)
        
        self.lblpaygift=Label(self.lblf1,text=('pay_gift'),bg='green')
        self.lblpaygift.grid(row=5,column=0)
        self.enpaygift=Entry(self.lblf1,width=20)
        self.enpaygift.grid(row=5,column=1,pady=10)
        self.lbltax=Label(self.lblf1,text=('Tax'),bg='green')
        self.lbltax.grid(row=5,column=2)
        self.entax=Entry(self.lblf1,width=16)
        self.entax.grid(row=5,column=3,pady=10)
        
        self.lblpaywtax=Label(self.lblf1,text=('pay_w_tax'),                        bg='green')
        self.lblpaywtax.grid(row=6,column=0)
        self.enpaywtax=Entry(self.lblf1,width=20)
        self.enpaywtax.grid(row=6,column=1)
        self.lblaccount=Label(self.lblf1,text=('account'),bg='green')
        self.lblaccount.grid(row=6,column=2)
        self.enaccount=Entry(self.lblf1,width=16)
        self.enaccount.grid(row=6,column=3)
        #=====button======
        self.btnadd=Button(self.lblf2,text=('ADD'),width=5,height=1,command=adddata)
        self.btnadd.grid(row=0,column=0)
        
        self.btnsearch=Button(self.lblf2,text=('SEARCH'),width=5,            height=1)
        self.btnsearch.grid(row=0,column=1,padx=5)
        
        self.btnupdate=Button(self.lblf2,text=('UPDATE'),width=5,            height=1)
        self.btnupdate.grid(row=0,column=2)
        
        self.btndelete=Button(self.lblf2,text=('DELETE'),width=5,height=1)
        self.btndelete.grid(row=0,column=2)
        
        self.btndisplay=Button(self.lblf2,text=('DISPLAY'),width=3,height=1)
        self.btndisplay.grid(row=0,column=3,padx=5)
        
        self.btncal=Button(self.lblf2,text=('CAL'),width=4,height=1)
        self.btncal.grid(row=0,column=4)
        
        self.btnexit=Button(self.lblf2,text=('EXIT'),width=3,height=1,command=exit)
        self.btnexit.grid(row=0,column=5,padx=5)
        
           
        #======listbox&scrollbar======
        self.scroll=ttk.Scrollbar(self.lblf3)
        self.scroll.pack(side=RIGHT,fill=Y)


        self.scroll2=ttk.Scrollbar(self.lblf3,orient='horizontal')
        self.scroll2.pack(side='bottom',fill=X)

        self.list=Listbox(self.lblf3,height=50,width=50,                               yscrollcommand=self.scroll.set,xscrollcommand=self.                scroll2.set,bd=0)
        self.list.pack(fill='both')

        self.scroll.config(command=self.list.yview)
        self.scroll2.config(command=self.list.xview)
    
    
    
    
        
        
        
if __name__=='__main__':
    root=Tk()
    application=gh(root)
    root.mainloop()
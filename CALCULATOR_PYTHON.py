#GUI
import tkinter as tkr
app = tkr.Tk(__name__)
app.title('THE AAAA CALCULATOR')
app.geometry('300x400')

tkr.Label(app,text='***CALCULATOR***',font=('Times New Roman',15)).pack()
tkr.Label(app,text='ENTER FIRST NUMBER').place(x=20,y=50)
tkr.Label(app,text='ENTER SECOND NUMBER').place(x=150,y=50)
fv=tkr.Variable(app)
sv=tkr.Variable(app)
#ENTRY
tkr.Entry(app,textvariable=fv,width=7,font=('Times New Roman',20),fg='black',bg='pink').place(x=25,y=80)
tkr.Entry(app,textvariable=sv,width=7,font=('Times New Roman',20),fg='black',bg='pink').place(x=165,y=80)
#FUNCTION DEFINITION
def mysum():
    res.set(eval(fv.get()+'+'+sv.get()))
def mysub():
    res.set(eval(fv.get()+'-'+sv.get()))
def mymul():
    res.set(eval(fv.get()+'*'+sv.get()))
def mydiv():
    res.set(eval(fv.get()+'/'+sv.get()))      

#BUTTONS
tkr.Button(app,text="+",width=3,command=mysum,bg='grey',fg='white',font=(10)).place(x=25,y=200)
tkr.Button(app,text="-",width=3,command=mysub,bg='grey',fg='white',font=(10)).place(x=100,y=200)
tkr.Button(app,text="*",width=3,command=mymul,bg='grey',fg='white',font=(10)).place(x=175,y=200)
tkr.Button(app,text="/",width=3,command=mydiv,bg='grey',fg='white',font=(10)).place(x=250,y=200)
#RESULT
tkr.Label(app,text='RESULT',font=('Times New Roman',10)).place(x=25,y=300)
res=tkr.Variable(app)
res.set('0')
tkr.Entry(app,textvariable=res,width=7,font=('Times New Roman',15),fg='black',bg='pink').place(x=97,y=295)
app.mainloop()

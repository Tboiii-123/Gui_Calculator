from tkinter import *
root=Tk()

root.title('My calculator')

root.geometry('375x490')

menu=Menu(root)

root.config(menu=menu)
root.resizable(False,False)
submenu=Menu(menu)
def dark():
     root.config(bg='black')

def light():
     root.config(bg='white')

def red():
     root.config(bg='red')

def yellow():
     root.config(bg='yellow')

def green():
     root.config(bg='green')
     

def blue():
     root.config(bg='blue')
     
     

menu.add_cascade(label='Standard',menu=submenu)

submenu.add_command(label='Programmer')
submenu.add_command(label='Date Calculation')
submenu.add_command(label='Programmer')
submenu.add_command(label='Converter',font=('Helvetica',12))
submenu.add_command(label='Currency')
submenu.add_command(label='Volume')
submenu.add_command(label='Length')
submenu.add_command(label='About')



Mode=Menu(menu)

menu.add_cascade(label='Modes',menu=Mode)
Mode.add_command(label='Dark-Mode',command=dark)
Mode.add_command(label='Light-Mode',command=light)
Mode.add_command(label='Red-Mode',command=red)
Mode.add_command(label='Blue-Mode',command=blue)
Mode.add_command(label='Yellow-Mode',command=yellow)
Mode.add_command(label='Green-Mode',command=green)



#Function

equation=""
     
def show(value):
     global equation
     equation+=value
     Label_result.config(text=equation)

def clear():
     global equation
     equation=" "
     Label_result.config(text=equation)


def calculate():
     global equation
     result=""
     if equation !="" :
          try:
               result = eval(equation)
          except:
               result ="Syntax Error"
               equation=""
     Label_result.config(text=result)






Label_result=Label(root,width=30,height=1,text=" ",font=('arial',30))
Label_result.pack()


Button(root,text="C",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda: clear()).place(x=5,y=70)
Button(root,text="/",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="red",command=lambda: show('/')).place(x=95,y=70)
Button(root,text="%",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="yellow",command=lambda: show('%')).place(x=190,y=70)
Button(root,text="*",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="orange",command=lambda: show('*')).place(x=285,y=70)




Button(root,text="7",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda: show('7')).place(x=5,y=155)
Button(root,text="8",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="red",command=lambda: show('8')).place(x=95,y=155)
Button(root,text="9",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="yellow",command=lambda: show('9')).place(x=190,y=155)
Button(root,text="-",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="orange",command=lambda: show('-')).place(x=285,y=155)



Button(root,text="4",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda: show('4')).place(x=5,y=240)
Button(root,text="5",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="red",command=lambda: show('5')).place(x=95,y=240)
Button(root,text="6",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="yellow",command=lambda: show('6')).place(x=190,y=240)
Button(root,text="+",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="orange",command=lambda: show('+')).place(x=285,y=240)




Button(root,text="1",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda: show('1')).place(x=5,y=325)
Button(root,text="2",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="red",command=lambda: show('2')).place(x=95,y=325)
Button(root,text="3",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="yellow",command=lambda: show('3')).place(x=190,y=325)
Button(root,text="0",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="orange",command=lambda: show('0')).place(x=285,y=325)


Button(root,text=".",width=8,height=1,font=("arial",25,"bold"),bd=1,fg="#fff",bg="green",command=lambda: show('.')).place(x=10,y=412)
Button(root,text="=",width=8,height=1,font=("arial",25,"bold"),bd=1,fg="#fff",bg="green",command=lambda: calculate()).place(x=200,y=412)




root.mainloop()
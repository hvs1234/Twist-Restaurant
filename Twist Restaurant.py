#Libraries
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font

#Application Setup
root = Tk()
root.title("Twist Restaurant")
root.geometry("1000x500+200+100")
root.resizable(False,False)
root.configure(bg="light green")

#Functions
def delete():
    dosa_entry.delete(0,END)
    special_thali_entry.delete(0,END)
    momos_entry.delete(0,END)
    thali_entry.delete(0,END)
    samosa_entry.delete(0,END)
    kulhad_lassi_entry.delete(0,END)
    jalebi_fafda_entry.delete(0,END)
    malai_chaap_entry.delete(0,END)
    kadai_paneer_entry.delete(0,END)

def calculate():
    try: a1=int(dosa_entry.get())
    except: a1=0
    try: a2=int(special_thali_entry.get())
    except: a2=0
    try: a3=int(momos_entry.get())
    except: a3=0
    try: a4=int(thali_entry.get())
    except: a4=0
    try: a5=int(samosa_entry.get())
    except: a5=0
    try: a6=int(kulhad_lassi_entry.get())
    except: a6=0
    try: a7=int(jalebi_fafda_entry.get())
    except: a7=0
    try: a8=int(malai_chaap_entry.get())
    except: a8=0
    try: a9=int(kadai_paneer_entry.get())
    except: a9=0
    
    cal1 = 60*a1
    cal2 = 120*a2
    cal3 = 50*a3
    cal4 = 60*a4
    cal5 = 20*a5
    cal6 = 70*a6
    cal7 = 110*a7
    cal8 = 150*a8
    cal9 = 250*a9

    cost = cal1+cal2+cal3+cal4+cal5+cal6+cal7+cal8+cal9
    str_bill = "Rs.",str('%.2f' %cost)
    total_bill.set(str_bill)


def menu():
    global f1
    l1 = Label(f1,text="Dosa......Rs.60/Plate",fg="black",bg="light cyan"
    ,font=("Lucida Calligraphy",12,"bold")).place(x=10,y=80)
    l2 = Label(f1,text="Special Thali...Rs.120",fg="black",bg="light cyan"
    ,font=("Lucida Calligraphy",12,"bold")).place(x=10,y=110)
    l3 = Label(f1,text="Momos......Rs.50/Plate",fg="black",bg="light cyan"
    ,font=("Lucida Calligraphy",12,"bold")).place(x=10,y=140)
    l4 = Label(f1,text="Thali......Rs.60/Plate",fg="black",bg="light cyan"
    ,font=("Lucida Calligraphy",12,"bold")).place(x=10,y=170)
    l5 = Label(f1,text="Samosa......Rs.20/Plate",fg="black",bg="light cyan"
    ,font=("Lucida Calligraphy",12,"bold")).place(x=10,y=200)
    l6 = Label(f1,text="Kulhad Lassi......Rs.70",fg="black",bg="light cyan"
    ,font=("Lucida Calligraphy",12,"bold")).place(x=10,y=230)
    l7 = Label(f1,text="Jalebi Fafda...Rs.110",fg="black",bg="light cyan"
    ,font=("Lucida Calligraphy",12,"bold")).place(x=10,y=260)
    l8 = Label(f1,text="Malai Chaap...Rs.150",fg="black",bg="light cyan"
    ,font=("Lucida Calligraphy",12,"bold")).place(x=10,y=290)
    l9 = Label(f1,text="Kadai Paneer...Rs.250",fg="black",bg="light cyan"
    ,font=("Lucida Calligraphy",12,"bold")).place(x=10,y=320)

def set_menu():
    dosa = StringVar()
    Special_thali = StringVar()
    momos = StringVar()
    thali = StringVar()
    samosa = StringVar()
    kulhad_lassi = StringVar()
    jalebi_fafda = StringVar()
    malai_chaap = StringVar()
    kadai_paneer = StringVar()

    global dosa_entry; global special_thali_entry; global momos_entry; global thali_entry; 
    global samosa_entry; global kulhad_lassi_entry; global jalebi_fafda_entry; global malai_chaap_entry
    global kadai_paneer_entry
    
    dosa_label = Label(f2,text="Dosa",font=("Lucida Calligraphy",13,"bold"),width=12,fg="dark green",bg="light yellow")
    dosa_label.grid(row=1,column=0)
    dosa_entry = Entry(f2,font=("Lucida Calligraphy",13,"bold"),width=8,bd=6,
    bg="light pink",fg="purple",textvariable=dosa)
    dosa_entry.grid(row=1,column=1)
    
    special_thali_label = Label(f2,text="Special thali",font=("Lucida Calligraphy",13,"bold"),width=12,
    fg="dark green",bg="light yellow")
    special_thali_label.grid(row=2,column=0)
    special_thali_entry = Entry(f2,font=("Lucida Calligraphy",13,"bold"),width=8,bd=6,
    bg="light pink",fg="purple",textvariable=Special_thali)
    special_thali_entry.grid(row=2,column=1)
    
    momos_label = Label(f2,text="Momos",font=("Lucida Calligraphy",13,"bold"),width=12,fg="dark green",bg="light yellow")
    momos_label.grid(row=3,column=0)
    momos_entry = Entry(f2,font=("Lucida Calligraphy",13,"bold"),width=8,bd=6,
    bg="light pink",fg="purple",textvariable=momos)
    momos_entry.grid(row=3,column=1)
    
    thali_label = Label(f2,text="Thali",font=("Lucida Calligraphy",13,"bold"),width=12,fg="dark green",bg="light yellow")
    thali_label.grid(row=4,column=0)
    thali_entry = Entry(f2,font=("Lucida Calligraphy",13,"bold"),width=8,bd=6,
    bg="light pink",fg="purple",textvariable=thali)
    thali_entry.grid(row=4,column=1)
    
    samosa_label = Label(f2,text="Samosa",font=("Lucida Calligraphy",13,"bold"),width=12,fg="dark green",bg="light yellow")
    samosa_label.grid(row=5,column=0)
    samosa_entry = Entry(f2,font=("Lucida Calligraphy",13,"bold"),width=8,bd=6,
    bg="light pink",fg="purple",textvariable=samosa)
    samosa_entry.grid(row=5,column=1)
    
    kulhad_lassi_label = Label(f2,text="Kulhad Lassi",font=("Lucida Calligraphy",13,"bold"),width=12,
    fg="dark green",bg="light yellow")
    kulhad_lassi_label.grid(row=6,column=0)
    kulhad_lassi_entry = Entry(f2,font=("Lucida Calligraphy",13,"bold"),width=8,bd=6,
    bg="light pink",fg="purple",textvariable=kulhad_lassi)
    kulhad_lassi_entry.grid(row=6,column=1)
    
    jalebi_fafda_label = Label(f2,text="Jalebi Fafda",font=("Lucida Calligraphy",13,"bold"),
    width=12,fg="dark green",bg="light yellow")
    jalebi_fafda_label.grid(row=7,column=0)
    jalebi_fafda_entry = Entry(f2,font=("Lucida Calligraphy",13,"bold"),width=8,bd=6,
    bg="light pink",fg="purple",textvariable=jalebi_fafda)
    jalebi_fafda_entry.grid(row=7,column=1)
    
    malai_chaap_label = Label(f2,text="Malai Chaap",font=("Lucida Calligraphy",13,"bold"),width=12,
    fg="dark green",bg="light yellow")
    malai_chaap_label.grid(row=8,column=0)
    malai_chaap_entry = Entry(f2,font=("Lucida Calligraphy",13,"bold"),width=8,bd=6,
    bg="light pink",fg="purple",textvariable=malai_chaap)
    malai_chaap_entry.grid(row=8,column=1)
    
    kadai_paneer_label = Label(f2,text="Kadai Paneer",font=("Lucida Calligraphy",13,"bold"),width=12,
    fg="dark green",bg="light yellow")
    kadai_paneer_label.grid(row=9,column=0)
    kadai_paneer_entry = Entry(f2,font=("Lucida Calligraphy",13,"bold"),width=8,bd=6,
    bg="light pink",fg="purple",textvariable=kadai_paneer)
    kadai_paneer_entry.grid(row=9,column=1)

    btn1 = Button(f2,text=".",borderwidth=0,height=0,font="arial 15 bold",
    bg="light yellow",fg="black",activebackground="light yellow",
    activeforeground="black",command=delete)
    btn1.grid(row=1,column=2)
    btn2 = Button(f2,text=".",borderwidth=0,height=0,font="arial 15 bold",
    bg="light yellow",fg="black",activebackground="light yellow",
    activeforeground="black",command=delete)
    btn2.grid(row=2,column=2)
    btn3 = Button(f2,text=".",borderwidth=0,height=0,font="arial 15 bold",
    bg="light yellow",fg="black",activebackground="light yellow",
    activeforeground="black",command=delete)
    btn3.grid(row=3,column=2)
    btn4 = Button(f2,text=".",borderwidth=0,height=0,font="arial 15 bold",
    bg="light yellow",fg="black",activebackground="light yellow",
    activeforeground="black",command=delete)
    btn4.grid(row=4,column=2)
    btn5 = Button(f2,text=".",borderwidth=0,height=0,font="arial 15 bold",
    bg="light yellow",fg="black",activebackground="light yellow",
    activeforeground="black",command=delete)
    btn5.grid(row=5,column=2)
    btn6 = Button(f2,text=".",borderwidth=0,height=0,font="arial 15 bold",
    bg="light yellow",fg="black",activebackground="light yellow",
    activeforeground="black",command=delete)
    btn6.grid(row=6,column=2)
    btn7 = Button(f2,text=".",borderwidth=0,height=0,font="arial 15 bold",
    bg="light yellow",fg="black",activebackground="light yellow",
    activeforeground="black",command=delete)
    btn7.grid(row=7,column=2)
    btn8 = Button(f2,text=".",borderwidth=0,height=0,font="arial 15 bold",
    bg="light yellow",fg="black",activebackground="light yellow",
    activeforeground="black",command=delete)
    btn8.grid(row=8,column=2)
    btn9 = Button(f2,text=".",borderwidth=0,height=0,font="arial 15 bold",
    bg="light yellow",fg="black",activebackground="light yellow",
    activeforeground="black",command=delete)
    btn9.grid(row=9,column=2)

    total = Button(f2,text="Total",bg="light yellow",fg="dark blue",borderwidth=0,height=0,
    font=Font(weight="bold"),activebackground="light yellow",activeforeground="dark blue",command=calculate)
    total.grid(row=10,column=1)
    
def bill_system():
    global total_bill
    total_bill = StringVar()
    bill = Label(f3,text="BILL",fg="indigo",bg="light grey",font="Algerian 30 bold underline")
    bill.place(x=100,y=10)
    l1 = Label(f3,text="Total",bg="black",fg="white",font="Algerian 20 bold",width=15)
    l1.place(x=3,y=70)
    e1 = Entry(f3,textvariable=total_bill,font="Arial 20 bold",bd=6,
    width=15,bg="light yellow",fg="dark blue")
    e1.place(x=23,y=120); e1.config(state='readonly',bg="light yellow",fg="dark blue")
    l2 = Label(f3,text="Signed by\ntwist Restaurant",font="Gabriola 25 bold",fg="dark green",bg="light grey")
    l2.place(x=43,y=200)

#Application Creation
img1 = PhotoImage(file="E:\\pyImages\\cafe logo.png")
root.iconphoto(False,img1)
l1 = Label(root,text="Twist Restaurant",width=300,height=2,fg="white",bg="black",font="Algerian 33 bold")
l1.pack()
f1 = Frame(root,bg="light cyan",highlightbackground="black",highlightthickness=2,width=300,height=370,
           bd=6,relief=RAISED)
f1.place(x=10,y=118)

l2 = Label(f1,text="Menu",font="Gabriola 35 bold underline",fg="black",bg="light cyan")
l2.place(x=80,y=0)
menu()

f2 = Frame(root,bd=5,highlightbackground="black",highlightthickness=2,bg="light yellow",
           width=300,height=370,relief=RAISED)
f2.place(x=340,y=110)
f3 = Frame(root,bd=5,highlightbackground="black",highlightthickness=2,bg="light grey",
           width=300,height=370,relief=RAISED)
f3.place(x=670,y=115)

set_menu()
bill_system()
root.mainloop()
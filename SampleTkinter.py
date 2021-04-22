from tkinter import *

window = Tk()

def convertKg():
    #Value Calculation
    grams=float(e1Value.get()) * 1000
    pounds=float(e1Value.get()) * 2.20462
    ounces=float(e1Value.get()) * 35.274

    #Value Insertion
    t1.insert(END, grams)
    t2.insert(END, pounds)
    t3.insert(END, ounces)


labelValue = StringVar()
labelValue.set("Kg")
 
label = Label(window, textvariable = labelValue)
label.grid(row=0, column = 0)

e1Value=StringVar()
e1=Entry(window,textvariable=e1Value)#Entry element
e1.grid(row=0, column=1)

b1=Button(window, text="Convert", command=convertKg)
b1.grid(row=0, column=2) #Add Button

#Text Elements
t1= Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2=Text(window, height=1, width=20 )
t2.grid(row=1, column=1)

t3=Text(window, height=1, width=20 )
t3.grid(row=1, column=2)
window.mainloop()
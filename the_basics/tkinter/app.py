from tkinter import *

window = Tk()

def km_to_milles():
    try:
        grms = float(k_entry_value.get()) * 1000
        pounds = float(k_entry_value.get()) *  2.20462
        ounces = float(k_entry_value.get()) *  35.274
        text_grms.delete('1.0',END)# Deletes the content of the Text box from start to END
        text_grms.insert(END,grms)
        text_pounds.delete('1.0',END)
        text_pounds.insert(END,pounds)
        text_ounces.delete('1.0',END)
        text_ounces.insert(END,ounces)
    except ValueError:
        print("You can use numbers only")
    


kg_lable = Label(window,text="Kg")
kg_lable.grid(row = 0,column = 0)


k_entry_value = StringVar()
k_entry = Entry(window,textvariable= k_entry_value)
k_entry.grid(row=0,column=1)


b_convert = Button(window,text= 'Convert',command= km_to_milles)
b_convert.grid(row=0,column=2)


text_grms = Text(window,height = 1,width = 20)
text_grms.grid(row = 1,column = 0)

text_pounds = Text(window,height = 1,width = 20)
text_pounds.grid(row = 1,column = 1)

text_ounces = Text(window,height = 1,width = 20)
text_ounces.grid(row = 1,column = 2)

window.mainloop()




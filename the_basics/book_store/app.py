from tkinter import *
import backend



def view_command():
    books = backend.get_data()
    listbox.delete(0,END)
    for book in books:
       listbox.insert(END,book) 
       
def search_command():
    books = backend.search(title=title.get(),author=author.get(),year=year.get(),isbn=isbn.get())
    listbox.delete(0,END)
    for book in books:
        listbox.insert(END,book) 
    
def add_command():
    backend.insert(title=title.get(),author=author.get(),year=year.get(),isbn=isbn.get())
    listbox.delete(0,END)
    listbox.insert(END,(title.get(),author.get(),year.get(),isbn.get())) 
    
def get_selected_row(event):
    global selected_tuple
    if len(listbox.curselection()) > 0:
        index = listbox.curselection()[0] #(index,) the return is a tuple so we get [0]
        selected_tuple = listbox.get(index)
        set_values_of_selected_book()
        return selected_tuple
    
def delete_command():
    id = selected_tuple[0]
    backend.delete(id)
    view_command()

def update_command():
    backend.update(id=selected_tuple[0],title=title.get(),author=author.get(),year=year.get(),isbn=isbn.get())
    listbox.delete(0,END)
    view_command()

def set_values_of_selected_book():
    titl_entry.delete(0,END)
    titl_entry.insert(END,selected_tuple[1]) 
    
    author_entry.delete(0,END)
    author_entry.insert(END,selected_tuple[2]) 
    
    year_entry.delete(0,END)
    year_entry.insert(END,selected_tuple[3]) 
    
    isbn_entry.delete(0,END)
    isbn_entry.insert(END,selected_tuple[4]) 


# Prepare the Window
window = Tk()
window.wm_title("BookStore")

################################## Row 0 ################################################
lable_title = Label(window,text="Title")
lable_title.grid(row = 0,column = 0)


title = StringVar()
titl_entry = Entry(window,textvariable= title)
titl_entry.grid(row=0,column=1)

lable_author = Label(window,text="Author")
lable_author.grid(row = 0,column =2)

author = StringVar()
author_entry = Entry(window,textvariable= author)
author_entry.grid(row=0,column=3,padx=3)


################################## Row 1 ################################################
lable_year = Label(window,text="Year")
lable_year.grid(row = 1,column = 0)


year = StringVar()
year_entry = Entry(window,textvariable= year)
year_entry.grid(row=1,column=1)

lable_isbn = Label(window,text="ISBN")
lable_isbn.grid(row = 1,column =2)

isbn = StringVar()
isbn_entry = Entry(window,textvariable= isbn)
isbn_entry.grid(row=1,column=3,padx=3)


################################## Row 2 ################################################
b_viewAll = Button(window,text= 'View ALL',command= view_command)
b_viewAll.grid(row=2,column=3,columnspan=1,sticky=NSEW,padx=5)

listbox = Listbox(window,width=35,height=6)
listbox.grid(row=2,column=0,columnspan=2,rowspan=6,padx=3)

sb = Scrollbar(window)
sb.grid(row=2, column=2,rowspan=6)

listbox.configure(yscrollcommand=sb.set)
sb.configure(command= listbox.yview)

listbox.bind('<<ListboxSelect>>',get_selected_row)

################################## Row 3 ################################################
btn_search = Button(window,text= 'Search Entry',command= search_command)
btn_search.grid(row=3,column=3,columnspan=1,sticky=NSEW,padx=5)


################################## Row 4 ################################################
btn_add = Button(window,text= 'Add Entry',command= add_command)
btn_add.grid(row=4,column=3,columnspan=1,sticky=NSEW,padx=5)


################################## Row 5 ################################################
btn_update = Button(window,text= 'Update Selected',command=update_command)
btn_update.grid(row=5,column=3,columnspan=1,sticky=NSEW,padx=5)


################################## Row 6 ################################################
btn_delete = Button(window,text= 'Delete Selected',command= delete_command)
btn_delete.grid(row=6,column=3,columnspan=1,sticky=NSEW,padx=5)


################################## Row 7 ################################################
btn_close = Button(window,text= 'Close',command= backend.close)
btn_close.grid(row=7,column=3,columnspan=1,sticky=NSEW,padx=5)

window.mainloop()




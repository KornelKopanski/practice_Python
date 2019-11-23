
from tkinter import *
from tkinter import ttk
from datetime import *

class Wi(Frame):

    def __init__(self,master):

        super(Wi,self).__init__(master)
        self.grid()
        self.create_label()
        self.create_entry()
        self.create_combobox()

    def create_label(self):

        self.city = Label(self,text="Miasto")
        self.city.grid(row=0,column=0)
        self.name_company = Label(self,text="Nazwa firmy")
        self.name_company.grid(row=1,column=0)
        self.site_company = Label(self,text="Strona WWW")
        self.site_company.grid(row=2,column=0)
        self.status = Label(self,text = "Status")
        self.status.grid(row=3,column=0)
        self.post_date = Label(self,text="Data aplikacji")
        self.post_date.grid(row=4,column=0)
        self.post_date_info = Label(self, text=str(date.today()), bg="white")
        self.post_date_info.grid(row=4, column=1)
        self.description = Label(self,text="Uwagi")
        self.description.grid(row=5,column=0)

    def create_combobox(self):
        self.category_combobox = ttk.Combobox(self, values=["Lublin", "Warszawa"])
        self.category_combobox.current(0)
        self.category_combobox.grid(row=0, column=1)
        self.status_combobox = ttk.Combobox(self,values=["Do wysłania","Wysłane","Feedback Positive","Feedback Negative"])
        self.status_combobox.current(0)
        self.status_combobox.grid(row=3,column=1)

    def create_entry(self):

        self.name_company_entry = Entry(self)
        self.name_company_entry.grid(row=1,column=1)
        self.site_company_entry = Entry(self)
        self.site_company_entry.grid(row=2,column=1)
        self.description_entry = Entry(self)
        self.description_entry.grid(row=5,column=1)






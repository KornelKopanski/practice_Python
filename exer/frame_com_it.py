
from tkinter import *

class Wi(Frame):

    def __init__(self,master):

        super(Wi,self).__init__(master)
        self.grid()
        self.create_label()
        self.create_entry()
        self.create_button()

    def create_label(self):


        self.site_company = Label(self,text="Strona WWW")
        self.site_company.grid(row=0,column=0)

        self.description = Label(self,text="Uwagi")
        self.description.grid(row=1,column=0)

    def create_entry(self):


        self.site_company_entry = Entry(self,width = 33)
        self.site_company_entry.grid(row=0,column=1)

        self.description_entry = Text(self,width = 25, height = 10)
        self.description_entry.grid(row=1,column=1)

    def create_button(self):

        self.save = Button(self,text="Zapisz dane", width = 25)
        self.save.grid(row=2,column=1)

        self.save = Button(self, text="Pokaż dane", width = 25)
        self.save.grid(row=3, column=1)






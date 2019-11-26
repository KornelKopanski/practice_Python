

from tkinter import *
from tkinter import ttk

class IW(Frame):

    def __init__(self,master):

        super(IW,self).__init__(master)
        self.grid()
        self.create_label()
        self.create_button()
        self.create_listbox()
        self.create_combobox()

    def create_label(self):

        self.company = Label(self,text="FIRMY")
        self.company.grid(row=0,column=0,columnspan=4)

    def create_listbox(self):



        self.listbox_frame = Frame(self)
        self.listbox_frame.grid(row=1,column=0,columnspan=4)

        scrollbar_product_window = Scrollbar(self.listbox_frame)

        self.main_products_window = Listbox(self.listbox_frame,width=57,height = 20,
                                            yscrollcommand=scrollbar_product_window.set)
        self.main_products_window.pack(side=LEFT, fill=BOTH)

        scrollbar_product_window.pack(side=RIGHT, fill=Y)
        scrollbar_product_window.config(command=self.main_products_window.yview)




    def create_combobox(self):

        self.category_combobox = ttk.Combobox(self, values=["Do wysłania","Wysłane","Feedback Positive","Feedback Negative"],width = 30)
        self.category_combobox.current(0)
        self.category_combobox.grid(row=3, column=0,columnspan=4)

    def create_button(self):
        self.ch_status = Button(self, text="Zmień status",width = 27)
        self.ch_status.grid(row=4, column=0, columnspan=4)

        self.exit = Button(self,text="Zamknij",command=self.master.destroy,width = 27)
        self.exit.grid(row=5,column=0,columnspan=4)

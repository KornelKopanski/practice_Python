
from exer.save_data import *
from exer.info_window import *
from tkinter.messagebox import *

class Wi(Frame):

    def __init__(self,master):

        super(Wi,self).__init__(master)
        self.grid()
        self.create_label()
        self.create_entry()
        self.create_button()
        self.create_combobox()

    def create_label(self):

        self.site_company = Label(self,text="Strona WWW")
        self.site_company.grid(row=1,column=0)

        self.description = Label(self,text="Uwagi")
        self.description.grid(row=2,column=0)

        self.city = Label(self,text="Miasto")
        self.city.grid(row=0,column=0)

        self.status = Label(self,text="Status")
        self.status.grid(row=3,column=0)

    def create_entry(self):


        self.site_company_entry = Entry(self,width = 33)
        self.site_company_entry.grid(row=1,column=1)

        self.description_entry = Text(self,width = 25, height = 10)
        self.description_entry.grid(row=2,column=1)

    def create_combobox(self):

        self.city_combobox = ttk.Combobox(self, values=["Lublin", "Warszawa"],width = 30)
        self.city_combobox.current(0)
        self.city_combobox.grid(row=0, column=1)
        self.status_combobox = ttk.Combobox(self,values=["Do wysłania","Wysłane","Feedback Positive","Feedback Negative"],width = 30)
        self.status_combobox.current(0)
        self.status_combobox.grid(row=3,column=1)

    def get_data(self):

        city = self.city_combobox.get()
        status = self.status_combobox.get()
        site = self.site_company_entry.get()
        description = self.description_entry.get("1.0",END)

        if site:
            save_data = SaveData()
            save_data.savedata(city, status, site, description)
        else:
            showinfo("Uwaga","Proszę wpisać stronę 'WWW' danej firmy!")

    def create_button(self):

        self.save = Button(self,text="DODAJ FIRMĘ", width = 25,command=self.get_data)
        self.save.grid(row=4,column=1)

        show_info_company = Info_Window()

        self.save = Button(self, text="POKAŻ FIRMY", width = 25, command =show_info_company.main_product_window )
        self.save.grid(row=5, column=1)

        self.save = Button(self, text="ZAMKNIJ", width=25, command=self.master.destroy)
        self.save.grid(row=6, column=1)







import json
from tkinter.messagebox import *

class SaveData:

    _all_data = []

    def __init__(self):

        self._read()

    def _read(self):

        with open("data.json", "r")  as my_file:
            x = json.load(my_file)

    def _write(self):

        with open("data.json", "w")  as my_file:
            json.dump(self._all_data, my_file, indent=2)

    def savedata(self,city,status,site,description,date):

        test = []

        for info in self._all_data:
            for item in info:
                if item == "site":
                    test.append(info[item])

        if site not in test:
            i = {}
            i["city"] = city
            i["status"] = status
            i["site"] = site
            i["date"] = date
            if description != '\n':
                i["description"] = description
            else:
                i["description"] = "Brak uwag"

            self._all_data.append(i)

            self._write()
        else:
            showinfo("Uwaga!","Dana firma istnieje już w bazie!")









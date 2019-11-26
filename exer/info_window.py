
from exer.info_frame import *

class Info_Window:


    def main_product_window(self):

        self.root_two = Tk()
        self.root_two.title("DANE O FIRMACH")
        self.root_two.geometry("365x430")

        frame_info_window = IW(self.root_two)

        self.root_two.mainloop()



from tkinter import *

class HairBookingApp:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title("Hair Booking App")
        self.main_window.geometry("500x400")


        self.name_var = StringVar()
        self.service_var = StringVar()

        Label(self.main_window, text="Name").pack()
        Entry(self.main_window, textvariable=self.name_var).pack()

        Label(self.main_window, text="Service").pack()
        self.service_menu = OptionMenu(self.main_window, self.service_var, "Haircut", "Colour", "Blow Dry")
        self.service_menu.pack()


        self.listbox = Listbox(self.main_window, width=50)
        self.listbox.pack(pady=20)

        
        bookings = ["SANDRA - Haircut", "EMMANUEL - Colour"]

        for b in bookings:
            self.listbox.insert(END, b)

        mainloop()

def main():
    app = HairBookingApp()

if __name__ == '__main__': 
    main()

       self.wash_var = IntVar()
       self.payment_var = StringVar()
       self.rating_var = IntVar()
    

       Checkbutton(self.main_window, text="Include Wash", variable=self.wash_var).pack()
       Label(self.main_window, text="Payment").pack()
       Radiobutton(self.main_window, text="Cash", variable=self.payment_var, value="Cash").pack()
       Radiobutton(self.main_window, text="Card", variable=self.payment_var, value="Card").pack()

       Label(self.main_window, text="Rating").pack()
       Scale(self.main_window, from_=1, to=10, orient=HORIZONTAL, variable=self.rating_var).pack()



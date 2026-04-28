
from tkinter import *

class HairBookingApp:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title("Hair Booking App")
        self.main_window.geometry("500x400")

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
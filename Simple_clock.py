import tkinter as tk
import time

class MinimalClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Minimal Clock')
        self.geometry('200x80')
        self.configure(bg='black')
        self.resizable(False, False)
        self.label = tk.Label(self, font=('Consolas', 32), fg='white', bg='black')
        self.label.pack(expand=True)
        self.update_clock()

    def update_clock(self):
        now = time.strftime('%H:%M:%S')
        self.label.config(text=now)
        self.after(1000, self.update_clock)

if __name__ == '__main__':
    MinimalClock().mainloop()
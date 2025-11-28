import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")  # فرمت ساعت
    label.config(text=current_time)  # به‌روزرسانی متن برچسب
    label.after(1000, update_time)  # به‌روزرسانی هر ۱۰۰۰ میلی‌ثانیه (۱ ثانیه)

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("ساعت دیجیتال")

# ایجاد برچسب برای نمایش ساعت
label = tk.Label(root, font=("Helvetica", 48), fg="black")
label.pack()

update_time()  # فراخوانی تابع به‌روزرسانی ساعت

# اجرای حلقه اصلی
root.mainloop()
#Produce by AmirHossein Taghizadeh
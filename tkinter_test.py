import tkinter as tk
from tkinter import messagebox as mb

window = tk.Tk()
window.title("window 10")

rate = tk.DoubleVar()
rate.set(75.96)
rate_1 = tk.DoubleVar()
rate_1.set(1)
    
selected = 75
main_frame = tk.Frame(window, padx=20, pady=20)
my_label2 = tk.Label(main_frame, text="введите сумму")
my_input1 = tk.Entry(main_frame, width=50)
my_label4 = tk.Label(main_frame, text="валюта в которой вводите")
my_radio1 = tk.Radiobutton(main_frame,text="USD", value = 75.96, variable=rate)
my_radio2 = tk.Radiobutton(main_frame,text="EUR", value = 86.01, variable=rate)
my_radio3 = tk.Radiobutton(main_frame,text="BTC", value = 2926121.62, variable=rate)
my_radio4 = tk.Radiobutton(main_frame, text="RUB", value= 1, variable=rate)
my_label5 = tk.Label(main_frame, text="валюта в которой хотите получить")
my_radio5 = tk.Radiobutton(main_frame, text="USD", value = 75.96, variable=rate_1)
my_radio6 = tk.Radiobutton(main_frame, text="EUR", value = 86.01, variable=rate_1)
my_radio7 = tk.Radiobutton(main_frame, text="BTC", value = 2926121.62, variable=rate_1)
my_radio8 = tk.Radiobutton(main_frame, text="RUB", value = 1, variable=rate_1)
my_button = tk.Button(main_frame, text="получить результат", command= lambda: calculate_currency(rate, rate_1))
my_label3 = tk.Label(main_frame)
main_frame.pack()
my_label2.grid(column=1, row=0)
my_input1.grid(column=1, row=2)
my_radio1.grid(column=4, row=4)
my_radio2.grid(column=4, row=5)
my_radio3.grid(column=4, row=6)
my_radio4.grid(column=4, row=7)
my_label4.grid(column=1, row=3)
my_radio5.grid(column=1, row=4)
my_radio6.grid(column=1, row=5)
my_radio7.grid(column=1, row=6)
my_radio8.grid(column=1, row=7)
my_label5.grid(column=4, row=3)
my_button.grid(column=2, row=8)
my_label3.grid(column=4, row=2)



def calculate_currency(rate, rate_1):
    try:
        int(my_input1.get())
    except ValueError:
        mb.showwarning("Ошибка", "Введите сумму целым числом")
        my_input1.delete(0, 'end')
    else:
        entr_rate = round(int(my_input1.get()) * rate_1.get(), 2)
        result_1 = round(int(entr_rate) / rate.get(), 2)
        my_label3.config(text=result_1)


main_frame.mainloop()



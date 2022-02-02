import tkinter as tk

window = tk.Tk()
window.title("Windows 10")
window.geometry("800x600")

rate = tk.DoubleVar()
rate.set(75.96)
	
selected = 75
my_label2 = tk.Label(window, text="введите сумму в рублях")
my_input1 = tk.Entry(window, width=50)
my_radio1 = tk.Radiobutton(window,text="USD", value = 75.96, variable=rate)
my_radio2 = tk.Radiobutton(window,text="EUR", value = 86.01, variable=rate)
my_radio3 = tk.Radiobutton(window,text="BTC", value = 2926121.62, variable=rate)
my_button = tk.Button(window, text="получить результат", command= lambda: calculate_currency(rate))
my_label3 = tk.Label(window)

my_label2.pack()
my_input1.pack()
my_radio1.pack()
my_radio2.pack()
my_radio3.pack()
my_button.pack()
my_label3.pack()

def calculate_currency(rate):
	result = round(int(my_input1.get()) / rate.get(), 2)
	my_label3.config(text=result)


window.mainloop()

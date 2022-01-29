import tkinter as tk

window = tk.Tk()
window.title("Windows 10")
window.geometry("800x600")

def change_label_text():
	l1 = tk.Label(window, text=i1.get())
	l1.pack()

i1 = tk.Entry(window, width=50)
b1 = tk.Button(window, text="1", command=change_label_text)
b2 = tk.Button(window, text="2", command=change_label_text)
b3 = tk.Button(window, text="3", command=change_label_text)
b4 = tk.Button(window, text="4", command=change_label_text)
b5 = tk.Button(window, text="5", command=change_label_text)
b6 = tk.Button(window, text="6", command=change_label_text)
b7 = tk.Button(window, text="7", command=change_label_text)
b8 = tk.Button(window, text="8", command=change_label_text)
b9 = tk.Button(window, text="9", command=change_label_text)
b0 = tk.Button(window, text="0", command=change_label_text)
b10 = tk.Button(window, text="получить результат", command=change_label_text)
b1.grid(row=1,column=1, padx=50, pady=0)
b2.grid(row=1,column=2, padx=50, pady=0)
b3.grid(row=1,column=3, padx=50, pady=0)
b4.grid(row=2,column=1, padx=50, pady=0)
b5.grid(row=2,column=2, padx=50, pady=0)
b6.grid(row=2,column=3, padx=50, pady=0)
b7.grid(row=3,column=1, padx=50, pady=0)
b8.grid(row=3,column=2, padx=50, pady=0)
b9.grid(row=3,column=3, padx=50, pady=0)
b0.grid(row=4,column=2, padx=50, pady=0)
b10.grid(row=5,column=2, padx=50, pady=0)
i1.grid(row=8, column= 2, padx=50, pady=0)




window.mainloop()

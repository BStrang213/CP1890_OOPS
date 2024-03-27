import tkinter as tk
from tkinter import ttk, messagebox

from future_value_Arun import future_value

window = tk.Tk()
window.title("Future Value Calculator")
window.geometry("400x400")

frame = ttk.Frame(window, padding="10 10 10 10")
frame.pack(fill="both", expand=True)


def button1():
    month = invest_text.get()
    if month:
        month = int(month)
    else:
        messagebox.showerror("Error", "there is no month!")
    year = yearly_text.get()
    if year:
        year = int(year)
    else:
        messagebox.showerror("Error", "there is no yearly percent!")
    years = years_text.get()
    if years:
        years = int(years)
    else:
        messagebox.showerror("Error", "no years inputted!")
    amount = future_value(month, year, years)
    fut_text.set(str(amount))


def button2():
    window.destroy()


invest_input = ttk.Label(frame, text="Monthly Investment:")
invest_input.grid(column=0, row=0, sticky=tk.E)
invest_text = tk.StringVar()
invest_entry = ttk.Entry(frame, width=25, textvariable=invest_text)
invest_entry.grid(column=1, row=0, sticky=tk.E)

yearly = ttk.Label(frame, text="Yearly Interest Rate:")
yearly.grid(column=0, row=1, sticky=tk.E)
yearly_text = tk.StringVar()
yearly_entry = ttk.Entry(frame, width=25, textvariable=yearly_text)
yearly_entry.grid(column=1, row=1, sticky=tk.E)

years_input = ttk.Label(frame, text="Years:")
years_input.grid(column=0, row=2, sticky=tk.E)
years_text = tk.StringVar()
years_entry = ttk.Entry(frame, width=25, textvariable=years_text)
years_entry.grid(column=1, row=2, sticky=tk.E)

fut_val = ttk.Label(frame, text="Future Value:")
fut_val.grid(column=0, row=3, sticky=tk.E)
fut_text = tk.StringVar()
fut_entry = ttk.Entry(frame, width=25, textvariable=fut_text, state="readonly")
fut_entry.grid(column=1, row=3, sticky=tk.E)

button1 = ttk.Button(frame, text="Calculate", command=button1)
button1.grid(column=1, row=4, sticky=tk.W)

button2 = ttk.Button(frame, text="Exit", command=button2)
button2.grid(column=1, row=4, sticky=tk.E)

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=3)

window.mainloop()

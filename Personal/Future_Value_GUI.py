from future_value_Arun import future_value
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Future Value Calculator")
window.geometry("400x400")

frame = ttk.Frame(window, padding="10 10 10 10")
frame.pack(fill="both", expand=True)

# def Clicked_button1():

invest_input = ttk.Label(frame, text="Monthly Investment")
invest_input.grid(column=0, row=0, sticky=tk.E)
invest_text = tk.StringVar()
invest_entry = ttk.Entry(frame, width=25, textvariable=invest_text)
invest_entry.grid(column=1, row=0, sticky=tk.E)

yearly = ttk.Label(frame, text="Yearly Interest Rate")
yearly.grid(column=0, row=1)
yearly_text = tk.StringVar()
yearly_entry = ttk.Entry(frame, width=25, textvariable=yearly_text)
yearly_entry.grid(column=1, row=1, sticky=tk.E)

years_input = ttk.Label(frame, text="Years")
years_text = tk.StringVar()
years_entry = ttk.Entry(frame, width=25, textvariable=years_text)
years_entry.grid(column=1, row=2, sticky=tk.E)

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=3)

window.mainloop()
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Player")
window.geometry("400x250")

frame = ttk.Frame(window, padding="10 10 10 10")
frame.pack(fill="both", expand=True)


def Button_1():
    play = player_text.get()


def Button_2():
    print("place Holder")


def Button_3():
    window.destroy()


player = ttk.Label(frame, text="Player ID:")
player.grid(column=0, row=0, sticky=tk.E)
player_text = tk.StringVar()
player_entry = ttk.Entry(frame, width=26, textvariable=player_text)
player_entry.grid(column=1, row=0, sticky=tk.E)

First = ttk.Label(frame, text="First Name:")
First.grid(column=0, row=1, sticky=tk.E)
First_text = tk.StringVar()
First_entry = ttk.Entry(frame, width=26, textvariable=First_text)
First_entry.grid(column=1, row=1, sticky=tk.E)

Last = ttk.Label(frame, text="Last Name:")
Last.grid(column=0, row=2, sticky=tk.E)
Last_text = tk.StringVar()
Last_entry = ttk.Entry(frame, width=26, textvariable=Last_text)
Last_entry.grid(column=1, row=2, sticky=tk.E)

position = ttk.Label(frame, text="Position:")
position.grid(column=0, row=3, sticky=tk.E)
position_text = tk.StringVar()
position_entry = ttk.Entry(frame, width=26, textvariable=position_text)
position_entry.grid(column=1, row=3, sticky=tk.E)

At_Bats = ttk.Label(frame, text="At_Bats:")
At_Bats.grid(column=0, row=4, sticky=tk.E)
At_Bats_text = tk.StringVar()
At_Bats_entry = ttk.Entry(frame, width=26, textvariable=At_Bats_text)
At_Bats_entry.grid(column=1, row=4, sticky=tk.E)

Hits = ttk.Label(frame, text="Hits:")
Hits.grid(column=0, row=5, sticky=tk.E)
Hits_text = tk.StringVar()
Hits_entry = ttk.Entry(frame, width=26, textvariable=Hits_text)
Hits_entry.grid(column=1, row=5, sticky=tk.E)

batting = ttk.Label(frame, text="Batting Avg:")
batting.grid(column=0, row=6, sticky=tk.E)
batting_text = tk.StringVar()
batting_entry = ttk.Entry(frame, width=26, textvariable=batting_text, state="readonly")
batting_entry.grid(column=1, row=6, sticky=tk.E)


get_button = ttk.Button(frame, text="Get player", command=Button_1)
get_button.grid(column=3, row=0, sticky=tk.E)

changes = ttk.Button(frame, text="Save Changes", command=Button_2)
changes.grid(column=1, row=7, sticky=tk.W)

cancel = ttk.Button(frame, text="Cancel", command=Button_3)
cancel.grid(column=1, row=7, sticky=tk.E)

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=3)

window.mainloop()

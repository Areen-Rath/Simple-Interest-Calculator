from tkinter import *

window = Tk()

window.title("Simple Interest Calculator")
window.geometry("400x400")

window.configure(bg = "lightcyan")

def interest():
    principal = float(principal_entry.get())
    rate = float(rate_entry.get())
    time = float(time_entry.get())
    i = principal * rate * time/100
    interest = round(i, 2)
    result.destroy()

    output = Label(
        result_frame,
        text = f"Your interest is {interest}",
        fg = "black",
        bg = "lightcyan",
        font = ("Calibri", 12),
        width = 42
    )
    output.place(x = 20, y = 40)
    output.pack()

heading = Label(
    window,
    text = "Simple Interest Calculator",
    fg = "black", 
    bg = "lightcyan",
    font = ("Calibri", 20),
    bd = 5
)
heading.place(x = 50, y = 20)

principal_label = Label(
    window,
    text = "Principal",
    fg = "black", 
    bg = "lightcyan",
    font = ("Calibri", 12),
    bd = 1
)
principal_label.place(x = 20, y = 90)

principal_entry = Entry(window, text = '', bd = 2, width = 22)
principal_entry.place(x = 170, y = 95)

result_frame = LabelFrame(window, text = "Interest", bg = "lightcyan", font = ("Calibri", 12))
result_frame.pack(padx = 20, pady = 20)
result_frame.place(x = 20, y = 300)

result = Label(result_frame, text = '', bg = "lightcyan", font = ("Calibri", 12), width = 33)
result.place(x = 20, y = 20)
result.pack()

rate_label = Label(
    window,
    text = "Rate of Interest (in %)",
    fg = "black",
    bg = "lightcyan",
    font = ("Calibri", 12)
)
rate_label.place(x = 20, y = 140)

rate_entry = Entry(window, text = '', bd = 2, width = 15)
rate_entry.place(x = 170, y = 145)

time_label = Label(
    window,
    text = "Time Period (in Years)",
    fg = "black",
    bg = "lightcyan",
    font = ("Calibri", 12)
)
time_label.place(x = 20, y = 185)

time_entry = Entry(window, text = '', bd = 2, width = 22)
time_entry.place(x = 170, y = 185)

button = Button(window, text = "Calculate", fg = "black", bg = "lightcyan", bd = 4, command = interest)
button.place(x = 20, y = 250)

window.mainloop()
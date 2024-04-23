from tkinter import *
from tkinter.ttk import Combobox, Scrollbar

#-----------------------------------------------------------------------------------------------------

# Вираховування оцінки
def btn0_click():
    mark = 0
    if v1.get() == 1 and v2.get() == 1 and v3.get() == 0 and v4.get() == 0:
        mark += 2
    elif v1.get() == 1 and v2.get() == 0 and v3.get() == 0 and v4.get() == 0:
        mark += 1
    elif v1.get() == 0 and v2.get() == 1 and v3.get() == 0 and v4.get() == 0:
        mark += 1
    if v5.get() == 4:
        mark += 2
    if ent3.get() == '9':
        mark += 2
    if cb4.get() == '10':
        mark += 2
    if scale5.get() == 70:
        mark += 2
    if n6[0] == 1:
        mark += 2
    v6.set("Ваша оцінка: " + str(mark))
    if mark > 6:
        lbl0.config(fg="green")
    else:
        lbl0.config(fg="red")

#---------------------------------------------------------------------------------------------------------

tk = Tk()
tk.title("Тест з математики")
font_title = ("Arial", 14, "bold")
font_q = ("Arial", 12, "bold")
tk.geometry('400x500')
tk.resizable(width=False, height=False)

#----------------------------------------------------------------------------------------------------------

# Scrollbar
frame = Frame(tk)
frame.pack(fill=BOTH, expand=True)

canvas = Canvas(frame)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)


def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas.bind('<Configure>', on_configure)

tk_scrollbar = Frame(canvas)

canvas.create_window((0, 0), window=tk_scrollbar, anchor='nw')
canvas.update_idletasks()
#-----------------------------------------------------------------------------------------------------------

# Питання 1
lbl1 = Label(tk_scrollbar, text="Питання №1", font=font_title)
lbl11 = Label(tk_scrollbar, text="Знайти ВСІ корені рівняння: x^2+3x-10=0", font=font_q)
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
chb1 = Checkbutton(tk_scrollbar, text="-5", variable=v1, onvalue=1, offvalue=0)
chb2 = Checkbutton(tk_scrollbar, text="2", variable=v2, onvalue=1, offvalue=0)
chb3 = Checkbutton(tk_scrollbar, text="8", variable=v3, onvalue=1, offvalue=0)
chb4 = Checkbutton(tk_scrollbar, text="-1", variable=v4, onvalue=1, offvalue=0)


# Питання 2
lbl2 = Label(tk_scrollbar, text="Питання №2", font=font_title)
lbl21 = Label(tk_scrollbar, text="Чому дорівнює куб числа 2?", font=font_q)
v5 = IntVar()
rbt1 = Radiobutton(tk_scrollbar, text="6", variable=v5, value=1)
rbt2 = Radiobutton(tk_scrollbar, text="4", variable=v5, value=2)
rbt3 = Radiobutton(tk_scrollbar, text="3", variable=v5, value=3)
rbt4 = Radiobutton(tk_scrollbar, text="8", variable=v5, value=4)

# Питання 3
lbl3 = Label(tk_scrollbar, text="Питання №3", font=font_title)
lbl31 = Label(tk_scrollbar, text='Яка найбільша цифра?')
ent3 = Entry(tk_scrollbar)


# Питання 4
lbl4 = Label(tk_scrollbar, text="Питання №4", font=font_title)
lbl41 = Label(tk_scrollbar, text="Скільки становить 1% від 1000грн?", font=font_q)
data = ('1','10','100','1000')
cb4 = Combobox(tk_scrollbar, values=data)


# Питання 5
lbl5 = Label(tk_scrollbar, text="Питання №5", font=font_title)
lbl51 = Label(tk_scrollbar, text="Середнє арифметичне чисел 53, 67 та 90", font=font_q)
scale5 = Scale(tk_scrollbar, orient=HORIZONTAL, length=300, from_=50, to=80, tickinterval=5, resolution=1)


# Питання 6
n6 = [0]

def yes():
    n6.clear()
    n6.append(1)

def no():
    n6.clear()
    n6.append(0)

lbl6 = Label(tk_scrollbar, text="Питання №6", font=font_title)
lbl61 = Label(tk_scrollbar, text="Чи є 13 простим числом?", font=font_q)
btn61 = Button(tk_scrollbar, text="Так", command=yes)
btn62 = Button(tk_scrollbar, text="Ні", command=no)


# Відповісти
btn0 = Button(tk_scrollbar, text="Відповісти", command=btn0_click, font=font_q)
v6 = StringVar()
lbl0 = Label(tk_scrollbar, text='', textvariable=v6, font=font_title)



#.pack()
lbl1.pack()
lbl11.pack()
chb1.pack()
chb2.pack()
chb3.pack()
chb4.pack()

lbl2.pack()
lbl21.pack()
rbt1.pack()
rbt2.pack()
rbt3.pack()
rbt4.pack()

lbl3.pack()
lbl31.pack()
ent3.pack()

lbl4.pack()
lbl41.pack()
cb4.pack()

lbl5.pack()
lbl51.pack()
scale5.pack()

lbl6.pack()
lbl61.pack()
btn61.pack()
btn62.pack()

btn0.pack()
lbl0.pack()

tk.mainloop()

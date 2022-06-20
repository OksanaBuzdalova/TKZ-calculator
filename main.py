from tkinter import *
import matplotlib, numpy, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

step_orange = 20.5
step_brown = 17.5
step_blue = 13.6
step_green = 11.2
turns = 5500
n = 2
hours = 0
time_cost = 0
gap = 0
m = 1
amount = 0
speed = 0

window = Tk()
insert_step_orange = 0
insert_step_brown = 0
insert_step_green = 0
insert_step_blue = 0
insert_turns = 0
insert_n = 0
insert_hours = 0
insert_pause = 0
insert_gap = 0
insert_amount_prA = 0
insert_speed_prA = 0

def update():
    global step_orange
    global step_brown
    global step_blue
    global step_green
    global turns
    global n
    global hours
    global time_cost
    global gap
    global amount
    global speed

    global insert_step_orange
    global insert_step_brown
    global insert_step_green
    global insert_step_blue
    global insert_turns
    global insert_n
    global insert_hours
    global insert_pause
    global insert_gap
    global insert_amount_prA
    global insert_speed_prA

    step_orange = float(insert_step_orange.get())
    step_brown = float(insert_step_brown.get())
    step_blue = float(insert_step_blue.get())
    step_green = float(insert_step_green.get())
    turns = int(insert_turns.get())
    n = int(insert_n.get())
    hours = int(insert_hours.get())
    time_cost = int(insert_pause.get())
    gap = float(insert_gap.get())
    amount = float(insert_amount_prA.get())
    speed = float(insert_speed_prA.get())

    main_func()

def add():
    global m
    global window
    m += 1
    window.destroy()
    window = Tk()
    draw()

def draw():
    global m
    global window
    global insert_step_orange
    global insert_step_brown
    global insert_step_green
    global insert_step_blue
    global insert_turns
    global insert_n
    global insert_hours
    global insert_pause
    global insert_gap
    global insert_amount_prA
    global insert_speed_prA

    window.title("Калькулятор")

    frm_form = Frame(relief=SUNKEN, borderwidth=3)
    frm_form.pack()

    lbl_step2 = Label(master=frm_form, text="Приоритет А")
    lbl_step2.grid(row=0, column=0, sticky="e")

    lbl_step = Label(master=frm_form, text="    ")
    lbl_step.grid(row=2, column=1, sticky="e")

    lbl_step_orange = Label(master=frm_form, text="Шаг скрутки (в мм):"+"\n " +"Оранжевый")
    insert_step_orange = Entry(master=frm_form, width=20)
    insert_step_orange.insert(0, "20.5")
    lbl_step_orange.grid(row=2, column=2)
    insert_step_orange.grid(row=3, column=2)

    lbl_step_brown = Label(master=frm_form, text="Шаг скрутки (в мм):"+"\n " +"Коричневый")
    insert_step_brown = Entry(master=frm_form, width=20)
    insert_step_brown.insert(0, "17.5")
    lbl_step_brown.grid(row=2, column=3)
    insert_step_brown.grid(row=3, column=3)

    lbl_step_blue = Label(master=frm_form, text="Шаг скрутки (в мм):"+"\n " +"Синий")
    insert_step_blue = Entry(master=frm_form, width=20)
    insert_step_blue.insert(0, "13.6")
    lbl_step_blue.grid(row=2, column=4)
    insert_step_blue.grid(row=3, column=4)

    lbl_step_green = Label(master=frm_form, text="Шаг скрутки (в мм):"+"\n " +"Зеленый")
    insert_step_green = Entry(master=frm_form, width=20)
    insert_step_green.insert(0, "11.2")
    lbl_step_green.grid(row=2, column=5)
    insert_step_green.grid(row=3, column=5)

    lbl_amount_prA = Label(master=frm_form, text="Кол-во")
    insert_amount_prA = Entry(master=frm_form, width=20)
    insert_amount_prA.insert(0, "1")
    lbl_amount_prA.grid(row=2, column=6)
    insert_amount_prA.grid(row=3, column=6)

    lbl_speed_prA = Label(master=frm_form, text="Скорость (км в день)")
    insert_speed_prA = Entry(master=frm_form, width=20)
    insert_speed_prA.insert(0, "1")
    lbl_speed_prA.grid(row=2, column=7)
    insert_speed_prA.grid(row=3, column=7)

    buttons = list()
    for i in range(m):
        buttons.append([])

    lbl_step3 = Label(master=frm_form, text="Приоритет Б")
    lbl_step3.grid(row=4, column=0, sticky="e")

    for i in range(m):
        for j in range(5):
            buttons[i].append(Entry(master=frm_form, width=20))

        lbl_type = Label(master=frm_form, text="Тип"+' '+str(i+1))
        lbl_type.grid(row=2 * i + 5, column=0, sticky="e")

        lbl_step2 = Label(master=frm_form, text="   ")
        lbl_step2.grid(row=2 * i + 5, column=1, sticky="e")

        lbl_step_orange2 = Label(master=frm_form, text="Шаг скрутки (в мм):"+"\n " +" Оранжевый")
        insert_step_orange2 = Entry(master=frm_form, width=20)
        insert_step_orange2.insert(0, "20.5")
        lbl_step_orange2.grid(row=2 * i + 5, column=2)
        insert_step_orange2.grid(row=2 * i + 6, column=2)

        lbl_step_brown2 = Label(master=frm_form, text="Шаг скрутки (в мм):"+"\n " +" Коричневый")
        insert_step_brown2 = Entry(master=frm_form, width=20)
        insert_step_brown2.insert(0, "17.5")
        lbl_step_brown2.grid(row=2 * i + 5, column=3)
        insert_step_brown2.grid(row=2 * i + 6, column=3)

        lbl_step_blue2 = Label(master=frm_form, text="Шаг скрутки (в мм):"+"\n " +" Синий")
        insert_step_blue2 = Entry(master=frm_form, width=20)
        insert_step_blue2.insert(0, "13.6")
        lbl_step_blue2.grid(row=2 * i + 5, column=4)
        insert_step_blue2.grid(row=2 * i + 6, column=4)

        lbl_step_green2 = Label(master=frm_form, text="Шаг скрутки (в мм):"+"\n " +"Зеленый")
        insert_step_green2 = Entry(master=frm_form, width=20)
        insert_step_green2.insert(0, "11.2")
        lbl_step_green2.grid(row=2 * i + 5, column=5)
        insert_step_green2.grid(row=2 * i + 6, column=5)

        lbl_amount_prA_2 = Label(master=frm_form, text="Кол-во")
        insert_amount_prA_2 = Entry(master=frm_form, width=20)
        insert_amount_prA_2.insert(0, "1")
        lbl_amount_prA_2.grid(row=2 * i + 5, column=6)
        insert_amount_prA_2.grid(row=2 * i + 6, column=6)

    frm_buttons2 = Frame()
    frm_buttons2.pack(fill=X, ipadx=5, ipady=5)
    btn_add = Button(
        master=frm_buttons2,
        text="Добавить",
        command=add
    )
    btn_add.pack(side=BOTTOM, pady=5, ipady=10)

    frm_form = Frame(relief=SUNKEN, borderwidth=3)
    frm_form.pack()

    lbl_step = Label(master=frm_form, text="")
    lbl_step1 = Label(master=frm_form, text="")
    lbl_step.grid(row=2 * m + 7, column=0, sticky="e")
    lbl_step1.grid(row=2 * m + 7, column=1)

    lbl_turns = Label(master=frm_form, text="Число оборотов рамки (в минуту)")
    insert_turns = Entry(master=frm_form, width=50)
    insert_turns.insert(0, "5500")
    lbl_turns.grid(row=2 * m + 8, column=0, sticky="e")
    insert_turns.grid(row=2 * m + 8, column=1)

    lbl_step = Label(master=frm_form, text="")
    lbl_step1 = Label(master=frm_form, text="")
    lbl_step.grid(row=2 * m + 9, column=0, sticky="e")
    lbl_step1.grid(row=2 * m + 9, column=1)

    lbl_n = Label(master=frm_form, text="Число парокрутов")
    insert_n = Entry(master=frm_form, width=50)
    insert_n.insert(0, "7")
    lbl_n.grid(row=2 * m + 10, column=0, sticky="e")
    insert_n.grid(row=2 * m + 10, column=1)

    lbl_step = Label(master=frm_form, text="")
    lbl_step1 = Label(master=frm_form, text="")
    lbl_step.grid(row=2 * m + 11, column=0, sticky="e")
    lbl_step1.grid(row=2 * m + 11, column=1)

    lbl_pause = Label(master=frm_form, text="Время перехода (мин)")
    insert_pause = Entry(master=frm_form, width=50)
    insert_pause.insert(0, "30")
    lbl_pause.grid(row=2 * m + 12, column=0, sticky="e")
    insert_pause.grid(row=2 * m + 12, column=1)

    lbl_step = Label(master=frm_form, text="")
    lbl_step1 = Label(master=frm_form, text="")
    lbl_step.grid(row=2 * m + 13, column=0, sticky="e")
    lbl_step1.grid(row=2 * m + 13, column=1)

    lbl_step = Label(master=frm_form, text="На какое время нужно")
    lbl_step1 = Label(master=frm_form, text="")
    lbl_step.grid(row=2 * m + 14, column=0, sticky="e")
    lbl_step1.grid(row=2 * m + 14, column=1)

    lbl_hours = Label(master=frm_form, text="сделать прогноз (в часах)?")
    insert_hours = Entry(master=frm_form, width=50)
    insert_hours.insert(0, "720")
    lbl_hours.grid(row=2 * m + 15, column=0, sticky="e")
    insert_hours.grid(row=2 * m + 15, column=1)

    lbl_step = Label(master=frm_form, text="")
    lbl_step1 = Label(master=frm_form, text="")
    lbl_step.grid(row=2 * m + 16, column=0, sticky="e")
    lbl_step1.grid(row=2 * m + 16, column=1)

    lbl_gap = Label(master=frm_form, text="Допустимая разница (в км)")
    insert_gap = Entry(master=frm_form, width=50)
    insert_gap.insert(0, "170")
    lbl_gap.grid(row=2 * m + 17, column=0, sticky="e")
    insert_gap.grid(row=2 * m + 17, column=1)

    lbl_step = Label(master=frm_form, text="")
    lbl_step1 = Label(master=frm_form, text="")
    lbl_step.grid(row=2 * m + 18, column=0, sticky="e")
    lbl_step1.grid(row=2 * m + 18, column=1)

    frm_buttons = Frame()
    frm_buttons.pack(fill=X, ipadx=5, ipady=5)

    btn_submit = Button(
        master=frm_buttons,
        text="Сформировать прогноз",
        command=update
    )
    btn_submit.pack(side=BOTTOM, pady=5, ipady=10)
    window.mainloop()


def main_func():
    global step_orange
    global step_brown
    global step_blue
    global step_green
    global turns
    global n
    global hours
    global time_cost
    global gap
    global window
    global amount
    global speed

    steps = [step_orange, step_brown, step_blue, step_green]

    reload_enter = list()
    reload_exit = list()
    for j in range(4):
        reload_enter.append((52*1000000)/(steps[j]*turns*60))
        reload_exit.append((14 * 1000000) / (steps[j] * turns*60))

    print(reload_enter, reload_exit)

    day_n = 4*270*1000000

    a = step_green / step_orange
    b = step_green / step_brown
    c = step_green / step_blue

    z = day_n / (a + b + c + 1)

    a = a * z
    b = b * z
    c = c * z

    day_1 = day_n / n

    orange_pairs = a / day_1
    brown_pairs = b / day_1
    blue_pairs = c / day_1
    green_pairs = z / day_1

    stable = [int(orange_pairs), int(brown_pairs), int(blue_pairs), int(green_pairs)]
    print(stable)

    orange_pairs -= stable[0]
    brown_pairs -= stable[1]
    blue_pairs -= stable[2]
    green_pairs -= stable[3]

    l = list()
    l.append(orange_pairs)
    l.append(brown_pairs)
    l.append(blue_pairs)
    l.append(green_pairs)
    l.sort()

    unstable = [0, 0, 0, 0]

    for i in range(n - stable[0] - stable[1] - stable[2] - stable[3]):
        if orange_pairs == l[4 - i - 1]:
            unstable[0] += 1
        if brown_pairs == l[4 - i - 1]:
            unstable[1] += 1
        if blue_pairs == l[4 - i - 1]:
            unstable[2] += 1
        if green_pairs == l[4 - i - 1]:
            unstable[3] += 1
    print(unstable)

    h = list()
    h = [0, 0, 0, 0]
    names = ['Оранжевый', 'Коричневый', 'Синий', 'Зеленый']

    changes = list()

    changes.append('Час № 0:'+'\n')
    for i in range(4):
        changes.append(names[i] + ': ' + 'стабильные ' + str(stable[i]) + ', балансирующие ' + str(unstable[i])+'\n')

    stable_temp = stable.copy()
    unstable_temp = unstable.copy()
    n_rasp_stable = n*[-1]
    n_rasp_unstable = n*[-1]
    for i in range(n):
        for j in range(4):
            if stable_temp[j] != 0:
                stable_temp[j] -= 1
                n_rasp_stable[i] = j
                break
            else:
                if unstable_temp[j] != 0:
                    unstable_temp[j] -= 1
                    n_rasp_unstable[i] = j
                    break

    colors_unstable = [-1]*4
    for i in range(4):
        for j in range(n):
            if n_rasp_unstable[j] == i:
                colors_unstable[i] = j

    time_cost = time_cost / 60
    empty_time = 0

    for i in range(1, hours + 1):
        change = False
        h[0] += steps[0] * turns * 60 * (stable[0] + unstable[0])
        h[1] += steps[1] * turns * 60 * (stable[1] + unstable[1])
        h[2] += steps[2] * turns * 60 * (stable[2] + unstable[2])
        h[3] += steps[3] * turns * 60 * (stable[3] + unstable[3])
        for j in range(4):
            for k in range(4):
                if abs(h[j] - h[k]) >= gap*1000*1000:
                    change = True
                    h[j] -= steps[j] * turns * 60 * (stable[j] + unstable[j])
                    h[k] -= steps[k] * turns * 60 * (stable[k] + unstable[k])

                    unstable[k], unstable[j] = unstable[j], unstable[k]
                    if colors_unstable[j] != -1:
                        empty_time += time_cost
                    if colors_unstable[k] != -1:
                        empty_time += time_cost
                    colors_unstable[k], colors_unstable[j] = colors_unstable[j], colors_unstable[k]
                    h[j] += steps[j] * turns * (60 - time_cost*60) * (stable[j] + unstable[j])
                    h[k] += steps[k] * turns * (60 - time_cost*60) * (stable[k] + unstable[k])

                    changes.append('Час № ' + str(i) + ':'+'\n')
                    for f in range(4):
                        changes.append(names[f] + ': ' + 'стабильные ' + str(stable[f]) + ', балансирующие ' + str(unstable[f]) +'\n')
                    break
            if change:
                break

    changes.append('Итог:'+'\n')
    changes.append('Будет произведено '+str((h[0] + h[1] + h[2] + h[3])/1000000) + ' километров кабеля' +'\n')
    changes.append('Время простоя ' + str(empty_time) + 'ч.' + '\n')
    changes.append('Коэффициент полезного времени ' + str(100*(hours*n - empty_time)/(hours*n)) + '%')
    changes_str = ''.join(changes)

    print(changes_str)

    window.destroy()

    window1 = Tk()
    text = Text(width=80, height=30)
    text.insert(INSERT, changes_str)
    text.configure(state='disabled')
    text.pack(side=LEFT)

    scroll = Scrollbar(command=text.yview)
    scroll.pack(side=LEFT, fill=Y)

    text.config(yscrollcommand=scroll.set)
    window1.mainloop()

draw()
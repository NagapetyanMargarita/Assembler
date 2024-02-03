# This is a sample Python script.
import tkinter
from tkinter import *
import time


def change_text_value(sum):
    text_area.delete("1.0", "end")  # Удаляем текущий текст
    text_area.insert("1.0", str(sum))  # Вставляем новый текст

def change_color_V(tag):
    r_canvas.itemconfig(tag, fill="red")

def change_color(tag):
    r_canvas.itemconfig(tag, fill="yellow")
    tk.after(300, lambda: reset_color(tag))

def reset_color(tag):
    r_canvas.itemconfig(tag, fill="white")
def update_rotation_angle(l):
    global rotation_angle
    rotation_angle += 5  # Увеличиваем угол поворота на 5 градусов
    rotation_angle %= 360  # Ограничиваем угол поворота до 360 градусов
    # Очищаем холст
    canvas.delete("fun")

    # Рисуем лопасти вентилятора с обновленным углом поворота
    for i in range(4):
        start_angle = rotation_angle + i * 90
        end_angle = start_angle + 45

        # Рисуем дугу лопасти
        canvas.create_arc(
            center_x - radius,
            center_y - radius,
            center_x + radius,
            center_y + radius,
            start=start_angle,
            extent=45,
            fill=blade_color,
            outline="",
            tags="fun"
        )
    delay = skor[l-1]
    # Вызываем функцию обновления через 50 миллисекунд
    tk.after(delay, update_rotation_angle,l)

v=-1
k1,k2,k3,k4 = 0,0,0,0
skor = 0
d=0
V = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
T1 = [60, 10, 23, 34, 50, 11, 32, 26, 10, -5, 26, 12]
T2 = [8, 22, 34]
T3 = [-4, -1, 0, 9]
T4 = [0, 1]
'''T1 = [-10, 10, 13, 34, 50, 1, 3, 26, 10, -5, 26, 12]
T2 = [8, 22, 13]
T3 = [-4, -1, 0, 9]
T4 = [0, 1]'''
array_sum=[]
v_array=[]
skor=[]
sum = 0
# создаем графическое окно tk
tk = Tk()
tk.title("Вентилятор")

# Создаем холст
canvas = Canvas(tk, height=400, width=600, bg="white")
canvas.pack()
text_area = Text(tk, height=3, width=20)
text_area.insert("1.0", "")
text_area.configure(borderwidth=2, relief="solid")
text_area_window = canvas.create_window(508, 310, window=text_area, anchor="center")

canvas.create_rectangle(100, 360, 300, 390, fill="black")#впправо вверх
canvas.create_rectangle(190, 200, 210, 360, fill="black")#впправо вверх

r_canvas = Canvas(canvas, height=400, width=600, bg="white",  borderwidth=2, highlightthickness=2, highlightbackground="black")
r_canvas.place(x=400, y=50)

# Рисуем прямоугольник на отдельном холсте
r_canvas.create_rectangle(50, 50, 90, 90, fill="white", tags="T1_t")
r_canvas.create_rectangle(120, 50, 160, 90, fill="white", tags="T2_t")# вправо вверх
r_canvas.create_rectangle(50, 120, 90, 160, fill="white", tags="T3_t")
r_canvas.create_rectangle(120, 120, 160, 160, fill="white", tags="T4_t")
r_canvas.create_rectangle(70, 190, 140, 220, fill="green", tags="V")


# Координаты центра вентилятора. Работа свентилятоом
center_x = 200
center_y = 200
radius = 100 # Радиус вентилятора
blade_color = "grey" # Цвет лопастей вентилятора
rotation_angle = 0 # Угол поворота лопастей

for i in range(4):
    start_angle = rotation_angle + i * 90
    end_angle = start_angle + 45

    # Рисуем дугу лопасти
    canvas.create_arc(
        center_x - radius,
        center_y - radius,
        center_x + radius,
        center_y + radius,
        start=start_angle,
        extent=45,
        fill=blade_color,
        outline="",
        tags="fun"
    )

for k in range(0,3):
    if (k == 1):
        T1 = [-10, 10, 13, 34, 50, 1, 3, 26, 10, -5, 26, 12]
    if (k == 2):
        V = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    for i in range(1,13):
        sum += T1[k1]
        if (i == 12):
            sum += T2[k2]
            sum += T3[k3]
            sum += T4[k4]
            k4 +=1
            k2 += 1
            k3 += 1
        if (i == 9):
            sum += T3[k3]
            k3 += 1
        if (i == 8):
            sum += T2[k2]
            k2 += 1
        if (i == 6):
            sum += T3[k3]
            sum += T4[k4]
            k4 += 1
            k3 += 1
        if (i == 4):
            sum += T2[k2]
            k2 += 1
        if (i == 3):
            sum += T3[k3]
            k3 += 1
        if V[i-1] == 1:
            v = i
    if (sum / 21 >= 20 and v == -1):
        skor.append(100)
    elif (sum / 21 < 20 and v == -1):
        skor.append(500)
    else:
        skor.append(25)
    array_sum.append(sum/21)
    v_array.append(v)
    sum=0
    k1=k2=k3=k4=0
print(array_sum)
print(v_array)
print(skor)

def start_rotation(l):
    for i in range(1, 13):
        delay = (l - 1) * 12 * 500 + i * 500  # Вычисляем задержку для каждой итерации
        delay1 = delay * l
        tk.after(delay, change_color, "T1_t")
        if i == 12:
            tk.after(delay, change_color, "T2_t")
            tk.after(delay, change_color, "T3_t")
            tk.after(delay, change_color, "T4_t")
        if i == 9:
            tk.after(delay, change_color, "T3_t")
        if i == 8:
            tk.after(delay, change_color, "T2_t")
        if i == 6:
            tk.after(delay, change_color, "T3_t")
            tk.after(delay, change_color, "T4_t")
        if i == 4:
            tk.after(delay, change_color, "T2_t")
        if i == 3:
            tk.after(delay, change_color, "T3_t")
        if v_array[l - 1] == i:
            tk.after(delay, change_color_V, "V")
            break

    tk.after(delay, change_text_value, array_sum[l - 1])
    tk.after(delay, update_rotation_angle, l)


for l in range(1, 4):
    delay = (l - 1) * 12 * 300   # Вычисляем задержку для каждой итерации
    tk.after(delay, start_rotation, l)

# Запускаем функцию обновления угла поворота


# Запускаем главный цикл событий Tkinter
tk.mainloop()

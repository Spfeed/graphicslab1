import tkinter as tk
from tkinter import Canvas


def increase_radius(event):
    global R
    R += 10  # Увеличиваем радиус на 10
    canvas.delete("circle")
    draw_circle()


def decrease_radius(event):
    global R
    if R > 10:  # Уменьшаем радиус, но не меньше 10
        R -= 10
        canvas.delete("circle")
        draw_circle()


def draw_circle():
    canvas.create_oval(x - R, y - R, x + R, y + R, outline="blue", width=2, tags="circle")


def on_key(event):
    if event.keysym == 'greater':
        increase_radius(event)
    elif event.keysym == 'less':
        decrease_radius(event)
    elif event.keysym == 'Escape':
        root.quit()


# Создаем окно Tkinter
root = tk.Tk()
root.title("Рисование окружности")

# Устанавливаем начальные значения
x, y, R = 150, 150, 50

# Создаем Canvas (холст) для рисования окружности
canvas = Canvas(root, width=300, height=300)
canvas.pack()

# Рисуем окружность при запуске программы
draw_circle()

# Привязываем события к клавишам
root.bind("<KeyPress-greater>", on_key)
root.bind("<KeyPress-less>", on_key)
root.bind("<KeyPress-Escape>", on_key)

# Запускаем главный цикл Tkinter
root.mainloop()

import tkinter as tk



# Создается окно Tkinter и запускается главный цикл
root = tk.Tk()
root.title("Рисование окружности")
# Создается Canvas (холст) для рисования окружности, значения устанавливаются вручную
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Установка значений: x - координата центра окружности по оси абсцисс, y - по оси ординат, R - радиус окружности.
x, y, R = 150, 150, 50

def increase_radius():
    """
    Данная функция увеличивает радиус окружности на 10 пикселей.
    """
    global R
    R += 10  # Увеличиваем радиус на 10
    return R

def increase_rad_draw(event):
    """
    Аргументы: event - событие, по происхождению которого функция начинает работу, в данной ситуации - нажатие на клавишу

    Визуальное увеличиение радиуса производится при помощи удаления старой окружности с меньшим радиусом и отрисовки новой.
    """
    increase_radius()
    canvas.delete("circle")
    draw_circle(x,y,R,canvas)

def decrease_radius():
    """
     Данная функция увеличивает радиус окружности на 10 пикселей.

    Присутствует ограничение: минимальный радиус, после достижения которого окружность не уменьшается.

    """
    global R
    if R > 10:  # Уменьшаем радиус, но не меньше 10
        R-=10
    return R


def decrease_rad_draw(event):
    """
    Аргументы: event - событие, по происхождению которого функция начинает работу, в данной ситуации - нажатие на клавишу

    Визуальное уменьшение радиуса производится при помощи удаления старой окружности с большим радиусом и отрисовки новой.
    """
    decrease_radius()
    canvas.delete("circle")
    draw_circle(x,y,R,canvas)

def draw_circle(x,y,R,canvas):
    """
    Данная функция создает окружность на холсте.

    Аргументы:  x - координаты центра окружности по оси абсцисс;
                y - координаты центра окружности по оси ординат;
                R - радиус окружности.
                cavas - холст, на котором будет отрисовываться окружность

    По умолчанию в Tkinter отсутсвует возможность строить окружности, поэтому используется функция create_oval(), создающая овал
    по координатам 4 точек, при помощи чего он и приобретает вид окружности
    """
    canvas.create_oval(x - R, y - R, x + R, y + R, outline="blue", width=2, tags="circle")

#Привязка клавиш к событиям: ">" - к увеличению радиуса(см. выше), "<" - к уменьшению радиуса (см. выше), "esc" - остановка программы
#События increase_radius и decrease_radius являются вручную написанными функциями.
def on_key(event):
    if event.keysym == 'greater':
        increase_rad_draw(event)
    elif event.keysym == 'less':
        decrease_rad_draw(event)
    elif event.keysym == 'Escape':
        root.quit()

if __name__ == '__main__':
    # Рисуем окружность при запуске программы
    draw_circle(x,y,R,canvas)

    # Привязка события к клавишам "<", ">", "esc".
    root.bind("<KeyPress-greater>", on_key)
    root.bind("<KeyPress-less>", on_key)
    root.bind("<KeyPress-Escape>", on_key)

    # Запускаем главный цикл Tkinter
    root.mainloop()

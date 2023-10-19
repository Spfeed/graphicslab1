import unittest
import sys
import os
from tkinter import *
from main import draw_circle, increase_radius, decrease_radius

# Получаем путь к текущему каталогу скрипта
current_dir = os.path.dirname(os.path.abspath(__file__))
# Добавляем путь к родительскому каталогу
sys.path.append(os.path.join(current_dir, '..'))

import unittest
import tkinter as tk
from main import increase_radius, decrease_radius, draw_circle, R

class TestCircleFunctions(unittest.TestCase):

    #проверка функции увеличения радиуса
    def test_increase_radius(self):
        root=tk.Tk()
        canvas =tk.Canvas(root, width=200, height=300)
        canvas.pack()
        self.x, self.y, self.R = 150, 150, R
        draw_circle(self.x, self.y, self.R, canvas)
        print("Отработал увеличение")

        # Симулируем нажатие клавиши ">" для увеличения радиуса
        event = tk.Event()
        event.keysym = 'greater'
        canvas.event_generate("<KeyPress-greater>")
        canvas.update()

        # Проверяем, что радиус увеличился
        # Так как метод decrease_radius уже вызывался радиус R стал равен 40, поэтому производится сравнение с 50
        self.R = increase_radius(event)
        self.assertEqual(self.R, 50)

        root.destroy()

    #проверка уменьшения радиуса
    def test_decrease_radius(self):
        root = tk.Tk()
        canvas = tk.Canvas(root, width=200, height=300)
        canvas.pack()
        self.x, self.y, self.R = 150, 150, R
        draw_circle(self.x, self.y, self.R, canvas)
        print("Отработал уменьшение")

        # Симулируем нажатие клавиши "<" для уменьшения радиуса
        event = tk.Event()
        event.keysym = 'less'
        canvas.event_generate("<KeyPress-less>")
        canvas.update()

        # Проверяем, что радиус уменьшился
        #Так как начальное значение R=50, то сравниваем с 40
        self.R = decrease_radius(event)
        self.assertEqual(self.R, 40)

        root.destroy()

    if __name__ == '__main__':
        unittest.main()
import unittest
import sys
import os


# Получаем путь к текущему каталогу скрипта
current_dir = os.path.dirname(os.path.abspath(__file__))
# Добавляем путь к родительскому каталогу
sys.path.append(os.path.join(current_dir, '..'))

import unittest
from main_logic import increase_radius, decrease_radius

class TestCircleFunctions(unittest.TestCase):

    #проверка функции увеличения радиуса
    def test_decrease_radius(self):
        R = 50  # Исходный радиус
        event = object()  # Заглушка для event

        # Сохранить исходное значение радиуса
        initial_R = R

        # Вызвать decrease_radius
        R= decrease_radius()

        # Проверить, что радиус уменьшился на 10
        self.assertEqual(R, initial_R - 10)

    def test_increase_radius(self):
        R = 50  # Исходный радиус
        event = object()  # Заглушка для event

        # Сохранить исходное значение радиуса
        initial_R = R

        # Вызвать increase_radius
        R=increase_radius()

        # Проверить, что радиус увеличился на 10
        self.assertEqual(R, initial_R )

    if __name__ == '__main__':
        unittest.main()
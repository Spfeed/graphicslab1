import unittest
import sys
import os

# Получаем путь к текущему каталогу скрипта
current_dir = os.path.dirname(os.path.abspath(__file__))
# Добавляем путь к родительскому каталогу
sys.path.append(os.path.join(current_dir, '..'))



class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

#бесполезный комментарий для коммита
if __name__ == '__main__':
    unittest.main()

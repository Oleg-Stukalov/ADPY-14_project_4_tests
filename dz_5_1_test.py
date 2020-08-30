import unittest
from dz_5_1_functions import Functions_5_1

class TestFunctions(unittest.TestCase):

  #setUp method is overridden from the parent class TestCase
  def setUp(self):
    self.functions = Functions_5_1()

  #Each test method starts with the keyword test_
  def test_people(self):
    self.assertEqual(self.functions.number2name('2207 876234'), 'Василий Гупкин')
    self.assertEqual(self.functions.number2name('11-2'), 'Геннадий Покемонов')
    self.assertEqual(self.functions.number2name('10006'), 'Аристарх Павлов')

  def test_shelf(self):
    self.assertEqual(self.functions.number2shelf('2207 876234'), '1')
    self.assertEqual(self.functions.number2shelf('11-2'), '1')
    self.assertEqual(self.functions.number2shelf('5455 028765'), '1')
    self.assertEqual(self.functions.number2shelf('1006'), '2')

  def test_list(self):
    self.assertEqual(self.functions.list_documents('passport', '2207 876234', 'Василий Гупкин'), True)
    self.assertEqual(self.functions.list_documents('invoice', '11-2', 'Геннадий Покемонов'), True)
    self.assertEqual(self.functions.list_documents('insurance', '10006', 'Аристарх Павлов'), True)

  def test_add(self):
    self.assertEqual(self.functions.add_document('testdoc', '12345', 'Ivan Petrov', '1'), True)

# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()




# Задача №1 unit-tests
#
# Из курса «Python: программирование на каждый день и сверхбыстрое прототипирование» необходимо протестировать программу по работе с бухгалтерией Лекции 2.1. При наличии своего решения данной задачи можно использовать его или использовать предложенный код в директории scr текущего задания.
#
#     Следует протестировать основные функции по получению информации о документах, добавлении и удалении элементов из словаря.
#     Используйте fixture для загрузки данных в тестовый класс.
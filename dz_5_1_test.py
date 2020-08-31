import unittest
from unittest.mock import patch
from dz_5_1_functions import Functions_5_1

class TestFunctions(unittest.TestCase):

  # number2name mock data
  number2name_set0 = '2207 876234'
  number2name_result0 = 'Василий Гупкин'
  number2name_set1 = '11-2'
  number2name_result1 = 'Геннадий Покемонов'
  number2name_set2 = '10006'
  number2name_result2 = 'Аристарх Павлов'

  # number2shelf mock data
  number2shelf_set0 = '2207 876234'
  number2shelf_result0 = '1'
  number2shelf_set1 = '11-2'
  number2shelf_result1 = '1'
  number2shelf_set2 = '2207 876234'
  number2shelf_result2 = 'Василий Гупкин'
  number2shelf_set3 = '5455 028765'
  number2shelf_result3 = '2'

  # list_documents mock data
  list_documents_set0 = None
  list_documents_result0 = 'passport', '2207 876234', 'Василий Гупкин'
  list_documents_set1 = None
  list_documents_result1 = 'invoice', '11-2', 'Геннадий Покемонов'
  list_documents_set2 = None
  list_documents_result2 = 'insurance', '10006', 'Аристарх Павлов'

  # add_document mock data
  add_document_set0 = 'testdoc', '12345', 'Ivan Petrov', '1'
  add_document_result0 = None

  #setUp method is overridden from the parent class TestCase
  def setUp(self):
    self.functions = Functions_5_1()

  #Each test method starts with the keyword test_
  @patch('builtins.input', return_value=number2name_set0)
  def test_people(self, mock_input):
    result = self.functions.number2name()
    self.assertEqual(result, number2name_result0)

  @patch('builtins.input', return_value=number2name_set1)
  def test_people(self, mock_input):
    result = self.functions.number2name()
    self.assertEqual(result, number2name_result1)

  @patch('builtins.input', return_value=number2name_set2)
  def test_people(self, mock_input):
    result = self.functions.number2name()
    self.assertEqual(result, number2name_result2)

  # def test_people(self):
    # self.assertEqual(self.functions.number2name('2207 876234'), 'Василий Гупкин')
    # self.assertEqual(self.functions.number2name('11-2'), 'Геннадий Покемонов')
    # self.assertEqual(self.functions.number2name('10006'), 'Аристарх Павлов')


  @patch('builtins.input', return_value=number2shelf_set0)
  def test_shelf(self, mock_input):
    result = self.functions.number2shelf()
    self.assertEqual(result, number2shelf_result0)

  @patch('builtins.input', return_value=number2shelf_set1)
  def test_shelf(self, mock_input):
    result = self.functions.number2shelf()
    self.assertEqual(result, number2shelf_result1)

  @patch('builtins.input', return_value=number2shelf_set2)
  def test_shelf(self, mock_input):
    result = self.functions.number2shelf()
    self.assertEqual(result, number2shelf_result2)

  @patch('builtins.input', return_value=number2shelf_set3)
  def test_shelf(self, mock_input):
    result = self.functions.number2shelf()
    self.assertEqual(result, number2shelf_result3)

# def test_shelf(self):
    # self.assertEqual(self.functions.number2shelf('2207 876234'), '1')
    # self.assertEqual(self.functions.number2shelf('11-2'), '1')
    # self.assertEqual(self.functions.number2shelf('5455 028765'), '1')
    # self.assertEqual(self.functions.number2shelf('1006'), '2')


  @patch('builtins.input', return_value=list_documents_set0)
  def test_list(self, mock_input):
    result = self.functions.list_documents()
    self.assertEqual(result, list_documents_result0)

  @patch('builtins.input', return_value=list_documents_set1)
  def test_list(self, mock_input):
    result = self.functions.list_documents()
    self.assertEqual(result, list_documents_result1)

  @patch('builtins.input', return_value=list_documents_set2)
  def test_list(self, mock_input):
    result = self.functions.list_documents()
    self.assertEqual(result, list_documents_result2)

  # def test_list(self):
    # self.assertEqual(self.functions.list_documents('passport', '2207 876234', 'Василий Гупкин'), True)
    # self.assertEqual(self.functions.list_documents('invoice', '11-2', 'Геннадий Покемонов'), True)
    # self.assertEqual(self.functions.list_documents('insurance', '10006', 'Аристарх Павлов'), True)


  @patch('builtins.input', return_value=add_document_set0)
  def test_add(self, mock_input):
    result = self.functions.add_document()
    self.assertEqual(result, add_document_result2)

  # def test_add(self):
    # self.assertEqual(self.functions.add_document('testdoc', '12345', 'Ivan Petrov', '1'), True)



# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()




# Задача №1 unit-tests
#
# Из курса «Python: программирование на каждый день и сверхбыстрое прототипирование» необходимо протестировать программу по работе с бухгалтерией Лекции 2.1. При наличии своего решения данной задачи можно использовать его или использовать предложенный код в директории scr текущего задания.
#
#     Следует протестировать основные функции по получению информации о документах, добавлении и удалении элементов из словаря.
#     Используйте fixture для загрузки данных в тестовый класс.
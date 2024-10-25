import unittest
from data_structures import *

class MyTestCase(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(find_max([1, 2, 3, 4, 5]), 5)
        self.assertEqual(find_max([-9, -6, -11]), -6)
    
    def test_find_min(self):
        self.assertEqual(find_min([1, 2, 3, 4, 5]), 1)
        self.assertEqual(find_min([-9, -6, -11]), -11)

    def test_find_average(self):
        self.assertAlmostEqual(find_average([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(find_average([10, 20, 30, 40]), 25.0)

    def test_find_all_even_numbers(self):
        self.assertEqual(find_even_numbers([1, 2, 3, 4, 5]), (2, 4))
        self.assertEqual(find_even_numbers([10, 15, 20, 25]), (10, 20))

    def test_find_all_odd_numbers(self):
        self.assertEqual(find_odd_numbers([1, 2, 3, 4, 5]), (1, 3, 5))
        self.assertEqual(find_odd_numbers([10, 15, 20, 25]), (15, 25))

    def test_find_total_number_of_even_numbers(self):
        self.assertEqual(find_number_of_even_numbers([1, 2, 3, 4, 5]), 2)
        self.assertEqual(find_number_of_even_numbers([10, 12, 13, 15, 20]), 3)

    def test_find_total_number_of_odd_numbers(self):
        self.assertEqual(find_number_of_odd_numbers([1, 2, 3, 4, 5]), 3)
        self.assertEqual(find_number_of_odd_numbers([10, 11, 12, 15, 20]), 2)

    def test_return_list_stats(self):
        stats = return_list_stats([1, 2, 3, 4, 5])
        self.assertEqual(stats["min"], 1)
        self.assertEqual(stats["max"], 5)
        self.assertEqual(stats["average"], 3.0)
        self.assertEqual(stats["even_numbers"], (2, 4))
        self.assertEqual(stats["odd_numbers"], (1, 3, 5))
        self.assertEqual(stats["number_of_even_numbers"], 2)
        self.assertEqual(stats["number_of_odd_numbers"], 3)                                                        g
    
    def test_basic(self):
        input_list = ['a', '1', 'b', '3', 'c', '@', '5', 'd', 'e']
        result_alphabets, result_numbers = process_characters(input_list)
        self.assertEqual(result_alphabets, ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(result_numbers, [1, 3, 5])

    def test_mixed_input(self):
        input_list = ['a', '1', 'b', '3', 'c', '2', '@', '5', 'd', 'e']
        result_alphabets, result_numbers = process_characters(input_list)
        self.assertEqual(result_alphabets, ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(result_numbers, [1, 3, 2, 5])

    def test_repeated_characters(self):
        input_list = ['1', 'b', 'a', 'c', 'c', 'b', 'a', '1']
        result_alphabets, result_numbers = process_characters(input_list)
        self.assertEqual(result_alphabets, ['b', 'a', 'c', 'c', 'b', 'a'])
        self.assertEqual(result_numbers, [1, 1])

    def test_special_characters(self):
        input_list = ['!', '@', '#', '1', '2', '3', '$', '%', '^']
        result_alphabets, result_numbers = process_characters(input_list)
        self.assertEqual(result_alphabets, [])
        self.assertEqual(result_numbers, [1, 2, 3])

    def test_more_special_characters(self):
        input_list = ['%', '&', '*', '4', '6', '8', '(', ')', '!', 'x']
        result_alphabets, result_numbers = process_characters(input_list)
        self.assertEqual(result_alphabets, ['x'])
        self.assertEqual(result_numbers, [4, 6, 8])

    def test_generate_squared_dict(self):
        assert generate_squared_dict(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
        self.assertNotEqual(generate_squared_dict(4), {1: 1, 2: 4, 3: 9, 4: 15})
        

    def test_convert_word_list_sentence(self): 
        self.assertEqual(convert_word_list_sentence(['hello', 'world']), 'hello world')
        self.assertEqual(convert_word_list_sentence(['Python', 'is', 'fun']), 'Python is fun')

 
    def test_convert_word_list_spaces(self): 
        self.assertEqual(convert_word_list_spaces(['hello', 'world']), 'hello world ')
        self.assertEqual(convert_word_list_spaces(['Python', 'is', 'fun']), 'Python is fun ')

    def test_letters_count_sentence(self):
        self.assertEqual(letters_count_sentence("Hello world!"), 10)
        self.assertEqual(letters_count_sentence("Python3.9"), 6)

    def test_alphanumeric_1(self):
        self.assertEqual(is_alphanumeric("Python3"), True)
        self.assertEqual(is_alphanumeric("Python!"), False)
    
    def test_alphanumeric_2(self):
        self.assertEqual(is_alphanumeric("Hello123"), True)
        self.assertEqual(is_alphanumeric("Hello!"), False)
    
    def test_alphanumeric_3(self): 
        self.assertEqual(is_alphanumeric("test123"), True)
        self.assertEqual(is_alphanumeric("test@123"), False)
    


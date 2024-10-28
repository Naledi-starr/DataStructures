import unittest
from data_structures import *

class MyTestCase(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(find_max([1, 2, 3, 4, 5]), 5)
        self.assertEqual(find_max([-9, -6, -11]), -6)
        self.assertNotEqual(find_max([1, 2, 3]), 2)
    
    def test_find_min(self):
        self.assertEqual(find_min([1, 2, 3, 4, 5]), 1)
        self.assertEqual(find_min([-9, -6, -11]), -11)
        self.assertNotEqual(find_min([10, 20, 30]), 20)

    def test_find_average(self):
        self.assertAlmostEqual(find_average([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(find_average([10, 20, 30, 40]), 25.0)
        self.assertNotEqual(find_average([1, 2, 3]), 4.0)

    def test_find_all_even_numbers(self):
        self.assertEqual(find_even_numbers([1, 2, 3, 4, 5]), (2, 4))
        self.assertEqual(find_even_numbers([10, 15, 20, 25]), (10, 20))
        self.assertNotEqual(find_even_numbers([1, 3, 5]), [1, 2, 3])

    def test_find_all_odd_numbers(self):
        self.assertEqual(find_odd_numbers([1, 2, 3, 4, 5]), (1, 3, 5))
        self.assertEqual(find_odd_numbers([10, 15, 20, 25]), (15, 25))
        self.assertNotEqual(find_odd_numbers([2, 4, 6]), [2, 3, 6])

    def test_find_total_number_of_even_numbers(self):
        self.assertEqual(find_number_of_even_numbers([1, 2, 3, 4, 5]), 2)
        self.assertEqual(find_number_of_even_numbers([10, 12, 13, 15, 20]), 3)
        self.assertNotEqual(find_number_of_even_numbers([1, 3, 5]), 2)

    def test_find_total_number_of_odd_numbers(self):
        self.assertEqual(find_number_of_odd_numbers([1, 2, 3, 4, 5]), 3)
        self.assertEqual(find_number_of_odd_numbers([10, 11, 12, 15, 20]), 2)
        self.assertNotEqual(find_number_of_odd_numbers([2, 4, 6]), 3)

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
        self.assertNotEqual(result_alphabets, ['a', 'b', 'c', 'f'])

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
        self.assertNotEqual(result_alphabets, ['a', 'b','c','d' ])

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
        self.assertEqual(generate_squared_dict(5), {1: 1, 2: 4, 3: 9, 4: 16, 5: 25})
        self.assertEqual(generate_squared_dict(3), {1: 1, 2: 4, 3: 9})
        self.assertNotEqual(generate_squared_dict(4), {1: 1, 2: 4, 3: 9, 4: 15})
        

    def test_convert_word_list_sentence(self): 
        self.assertEqual(convert_to_word_list(["Hello", "world"]), "Hello world")
        self.assertEqual(convert_to_word_list(["Python", "is", "awesome"]), "Python is awesome")
        self.assertNotEqual(convert_to_word_list(["Test"]), "Test.")

 
    def test_convert_word_list_spaces(self): 
        self.assertEqual(convert_to_word_list(["Hello", "world"], 3), "Hello   world")
        self.assertEqual(convert_to_word_list(["Space", "test"], 2), "Space  test")
        self.assertNotEqual(convert_to_word_list(["Only", "one"], 4), "Only   one")

    def test_letters_count_sentence(self):
        self.assertEqual(letters_count_map("Hello world!"), {'H': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1})
        self.assertEqual(letters_count_map("Testing 123"), {'T': 1, 'e': 1, 's': 1, 't': 1, 'i': 1, 'n': 1, 'g': 1})
        self.assertNotEqual(letters_count_map("Python"), {'P': 2})

    def test_alphanumeric_1(self):
        self.assertEqual(text_to_morse("Hello123"), True)
        self.assertEqual(text_to_morse("!@#"), False)
        self.assertNotEqual(text_to_morse("Python!"), True)
    
    def test_alphanumeric_2(self):
        self.assertEqual(text_to_morse("Python"), True)
        self.assertEqual(text_to_morse("12345"), True)
        self.assertNotEqual(text_to_morse("!Hello"), True)
    
    def test_alphanumeric_3(self): 
        self.assertEqual(text_to_morse(""), False)
        self.assertEqual(text_to_morse("Test123"), True)
        self.assertNotEqual(text_to_morse("NoSpecial#"), True)
    


import lab6
import unittest
from data import Book
from lab6 import book_sort
from lab6 import swap_case
from lab6 import translate
from lab6 import histogram
# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_book_sort(self):
        books = [
            Book(["TJ"],"Lord"),
            Book(["WOW"],'The'),
            Book(["DOW"],"Him")
        ]
        result = book_sort(books, 2)
        self.assertEqual(result,2)

    def test_book_sort_2(self):
        books = [
            Book(["TJ"], "Lord"),
            Book(["WOW"], 'Ahe'),
            Book(["DOW"], "Zim")
        ]
        result = book_sort(books, 1)
        self.assertEqual(result, 1)
    # Part 2
    def test_swap_case(self):
        self.assertEqual(swap_case("Hello"), "hELLO")
    def test_swap_case_2(self):
        self.assertEqual(swap_case("Python"), "pYTHON")

    # Part 3
    def test_translate(self):
        self.assertEqual(translate("hello world", "o", "0"), "hell0 w0rld")
    def test_translate_2(self):
        self.assertEqual(translate("hello world", "l", "1"), "he11o wor1d")

    # Part 4
    def test_histogram(self):
        input_text = "hello hello world world world"
        expected = {'hello': 2, 'world': 3}
        self.assertEqual(histogram(input_text), expected)

    def test_histogram_2(self):
        input_text = "apple apple apple pie"
        expected = {'apple': 3, 'pie': 1}
        self.assertEqual(histogram(input_text), expected)




if __name__ == '__main__':
    unittest.main()

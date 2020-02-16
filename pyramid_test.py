import Pyramid
import unittest

correct_pyramid = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
]
correct_before_last_level_calculated_row = [125, 164, 102, 95, 112, 123, 165, 128, 166, 109, 122, 147, 100, 54]
correct_pyramid_result = 1074

un_correct_pyramid_1 = [[2, 3]]
un_correct_pyramid_2 = [[2], [3]]
un_correct_pyramid_3 = [[7], [1, "9"]]
un_correct_pyramid_4 = [[8], [9, 9, 8]]
un_correct_pyramid_5 = [[5], [2.8, 1]]
un_correct_pyramid_6 = ([3], [9, 2])


# type in the terminal: python3 -m unittest -v pyramid_test
# in order to run all the tests. (only works if the terminal in the pyramid_python directory)
class PyramidTests(unittest.TestCase):

    def test_number_checker(self):
        self.assertFalse(Pyramid.number_check("3"))
        self.assertFalse(Pyramid.number_check(2.3))
        self.assertTrue(Pyramid.number_check(43221))

    def test_input_pyramid_is_correct(self):
        self.assertTrue(Pyramid.input_pyramid_is_correct(correct_pyramid))
        self.assertFalse(Pyramid.input_pyramid_is_correct(un_correct_pyramid_1))
        self.assertFalse(Pyramid.input_pyramid_is_correct(un_correct_pyramid_2))
        self.assertFalse(Pyramid.input_pyramid_is_correct(un_correct_pyramid_3))
        self.assertFalse(Pyramid.input_pyramid_is_correct(un_correct_pyramid_4))
        self.assertFalse(Pyramid.input_pyramid_is_correct(un_correct_pyramid_5))
        self.assertFalse(Pyramid.input_pyramid_is_correct(un_correct_pyramid_6))

    def test_longest_slide_down(self):
        self.assertEqual(Pyramid.longest_slide_down([[7]]), 7)
        with self.assertRaises(Exception):
            Pyramid.longest_slide_down(un_correct_pyramid_3)

    def test_give_bigger(self):
        self.assertEqual(Pyramid.give_bigger([4, 8, 11, 2], 2), 11)
        self.assertEqual(Pyramid.give_bigger([4, 8, 17, 2], 1), 17)

    def test_do_calc(self):
        self.assertEqual(Pyramid.do_calc([2, 2], [1, 2, 3]), [4, 5])
        self.assertEqual(Pyramid.do_calc([2, 1, 6], [11, 9, 3, 2]), [13, 10, 9])

    def test_calculate_longest_slide(self):
        self.assertEqual(Pyramid.calculate_longest_slide(correct_pyramid), correct_pyramid_result)

    def test_calculate_level(self):
        calculated_level_pyramid = correct_pyramid[:]
        calculated_level_pyramid[-2] = correct_before_last_level_calculated_row
        self.assertEqual(Pyramid.calculate_level(correct_pyramid), calculated_level_pyramid)
        correct_pyramid[-2] = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]


if __name__ == '__main__':
    unittest.main()

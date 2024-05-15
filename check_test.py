import unittest
import timeit
from main import check_params
from parameterized import parameterized

class TestCheckFixture(unittest.TestCase):

    def setUp(self):
        self.params = (True, 3, 5, [3, 5, 6, 10, 12])

    def test_check_params_true(self):
        par2, par3, par4, array1 = self.params
        result = check_params(par2, par3, par4, array1)
        self.assertEqual(result, 21)

    def tearDown(self):
        del self.params

class TestCheckExcept(unittest.TestCase):
    def test_check_params_exception(self):
        with self.assertRaises(TypeError):
            check_params("invalid", 3, 5, [3, 5, 6, 10, 12])

class TestCheckTime(unittest.TestCase):

    def test_check_params_performance(self):
        params = (True, 3, 5, [i for i in range(100000)])
        execution_time = timeit.timeit(lambda: check_params(*params), number=1)
        self.assertLess(execution_time, 1)

class TestCheckParams(unittest.TestCase):

    @parameterized.expand([
        (True, 3, 5, [3, 5, 6, 10, 12], 21),
        (False, 2, 7, [1, 4, 14, 52, 2], 14),
        (False, 5, 1, [3, 9, 10, 11, 42], 75)
    ])
    def test_check_params(self, par2, par3, par4, array1, expected):
        result = check_params(par2, par3, par4, array1)
        self.assertEqual(result, expected)

class TestCheckWhitebox(unittest.TestCase):


    def test_par2_true_par3_divisible(self):
        result = check_params(True, 3, 5, [3, 5, 6, 10, 12])
        self.assertEqual(result, 21)

    def test_par2_false_par4_divisible(self):
        result = check_params(False, 2, 7, [1, 4, 14, 52, 2])
        self.assertEqual(result, 14)

    def test_par2_true_par3_not_divisible(self):
        result = check_params(True, 3, 5, [1, 2, 4, 7])
        self.assertEqual(result, 0)

    def test_par2_false_par4_not_divisible(self):
        result = check_params(False, 2, 7, [3, 5, 6, 10, 12])
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()

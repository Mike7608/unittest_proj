import unittest
from utils import arrs

class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 2, "test"), 3)

    def test_get_index_error(self):
        with self.assertRaises(IndexError):
            arrs.get([1, 2, 3], 3)

    def test_get_zero_array(self):
        with self.assertRaises(IndexError):
            arrs.get([], 1)

    def test_get_default(self):
        self.assertEqual(arrs.get([1, 2, 3], -1, "test"), "test")

    def test_my_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])

    def test_my_slice_empty_array(self):
        self.assertEqual(arrs.my_slice([], 1), [])

    def test_my_slice_start(self):
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])

    def test_my_slice_end(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -1), [4])

    def test_my_slice_end_start(self):
        self.assertEqual(arrs.my_slice([1, 2, 3], -5), [1,2,3])

    def test_my_slice_zero(self):
        self.assertEqual(arrs.my_slice([]), [])




if __name__ == '__main__':
    unittest.main()
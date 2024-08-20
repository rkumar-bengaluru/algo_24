import unittest

from solution import Solution

class SolutionTest(unittest.TestCase):

    def test_move_zeroes(self):
        numbers = [0,1,0,3,12]
        expected = [1,3,12,0,0]
        solution = Solution()
        solution.move_zeroes(numbers)
        self.assertEqual(expected, numbers)
    
    def test_move_zeroes_01(self):
        numbers = [0,0]
        expected = [0,0]
        solution = Solution()
        solution.move_zeroes(numbers)
        self.assertEqual(expected, numbers)
    
    def test_move_zeroes_02(self):
        numbers = [1,5,0,3,7,0,8]
        expected = [1,5,3,7,8,0,0]
        solution = Solution()
        solution.move_zeroes(numbers)
        self.assertEqual(expected, numbers)

if __name__ =="__main__":
    unittest.main()

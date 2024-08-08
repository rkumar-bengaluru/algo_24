import unittest

from solution import Solution

class SolutionTest(unittest.TestCase):
    def test_validMountainArray(self):
        s = Solution()
        driver = [1,3,2]
        self.assertEqual(s.validMountainArray(driver), True)
    
    def test_validMountainArray_invalid(self):
        s = Solution()
        driver = [1,3,2,4,5,6,7,8,9]
        self.assertEqual(s.validMountainArray(driver), False)
    
    def test_validMountainArray_invalid1(self):
        s = Solution()
        driver = [2,1]
        self.assertEqual(s.validMountainArray(driver), False)

    def test_validMountainArray_invalid2(self):
        s = Solution()
        driver = [3,5,5]
        self.assertEqual(s.validMountainArray(driver), False)

    def test_validMountainArray_invalid3(self):
        s = Solution()
        driver = [0,3,2,1]
        self.assertEqual(s.validMountainArray(driver), True)
    
    def test_validMountainArray_invalid4(self):
        s = Solution()
        driver = [9,8,7,6,5,4,3,2,1,0]
        self.assertEqual(s.validMountainArray(driver), False)

if __name__ == "__main__":
    unittest.main()
import unittest

from solution import Solution

class SolutionTest(unittest.TestCase):
    
    def test_boats_to_save_01(self):
        people_weights = [3,2,1,2]
        boat_weight_limit = 3
        sol = Solution()
        no_of_boats_required = sol.boats_to_save(people_weights, boat_weight_limit)
        self.assertEqual(3, no_of_boats_required)

    def test_boats_to_save_02(self):
        people_weights = [3,5,3,4]
        boat_weight_limit = 5
        sol = Solution()
        no_of_boats_required = sol.boats_to_save(people_weights, boat_weight_limit)
        self.assertEqual(4, no_of_boats_required)

    def test_boats_to_save_03(self):
        people_weights = [1,2]
        boat_weight_limit = 3
        sol = Solution()
        no_of_boats_required = sol.boats_to_save(people_weights, boat_weight_limit)
        self.assertEqual(1, no_of_boats_required)

if __name__ == "__main__":
    unittest.main()
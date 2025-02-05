import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_leastInterval(self):
        sol = Solution()

        # Test case 1
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 2
        expected = 8
        self.assertEqual(sol.leastInterval(tasks, n), expected)

        # Test case 2
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 0
        expected = 6
        self.assertEqual(sol.leastInterval(tasks, n), expected)

        # Test case 3
        tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
        n = 2
        expected = 16
        self.assertEqual(sol.leastInterval(tasks, n), expected)

        # Test case 4
        tasks = ["A", "B", "C", "A", "B", "C"]
        n = 3
        expected = 7
        self.assertEqual(sol.leastInterval(tasks, n), expected)

        # Test case 5
        tasks = ["A", "A", "A", "B", "C", "C"]
        n = 2
        expected = 7
        self.assertEqual(sol.leastInterval(tasks, n), expected)

if __name__ == '__main__':
    unittest.main()

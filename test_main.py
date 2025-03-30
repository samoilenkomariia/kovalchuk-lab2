import unittest
from main import circular_single_ll

class TestCircularSingleLinkedList(unittest.TestCase):
    def setUp(self):
        self.cll = circular_single_ll()
    
    def test_initial_list(self):
        self.assertIsNone(self.cll.head)
        self.assertEqual(self.cll.length(), 0)


if __name__ == '__main__':
    unittest.main()
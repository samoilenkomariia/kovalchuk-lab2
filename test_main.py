import unittest
from main import circular_single_ll


class TestCircularSingleLinkedList(unittest.TestCase):

    def setUp(self):
        self.cll = circular_single_ll()

    def test_circular_traversal(self):
        self.create_list(5)
        current = self.cll.head
        for _ in range(5):
            current = current.next
        self.assertEqual(current, self.cll.head)

    def create_list(self, input_data):
        if isinstance(input_data, int):
            for i in range(input_data):
                self.cll.append(str(i))
        elif isinstance(input_data, (list, tuple)):
            for v in input_data:
                self.cll.append(v)

    def test_initial_list(self):
        self.assertIsNone(self.cll.head)

    def test_append_empty_list(self):
        self.cll.append('d')
        self.assertEqual(self.cll.head.data, 'd')
        self.assertEqual(self.cll.head, self.cll.head.next)

        self.cll.append('a')
        self.assertEqual(self.cll.head.data, 'd')
        self.assertEqual(self.cll.head.next.data, 'a')
        self.assertEqual(self.cll.head, self.cll.head.next.next)

    def test_append(self):
        self.create_list(4)
        current = self.cll.head
        for i in range(4):
            self.assertEqual(current.data, str(i))
            current = current.next
        self.assertEqual(self.cll.head, current)

    def test_append_invalid_data(self):
        test_cases = [2, 12, ['s'], True, None]
        for t in test_cases:
            with self.subTest(t=t):
                with self.assertRaises(TypeError) as context:
                    self.cll.append(t)
                self.assertEqual(str(context.exception),
                                 "Data must be of type str")

    def test_length(self):
        self.assertEqual(self.cll.length(), 0)

        for i in range(4):
            self.cll.append(str(i))
        self.assertEqual(self.cll.length(), 4)

    def test_insert_non_int_index(self):
        test_cases = ["0", 0.2, None, [0]]
        for i in test_cases:
            with self.subTest(i=i):
                with self.assertRaises(TypeError) as context:
                    self.cll.insert("a", i)
                self.assertEqual(str(context.exception),
                                 "Index must be an integer")

    def test_insert_index_out_of_bounds(self):
        invalid_indices = [-2, 3]

        for i in invalid_indices:
            with self.subTest(i=i):
                with self.assertRaises(IndexError) as context:
                    self.cll.insert("a", i)
                self.assertEqual(str(context.exception),
                                 "Index out of boundaries")

    def test_insert_into_empty_list(self):
        self.cll.insert("a", 0)
        self.assertEqual(self.cll.head, self.cll.head.next)
        self.assertEqual(self.cll.head.data, "a")
        self.assertEqual(self.cll.length(), 1)

    def test_insert_at_end(self):
        self.create_list(5)
        self.cll.insert("b", 5)
        self.assertEqual(self.cll.length(), 6)
        current = self.cll.head.next
        for _ in range(4):
            current = current.next
        self.assertEqual(current.data, "b")
        self.assertEqual(current.next, self.cll.head)

    def test_insert_in_middle(self):
        self.create_list(5)
        self.cll.insert("b", 2)
        self.assertEqual(self.cll.head.next.next.data, "b")
        self.assertEqual(self.cll.length(), 6)

    def test_delete_non_int_index(self):
        self.create_list(5)
        test_cases = ['abcd', '0', [0]]
        for i in test_cases:
            with self.subTest(i=i):
                with self.assertRaises(TypeError) as context:
                    self.cll.delete(i)
                self.assertEqual(str(context.exception),
                                 "Index must be an integer")

    def test_delete_index_out_of_bounds(self):
        with self.assertRaises(IndexError) as context:  # empty list
            self.cll.delete(0)
        self.assertEqual(str(context.exception), "Index out of boundaries")

        self.create_list(5)
        test_cases = [-3, 5, 6]
        for i in test_cases:
            with self.subTest(i=i):
                with self.assertRaises(IndexError) as context:
                    self.cll.delete(i)
                self.assertEqual(str(context.exception),
                                 "Index out of boundaries")

    def test_delete_single_node_list(self):
        self.cll.append('a')
        self.assertEqual(self.cll.delete(0), 'a')
        self.assertEqual(self.cll.length(), 0)

    def test_delete_first(self):
        self.create_list(5)

        current = self.cll.head
        for _ in range(4):
            current = current.next

        node_data = self.cll.head.data
        del_node_data = self.cll.delete(0)
        self.assertEqual(self.cll.length(), 4)
        self.assertEqual(del_node_data, node_data)
        # check if head is updated
        self.assertNotEqual(del_node_data, self.cll.head.data)
        # check if last is pointing to the updated head
        self.assertEqual(current.next, self.cll.head)

    def test_delete_third(self):
        for i in range(5):
            self.cll.append(str(i))
            if i == 0:
                current = self.cll.head
            else:
                current = current.next
                if i == 2:
                    node_data = current.data

        del_node_data = self.cll.delete(2)
        self.assertEqual(self.cll.length(), 4)
        self.assertEqual(del_node_data, node_data)
        # check if new third node is not as deleted one
        self.assertNotEqual(del_node_data, self.cll.head.next.next.data)
        # check if third node is '3' now, not '2'
        self.assertEqual(self.cll.head.next.next.data, '3')

    def test_delete_last(self):
        for i in range(5):
            self.cll.append(str(i))
            if i == 0:
                current = self.cll.head
            else:
                current = current.next
                if i == 3:
                    fourth_node = current

        node_data = current.data
        del_node_data = self.cll.delete(4)
        self.assertEqual(self.cll.length(), 4)
        self.assertEqual(del_node_data, node_data)
        # verify new last node
        self.assertEqual(fourth_node.next, self.cll.head)

    def test_delete_all_empty_list(self):
        self.assertIsNone(self.cll.head)
        try:
            self.cll.delete_all('f')
        except Exception as e:
            self.fail(
                f"detele_all for empty list raised unexpected error: {e}")
        self.assertIsNone(self.cll.head)

    def test_delete_all_invalid_values(self):
        for i in range(4):
            self.cll.append(str(i))

        test_cases = [2, ['d'], None]
        for t in test_cases:
            self.cll.delete_all(t)
        current = self.cll.head
        for i in range(4):
            if current.data != str(i):
                self.fail(
                    f"delete_all_invalid_values: expected {i}, got {current.data}"
                )
            current = current.next

    def test_delete_all(self):
        test_cases = ["a", "b", "b", "a", "a", "c", "a"]
        for t in test_cases:
            self.cll.append(t)
        self.cll.delete_all("a")

        self.assertEqual(self.cll.length(), 3)
        current = self.cll.head
        for _ in range(3):
            with self.subTest():
                self.assertNotEqual(current.data, "a")
            current = current.next

    def test_delete_all_no_matches(self):
        for i in range(3):
            self.cll.append(str(i))

        self.cll.delete_all('3')
        self.assertEqual(self.cll.length(), 3)
        current = self.cll.head
        for _ in range(3):
            with self.subTest():
                self.assertNotEqual(current.data, "a")
            current = current.next

    def test_get_not_int_index(self):
        for i in range(3):
            self.cll.append(str(i))

        test_cases = ['a', None, [0]]
        for i in test_cases:
            with self.subTest(i=i):
                with self.assertRaises(TypeError) as context:
                    self.cll.get(i)
                self.assertEqual(str(context.exception),
                                 "Index must be an integer")

    def test_get_index_out_of_bounds(self):
        with self.assertRaises(IndexError) as context:
            self.cll.get(0)
        self.assertEqual(str(context.exception), "Index out of boundaries")

        for i in range(3):
            self.cll.append(str(i))

        test_cases = [-1, 3, 4]
        for i in test_cases:
            with self.subTest(i=i):
                with self.assertRaises(IndexError) as context:
                    self.cll.get(i)
                self.assertEqual(str(context.exception),
                                 "Index out of boundaries")

    def test_get(self):
        for i in range(5):
            self.cll.append(str(i))

        self.assertEqual(self.cll.get(0), '0')
        self.assertEqual(self.cll.get(1), '1')
        self.assertEqual(self.cll.get(2), '2')
        self.assertEqual(self.cll.get(3), '3')
        self.assertEqual(self.cll.get(4), '4')

    def test_reverse_empty_list(self):
        self.cll.reverse()
        self.assertEqual(self.cll.length(), 0)
        self.assertIsNone(self.cll.head)

    def test_reverse(self):
        self.create_list(5)

        self.cll.reverse()
        #check if new head is former last node
        self.assertEqual(self.cll.head.data, '4')
        current = self.cll.head
        for i in range(4, -1, -1):
            with self.subTest(i=i):
                self.assertEqual(current.data, str(i))
            current = current.next
            # check if last node points to head
            if i == 1:
                self.assertEqual(current.next, self.cll.head)

    def test_reverse_single_node(self):
        self.cll.append('a')
        self.cll.reverse()
        self.assertEqual(self.cll.head.next, self.cll.head)

    def test_clone_empty_list(self):
        copy = self.cll.clone()
        self.assertEqual(copy.length(), 0)
        self.assertIsNone(copy.head)

    def test_clone(self):
        for i in range(5):
            self.cll.append(str(i))
        copy = self.cll.clone()
        current_copy = copy.head
        current = self.cll.head
        for _ in range(5):
            with self.subTest():
                self.assertEqual(current_copy.data, current.data)
            current = current.next
            current_copy = current_copy.next

    def test_find_first(self):
        self.assertEqual(self.cll.find_first('a'), -1)

        values = ['0', 'a', 'a', '2', 'a']
        for v in values:
            self.cll.append(v)

        self.assertEqual(self.cll.find_first('a'), 1)
        self.assertEqual(self.cll.find_first('b'), -1)

    def test_find_last(self):
        self.assertEqual(self.cll.find_last('c'), -1)

        values = ['c', 'a', 'c', 'c', 'a']
        for v in values:
            self.cll.append(v)

        self.assertEqual(self.cll.find_last('c'), 3)
        self.assertEqual(self.cll.find_last('b'), -1)

    def test_clear(self):
        self.cll.clear()
        self.assertEqual(self.cll.length(), 0)

        for i in range(5):
            self.cll.append(str(i))
        self.assertEqual(self.cll.length(), 5)
        self.cll.clear()
        self.assertEqual(self.cll.length(), 0)
        self.assertIsNone(self.cll.head)

    def test_extend(self):
        self.cll.extend(circular_single_ll())
        self.assertEqual(self.cll.length(), 0)

        list = circular_single_ll()
        for i in range(5):
            list.append(str(i))

        self.cll.extend(list)
        self.assertEqual(self.cll.length(), 5)
        current = self.cll.head
        for i in range(5):
            with self.subTest(i=i):
                self.assertEqual(current.data, str(i))
            current = current.next

        list.delete(0)
        self.assertEqual(list.length(), 4)
        self.assertEqual(self.cll.length(), 5)

        self.cll.extend(list)
        self.assertEqual(self.cll.length(), 9)
        current = self.cll.head
        for i in range(5):
            with self.subTest(i=i):
                self.assertEqual(current.data, str(i))
            current = current.next
            if i == 4:
                i = 1


if __name__ == '__main__':
    unittest.main()

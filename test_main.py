import unittest
from main import circular_single_ll


class TestCircularSingleLinkedList(unittest.TestCase):

    def setUp(self):
        self.cll = circular_single_ll()

    def test_circular_traversal(self):
        self.create_list(5)
        for i in range(5):
            with self.subTest(i=i):
                if i < 4:
                    self.assertEqual(self.cll.list[i].next, i + 1)
                else:
                    self.assertEqual(self.cll.list[i].next, 0)

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
        self.assertEqual(self.cll.head.next, 0)

        self.cll.append('a')
        self.assertEqual(self.cll.head.data, 'd')
        self.assertEqual(self.cll.head.next, 1)
        self.assertEqual(self.cll.list[1].data, 'a')
        self.assertEqual(self.cll.list[1].next, 0)

    def test_append(self):
        self.create_list(4)
        for i in range(4):
            self.assertEqual(self.cll.list[i].data, str(i))
        self.assertEqual(self.cll.head, self.cll.list[0])

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
        self.assertEqual(self.cll.head.data, "a")
        self.assertEqual(self.cll.head.next, 0)
        self.assertEqual(self.cll.length(), 1)

    def test_insert_at_end(self):
        self.create_list(5)
        self.cll.insert("b", 5)
        self.assertEqual(self.cll.length(), 6)
        self.assertEqual(self.cll.list[5].data, "b")
        self.assertEqual(self.cll.list[5].next, 0)

    def test_insert_in_middle(self):
        self.create_list(5)
        self.cll.insert("b", 2)
        self.assertEqual(self.cll.list[2].data, "b")
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

        del_node_data = self.cll.delete(0)
        self.assertEqual(self.cll.length(), 4)
        # check if head is updated
        self.assertNotEqual(del_node_data, self.cll.head.data)
        # check if last is pointing to the updated head
        self.assertEqual(self.cll.list[self.cll.length() - 1].next, 0)

    def test_delete_third(self):
        self.create_list(5)

        del_node_data = self.cll.delete(2)
        self.assertEqual(self.cll.length(), 4)
        # check if new third node is not as deleted one
        self.assertNotEqual(del_node_data, self.cll.list[2].data)
        # check if third node is '3' now, not '2'
        self.assertEqual(self.cll.list[2].data, '3')

    def test_delete_last(self):
        self.create_list(5)

        del_node_data = self.cll.delete(4)
        self.assertEqual(self.cll.length(), 4)
        # verify new last node
        self.assertNotEqual(del_node_data, self.cll.list[3].data)
        self.assertEqual(self.cll.list[3].next, 0)

    def test_delete_all_empty_list(self):
        self.assertIsNone(self.cll.head)
        try:
            self.cll.delete_all('f')
        except Exception as e:
            self.fail(
                f"detele_all for empty list raised unexpected error: {e}")
        self.assertIsNone(self.cll.head)

    def test_delete_all_invalid_values(self):
        self.create_list(4)

        test_cases = [2, ['d'], None]
        for t in test_cases:
            self.cll.delete_all(t)
        current = self.cll.head
        for i in range(4):
            if self.cll.list[i].data != str(i):
                self.fail(
                    f"delete_all_invalid_values: expected {i}, got {current.data}"
                )

    def test_delete_all(self):
        test_cases = ["a", "b", "b", "a", "a", "c", "a"]
        self.create_list(test_cases)

        self.cll.delete_all("a")
        self.assertEqual(self.cll.length(), 3)
        for i in range(3):
            with self.subTest(i=i):
                self.assertNotEqual(self.cll.list[i].data, "a")

    def test_delete_all_no_matches(self):
        self.create_list(3)

        self.cll.delete_all("3")
        self.assertEqual(self.cll.length(), 3)
        for i in range(3):
            with self.subTest(i=i):
                self.assertNotEqual(self.cll.list[i].data, "a")

    def test_get_not_int_index(self):
        self.create_list(3)

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

        self.create_list(3)

        test_cases = [-1, 3, 4]
        for i in test_cases:
            with self.subTest(i=i):
                with self.assertRaises(IndexError) as context:
                    self.cll.get(i)
                self.assertEqual(str(context.exception),
                                 "Index out of boundaries")

    def test_get(self):
        self.create_list(5)

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
        index = 0
        for i in range(4, -1, -1):
            with self.subTest(i=i, index=index):
                self.assertEqual(self.cll.list[index].data, str(i))
            # check if last node points to head
            if i == 1:
                self.assertEqual(self.cll.list[self.cll.length() - 1].next, 0)
            index += 1

    def test_reverse_single_node(self):
        self.cll.append('a')
        self.cll.reverse()
        self.assertEqual(self.cll.list[0].data, 'a')
        self.assertEqual(self.cll.head.next, 0)

    def test_clone_empty_list(self):
        copy = self.cll.clone()
        self.assertEqual(copy.length(), 0)
        self.assertIsNone(copy.head)

    def test_clone(self):
        for i in range(5):
            self.cll.append(str(i))
        copy = self.cll.clone()
        self.assertEqual(copy.length(), self.cll.length())
        for i in range(5):
            with self.subTest(i=i):
                self.assertEqual(copy.list[i].data, self.cll.list[i].data)

    def test_find_first(self):
        self.assertEqual(self.cll.find_first('a'), -1)

        values = ['0', 'a', 'a', '2', 'a']
        self.create_list(values)

        self.assertEqual(self.cll.find_first('a'), 1)
        self.assertEqual(self.cll.find_first('b'), -1)

    def test_find_last(self):
        self.assertEqual(self.cll.find_last('c'), -1)

        values = ['c', 'a', 'c', 'c', 'a']
        self.create_list(values)

        self.assertEqual(self.cll.find_last('c'), 3)
        self.assertEqual(self.cll.find_last('b'), -1)

    def test_clear(self):
        self.cll.clear()
        self.assertEqual(self.cll.length(), 0)

        self.create_list(5)
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
        for i in range(5):
            with self.subTest(i=i):
                self.assertEqual(self.cll.list[i].data, str(i))

        list.delete(0)
        self.assertEqual(list.length(), 4)
        self.assertEqual(self.cll.length(), 5)

        self.cll.extend(list)
        self.assertEqual(self.cll.length(), 9)
        i = 0
        for value in range(5):
            with self.subTest(i=i, value=value):
                self.assertEqual(self.cll.list[i].data, str(value))
            if value == 4:
                value = 1
            i += 1


if __name__ == '__main__':
    unittest.main()

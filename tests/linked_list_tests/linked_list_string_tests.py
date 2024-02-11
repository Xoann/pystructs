from src.pystructs.linked_list import LinkedList
import unittest


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.test_list = [1, 2, 3]
        self.linked_list = LinkedList(self.test_list)

    def test_linked_list_initialization(self):
        self.assertEqual(len(self.linked_list), len(self.test_list))

        i = 0
        curr = self.linked_list.head
        while curr is not None:
            self.assertEqual(curr.value, self.test_list[i])
            i += 1
            curr = curr.next

    def test_linked_list_string_representation(self):
        string_rep = str(self.linked_list)
        self.assertEqual(string_rep, "1 -> 2 -> 3")
        empty_linked_list = LinkedList()
        self.assertEqual(str(empty_linked_list), "None")

    def test_linked_list_get_item(self):
        for i in range(len(self.test_list)):
            self.assertEqual(self.test_list[i], self.linked_list[i])

    def test_linked_list_get_slice(self):
        long_linked_list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])

        sliced_list = long_linked_list[1:4]
        self.assertTrue(sliced_list == [2, 3, 4])

        sliced_list = long_linked_list[:4]
        self.assertTrue(sliced_list == [1, 2, 3, 4])

        sliced_list = long_linked_list[4:]
        self.assertTrue(sliced_list == [5, 6, 7, 8, 9])

        sliced_list = long_linked_list[:]
        self.assertTrue(sliced_list == [1, 2, 3, 4, 5, 6, 7, 8, 9])

        sliced_list = long_linked_list[::2]
        self.assertTrue(sliced_list == [1, 3, 5, 7, 9])

        sliced_list = long_linked_list[::-1]
        self.assertTrue(sliced_list == [9, 8, 7, 6, 5, 4, 3, 2, 1])

        sliced_list = long_linked_list[1:6:-2]
        self.assertTrue(sliced_list == [6, 4, 2])

    def test_linked_list_set_item(self):
        self.linked_list[1] = 99
        self.assertEqual(self.linked_list[1], 99)
        self.linked_list[1] = 2

    def test_linked_list_iterator(self):
        i = 0
        for item in self.linked_list:
            self.assertEqual(item, self.test_list[i])
            i += 1

        i = 0
        for node in self.linked_list.__iter__(return_nodes=True):
            self.assertEqual(node.value, self.test_list[i])
            i += 1

        i = 0
        for curr, prev in self.linked_list.__iter__(return_prev=True):
            self.assertEqual(curr.value, self.test_list[i])
            if prev is not None:
                self.assertEqual(prev.value, self.test_list[i - 1])
            i += 1

    def test_linked_list_contains(self):
        self.assertTrue(1 in self.linked_list)
        self.assertFalse(0 in self.linked_list)

    def test_linked_linked_eq(self):
        self.assertTrue(self.linked_list == self.test_list)
        self.test_list[1] = 99
        self.assertFalse(self.linked_list == self.test_list)
        self.test_list[1] = 2

    def test_linked_list_neq(self):
        self.assertFalse(self.linked_list != self.test_list)
        self.test_list[1] = 99
        self.assertTrue(self.linked_list != self.test_list)
        self.test_list[1] = 2

    def test_linked_list_lt(self):
        greater_list = [2, 3, 4]
        greater_linked_list = LinkedList(greater_list)

        smaller_list = [0, 1, 2]
        smaller_linked_list = LinkedList(smaller_list)

        empty_list = []
        empty_linked_list = LinkedList()

        self.assertRaises(TypeError, self.linked_list.__lt__, 0)
        self.assertRaises(TypeError, self.linked_list.__lt__, {1, 2, 3})
        self.assertFalse(empty_linked_list < empty_list)
        self.assertTrue(empty_linked_list < smaller_linked_list)
        self.assertFalse(smaller_linked_list < empty_list)
        self.assertTrue(smaller_linked_list < self.linked_list)
        self.assertTrue(smaller_linked_list < greater_linked_list)

    def test_linked_list_le(self):
        greater_list = [2, 3, 4]
        greater_linked_list = LinkedList(greater_list)

        smaller_list = [0, 1, 2]
        smaller_linked_list = LinkedList(smaller_list)

        empty_list = []
        empty_linked_list = LinkedList()

        self.assertRaises(TypeError, self.linked_list.__le__, 0)
        self.assertRaises(TypeError, self.linked_list.__le__, {1, 2, 3})
        self.assertTrue(empty_linked_list <= empty_list)
        self.assertTrue(empty_linked_list <= smaller_linked_list)
        self.assertFalse(smaller_linked_list <= empty_list)
        self.assertTrue(smaller_linked_list <= self.linked_list)
        self.assertTrue(smaller_linked_list <= smaller_list)
        self.assertTrue(smaller_linked_list <= greater_linked_list)

    def test_linked_list_gt(self):
        greater_list = [2, 3, 4]
        greater_linked_list = LinkedList(greater_list)

        smaller_list = [0, 1, 2]
        smaller_linked_list = LinkedList(smaller_list)

        empty_list = []
        empty_linked_list = LinkedList()

        self.assertRaises(TypeError, self.linked_list.__gt__, 0)
        self.assertRaises(TypeError, self.linked_list.__gt__, {1, 2, 3})
        self.assertFalse(empty_linked_list > empty_list)
        self.assertFalse(empty_linked_list > greater_linked_list)
        self.assertTrue(greater_linked_list > empty_list)
        self.assertTrue(greater_linked_list > self.linked_list)
        self.assertFalse(smaller_linked_list > greater_linked_list)

    def test_linked_list_ge(self):
        greater_list = [2, 3, 4]
        greater_linked_list = LinkedList(greater_list)

        smaller_list = [0, 1, 2]
        smaller_linked_list = LinkedList(smaller_list)

        empty_list = []
        empty_linked_list = LinkedList()

        self.assertRaises(TypeError, self.linked_list.__ge__, 0)
        self.assertRaises(TypeError, self.linked_list.__ge__, {1, 2, 3})
        self.assertTrue(empty_linked_list >= empty_list)
        self.assertFalse(empty_linked_list >= greater_linked_list)
        self.assertTrue(greater_linked_list >= empty_list)
        self.assertTrue(greater_linked_list >= self.linked_list)
        self.assertFalse(smaller_linked_list >= greater_linked_list)

    def test_linked_list_insert(self):
        self.linked_list.insert(0, 0)
        self.assertTrue(self.linked_list == [0, 1, 2, 3])
        self.linked_list.insert(len(self.linked_list), 99)
        self.assertTrue(self.linked_list == [0, 1, 2, 3, 99])
        self.linked_list.insert(2, 100)
        self.assertTrue(self.linked_list == [0, 1, 100, 2, 3, 99])
        self.linked_list.insert(-100, -1)
        self.assertTrue(self.linked_list == [-1, 0, 1, 100, 2, 3, 99])
        self.linked_list.insert(100, 55)
        self.assertTrue(self.linked_list == [-1, 0, 1, 100, 2, 3, 99, 55])
        self.assertTrue(len(self.linked_list) == 9)

    def test_linked_list_append(self):
        self.linked_list.append(10)
        self.assertTrue(self.linked_list == [1, 2, 3, 10])
        self.assertTrue(len(self.linked_list) == 4)

    def test_linked_list_remove(self):
        self.assertRaises(ValueError, self.linked_list.remove, 10)
        self.linked_list.remove(2)
        self.assertTrue(self.linked_list == [1, 3])
        self.assertTrue(len(self.linked_list) == 2)

    def test_linked_list_pop(self):
        empty_linked_list = LinkedList()
        self.assertRaises(IndexError, empty_linked_list.pop, 0)
        self.assertRaises(IndexError, self.linked_list.pop, 100)
        self.assertRaises(IndexError, self.linked_list.pop, -100)

        self.assertEqual(self.linked_list.pop(), 1)
        self.assertTrue(self.linked_list == [2, 3])
        self.assertEqual(self.linked_list.pop(-1), 3)
        self.assertTrue(self.linked_list == [2])

        self.assertTrue(len(self.linked_list) == 1)

    def test_linked_list_clear(self):
        self.linked_list.clear()
        self.assertTrue(self.linked_list == [])
        self.assertTrue(len(self.linked_list) == 0)

    def test_linked_list_index(self):
        self.assertRaises(ValueError, self.linked_list.index, 10)


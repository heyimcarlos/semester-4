import unittest

from singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = SinglyLinkedList()

    def test_is_empty(self):
        self.assertTrue(self.list.is_empty())
        self.assertEqual(self.list.len(), 0)

    def test_push_back(self):
        self.list.push_back(1)
        self.assertFalse(self.list.is_empty())
        self.assertEqual(self.list.len(), 1)
        self.assertTrue(self.list.contains(1))
        self.list.push_back(2)
        self.assertEqual(self.list.len(), 2)

    def test_push_front(self):
        self.list.push_front(1)
        self.assertFalse(self.list.is_empty())
        self.assertEqual(self.list.len(), 1)
        self.assertTrue(self.list.contains(1))
        self.list.push_front(2)
        self.assertEqual(self.list.len(), 2)

    def test_pop_back(self):
        self.list.push_front(1)
        self.assertFalse(self.list.is_empty())
        self.assertEqual(self.list.len(), 1)
        self.assertTrue(self.list.contains(1))
        detached = self.list.pop_back()
        if detached:
            self.assertEqual(detached.get_element(), 1)
        self.assertTrue(self.list.is_empty())

    def test_pop_front(self):
        self.list.push_front(1)
        self.assertFalse(self.list.is_empty())
        self.assertEqual(self.list.len(), 1)
        self.assertTrue(self.list.contains(1))
        detached = self.list.pop_front()
        if detached:
            self.assertEqual(detached.get_element(), 1)
        self.assertTrue(self.list.is_empty())

    def test_concat(self):
        self.list.push_back(1)
        self.list.push_back(2)
        self.list.push_back(3)

        other_list = SinglyLinkedList()
        other_list.push_back(4)
        other_list.push_back(5)

        print("Testing Concat Method")
        print("Original")
        print(self.list)
        print(other_list)

        self.list.concat(other_list)

        print("after concat")
        print(self.list)
        print(other_list)

        self.assertTrue(other_list.is_empty())
        self.assertEqual(self.list.len(), 5)
        print("End Testing Concat Method \n")

    def test_swap(self):
        self.list.push_back(1)
        self.list.push_back(2)
        self.list.push_back(3)
        self.list.push_back(4)
        self.list.push_back(5)

        print("Testing Swap Original")
        print(f"swapping {self.list.front()._next} and {self.list.back()}")
        print(self.list)

        head = self.list.front()
        node2 = self.list.back()
        if head and node2:
            node1 = head._next
            if node1:
                self.list.swap(node1, node2)

        print(self.list)
        print("End Testing Swap")


if __name__ == "__main__":
    unittest.main()

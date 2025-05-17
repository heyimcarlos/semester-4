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


if __name__ == "__main__":
    unittest.main()

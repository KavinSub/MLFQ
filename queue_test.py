import unittest

from queue import Queue



class TestQueueMethods(unittest.TestCase):
    
    def test_length(self):
        queue = Queue()

        expected_length = 0
        self.assertEqual(len(queue), expected_length)

        items = [1, 2, 3, 4, 5]

        for item in items:
            queue.enqueue(item)
            expected_length += 1
            self.assertEqual(len(queue), expected_length)

        while expected_length > 0:
            queue.dequeue()
            expected_length -= 1
            self.assertEqual(len(queue), expected_length)
    
    def test_operations(self):
        queue = Queue()

        items = [1, 2, 3, 4, 5]

        self.assertEqual(queue.to_list(), [])

        for i, item in enumerate(items):
            queue.enqueue(item)
            self.assertEqual(queue.to_list(), items[:i + 1])
        
        i = 0
        while len(queue) > 0:
            self.assertEqual(queue.dequeue(), items[i])
            self.assertEqual(queue.to_list(), items[i + 1:])
            i += 1
        


if __name__ == '__main__':
    unittest.main()
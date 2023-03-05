import unittest
from hw_3.custom_queue import Queue


class TestQueueMark(unittest.TestCase):
    """Проверка границ очереди"""
    def test_head_tail_mark(self):
        queue = Queue()
        assert queue.head is None
        assert queue.tail is None


class TestQueueEnqueue(unittest.TestCase):
    """Проверка постановки в очередь и ее порядка"""
    def test_queue_Enqueue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        assert queue.head.data == 'data1'
        assert queue.head.next_node.data == 'data2'
        assert queue.tail.data == 'data3'
        assert queue.tail.next_node is None


class TestQueueDequeue(unittest.TestCase):
    """Проверка извлечения из очередь и ее границы"""
    def test_queue_Dequeue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        assert queue.dequeue() == 'data1'
        assert queue.dequeue() == 'data2'
        assert queue.dequeue() == 'data3'
        assert queue.dequeue() is None

import unittest
from hw_3.utils import Node, Stack


class TestNode(unittest.TestCase):
    """Тест класса Node"""

    def test_node_init(self):
        """Проверка данных и границы стека"""
        node_10 = Node(10)
        assert node_10.data == 10
        assert node_10.next_node is None

    def test_node_inext_node(self):
        """Проверка, что next_node ссылается на узел"""
        node_10 = Node(10)
        node2 = Node(222, node_10)
        assert node2.next_node is node_10


class TestStack(unittest.TestCase):
    """Проверка данных и границы стека"""
    def test_stack_top(self):
        node = Node(None)
        stack = Stack(node)
        stack.push('data1')
        stack.push('data2')
        assert stack.top.data == 'data2'
        assert stack.top.next_node.data == 'data1'
        assert stack.top.next_node.next_node.data is None

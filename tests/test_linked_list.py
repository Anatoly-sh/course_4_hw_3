import unittest
from hw_3.linked_list import Node, LinkedList


class TestNode(unittest.TestCase):
    """Тест класса Node"""

    def test_node_init(self):
        """Проверка данных и связи с соседним узлом """
        node_10 = Node(10)
        assert node_10.data == 10
        assert node_10.next_node is None

    def test_node_next_node(self):
        """Проверка, что next_node ссылается на узел"""
        node_10 = Node(10)
        node2 = Node(222, node_10)
        assert node2.next_node is node_10


class TestLinkedListMark(unittest.TestCase):
    """Проверка границ списка при его инициации"""
    def test_mark(self):
        ll = LinkedList()
        assert ll.start_point is None
        assert ll.end_point is None


class TestInsertBeginning(unittest.TestCase):
    """Проверка постановки в список в нвчале"""
    def test_ll_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 11})
        ll.insert_beginning({'id': 22})
        ll.insert_beginning({'id': 33})
        assert ll.start_point.data == {'id': 33}
        assert ll.start_point.next_node.data == {'id': 22}
        assert ll.start_point.next_node.next_node.data == {'id': 11}


class TestInsertAtEnd(unittest.TestCase):
    """Проверка постановки в список в конце"""
    def test_ll_insert_at_end(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 11})
        ll.insert_at_end({'id': 22})
        ll.insert_at_end({'id': 33})
        assert ll.start_point.data == {'id': 11}
        assert ll.start_point.next_node.data == {'id': 22}
        assert ll.start_point.next_node.next_node.data == {'id': 33}



class TestToListAndGet(unittest.TestCase):
    def test_to_list_and_get_data(self):
        lll = LinkedList()
        lll.insert_beginning({'id': 1})
        lll.insert_at_end({'id': 2})
        lll.insert_at_end({'id': 3})
        lll.insert_beginning({'id': 0})

        """Ожидается list с данными односвязного списка"""
        assert isinstance(lll.to_list(), list)

        """Ожидается получение первого найденного словаря по ключу"""
        assert lll.get_data_by_id(2) == "{'id': 2}"
        assert lll.get_data_by_id(4) is None


class Node:
    """Класс узла с данными и адресом соседнего узла"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс связанного списка"""

    def __init__(self, start_point=None, end_point = None):
        self.start_point = start_point
        self.end_point = end_point

    def insert_beginning(self, data):
        """ Тут добавление элемента в начале"""
        new_node = Node(data, self.start_point)
        new_node.nextnode = self.start_point
        self.start_point = new_node

    def insert_at_end(self, data):
        """Тут добавление элемента в конце"""
        new_node = Node(data)
        if self.end_point is not None:
            self.end_point.next_node = new_node
            self.end_point = new_node

    def print_ll(self):
        ll_string = ''
        node = self.start_point
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node
        ll_string += ' None'
        print(ll_string)


if __name__ == '__main__':
    ll = LinkedList()

    ll.insert_beginning({'id': 3})
    ll.insert_beginning({'id': 2})
    ll.insert_beginning({'id': 1})
    ll.insert_at_end({'id': 5})
    ll.insert_at_end({'id': 6})
    ll.insert_beginning({'id': 0})
    ll.print_ll()
    # {'id': 0}-> {'id': 1} -> {'id': 2} -> {'id': 3} -> None
    print(ll.end_point)
    print(ll.start_point.data)

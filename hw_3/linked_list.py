class Node:
    """Класс узла с данными и адресом соседнего узла"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс связанного списка"""
    current_node = None

    def __init__(self, start_point=None, end_point=None):
        self.start_point = start_point
        self.end_point = end_point

    def insert_beginning(self, data):
        """ Тут добавление элемента в начале списка"""
        new_node = Node(data, self.start_point)
        self.start_point = new_node
        if self.end_point is None:
            self.end_point = new_node
            LinkedList.current_node = new_node

    def insert_at_end(self, data):
        """Тут добавление элемента в конце списка"""
        new_node = Node(data)
        if LinkedList.current_node is not None:
            LinkedList.current_node.next_node = new_node
        self.end_point = new_node
        LinkedList.current_node = new_node
        if self.start_point is None:
            self.start_point = new_node

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

    ll.insert_beginning({'id': 1})
    ll.insert_at_end({'id': 2})
    ll.insert_at_end({'id': 3})
    ll.insert_beginning({'id': 0})
    ll.print_ll()
    # {'id': 0}-> {'id': 1} -> {'id': 2} -> {'id': 3} -> None

    node = ll.start_point
    print(node.data)
    print(ll.start_point.data)
    print(ll.start_point.next_node.data)
    print(ll.start_point.next_node.next_node.data)
    print(ll.start_point.next_node.next_node.next_node.data)



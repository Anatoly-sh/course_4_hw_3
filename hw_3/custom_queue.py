class Node:
    """Класс узла с данными и адресом соседнего узла"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс очереди"""
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        """Помещает данные в очередь"""
        new_node = Node(data, self.tail)
        self.tail = new_node
        if self.head is None:
            self.head = new_node

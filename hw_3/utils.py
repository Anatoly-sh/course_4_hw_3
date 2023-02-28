class Node:
    """Класс узла с данными и адресом соседнего узла"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс стека FILO"""

    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        """ Тут добавление элемента """
        new_node = Node(data, self.top)
        self.top = new_node

    def pop(self):
        """Извлечение элемента"""
        pop_adr = self.top
        self.top = self.top.next_node
        return pop_adr.data

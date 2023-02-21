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


if __name__ == '__main__':
    node = Node(None)
    stack = Stack(node)  # инициализация, граница стека - None

    # тестовый прогон
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')
    print(stack.pop(), 'pop')
    print(stack.pop(), 'pop')

    print(stack.top.data)
    print(stack.top.next_node.data)
    # print(stack.top.next_node.next_node.data)
    # print(stack.top.next_node.next_node.next_node.data)

    # n1 = Node(5, None)
    # n2 = Node('a', n1)
    # print(n1.data)
    # print(n2.data)
    # print(n1)
    # print(n2.next_node)

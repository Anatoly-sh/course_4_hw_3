

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        """ Тут добавление элемента """
        new_node = Node(data, self.top)
        self.top = new_node

node = Node('init')

stack = Stack(node)

stack.push('data1')
stack.push('data2')
stack.push('data3')
stack.push('data4')

print(stack.top.data)
print(stack.top.next_node.data)
print(stack.top.next_node.next_node.data)
print(stack.top.next_node.next_node.next_node.data)

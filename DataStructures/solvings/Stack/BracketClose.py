class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def IsBalanced(sequence: str) -> bool:
    stack = Stack()
    for char in sequence:
        if char in ('(', '[', '{'):
            stack.push(char)
        else:
            if stack.is_empty():
                return False
            top = stack.pop()
            if (top == '(' and char != ')') or (top == '[' and char != ']') or (top == '{' and char != '}'):
                return False
    return stack.is_empty()


brackets1 = '(()]{}[]'  # False
brackets2 = '(((()))){[()]}'    # True
print(IsBalanced(brackets1), IsBalanced(brackets2), sep='\n')

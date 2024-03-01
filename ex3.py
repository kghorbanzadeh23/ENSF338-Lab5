
#1
class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from an empty stack")

    def is_empty(self):
        return len(self.stack) == 0

# Test the implementation
stack = ArrayStack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", stack.stack)  # Should print: [1, 2, 3]

popped = stack.pop()
print("Popped:", popped)  # Should print: 3
print("Stack:", stack.stack)  # Should print: [1, 2]

#2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            raise IndexError("pop from an empty stack")
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

    def is_empty(self):
        return self.head is None

# Test the implementation
ll_stack = LinkedListStack()
ll_stack.push(1)
ll_stack.push(2)
ll_stack.push(3)
print("Linked List Stack (top to bottom):", ll_stack.head.data, ll_stack.head.next.data, ll_stack.head.next.next.data)

popped_ll = ll_stack.pop()
print("Popped from Linked List Stack:", popped_ll)  # Should print: 3
print("Linked List Stack (after pop):", ll_stack.head.data, ll_stack.head.next.data)

#3
import random

def generate_random_tasks():
    tasks = []
    for _ in range(10000):
        task = "push" if random.random() < 0.7 else "pop"
        tasks.append(task)
    return tasks

# Test the function
random_tasks = generate_random_tasks()
print("Example Random Tasks:", random_tasks[:10])  # Print first 10 tasks

#4
import timeit

# Measure performance of ArrayStack
array_stack_setup = "from __main__ import ArrayStack, generate_random_tasks"
array_stack_time = timeit.timeit(
    "stack = ArrayStack()\nfor task in tasks:\n\tif task == 'push':\n\t\tstack.push(1)\n\telse:\n\t\tstack.pop()",
    setup=array_stack_setup + "\ntasks = generate_random_tasks()",
    number=100
)

# Measure performance of LinkedListStack
ll_stack_setup = "from __main__ import LinkedListStack, generate_random_tasks"
ll_stack_time = timeit.timeit(
    "stack = LinkedListStack()\nfor task in tasks:\n\tif task == 'push':\n\t\tstack.push(1)\n\telse:\n\t\tstack.pop()",
    setup=ll_stack_setup + "\ntasks = generate_random_tasks()",
    number=100
)

print("ArrayStack Time:", array_stack_time)
print("LinkedListStack Time:", ll_stack_time)
#5
import matplotlib.pyplot as plt

# Data for plotting
times = [array_stack_time, ll_stack_time]
labels = ['ArrayStack', 'LinkedListStack']

# Create bar plot
plt.bar(labels, times, color=['blue', 'green'])
plt.xlabel('Stack Implementation')
plt.ylabel('Time (seconds)')
plt.title('Performance of ArrayStack vs LinkedListStack')
plt.show()


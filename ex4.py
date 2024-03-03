import random
import timeit
import matplotlib.pyplot as plt

# Queue implementations

class ArrayQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("dequeue from empty queue")

    def is_empty(self):
        return len(self.items) == 0

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedListQueueCorrected:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def dequeue(self):
        if self.head is None:
            raise IndexError("dequeue from empty queue")
        temp = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            prev = None
            while temp.next:
                prev = temp
                temp = temp.next
            self.tail = prev
            if self.tail:
                self.tail.next = None
        return temp.data

    def is_empty(self):
        return self.head is None

# Function to generate random tasks
def generate_tasks(n=10000, enqueue_prob=0.7):
    return ["enqueue" if random.random() < enqueue_prob else "dequeue" for _ in range(n)]

# Performance test
def performance_test(queue_type):
    task_lists = [generate_tasks() for _ in range(100)]
    times = []

    for tasks in task_lists:
        queue = queue_type()
        start_time = timeit.default_timer()
        
        for task in tasks:
            if task == "enqueue":
                queue.enqueue(random.randint(1, 100))
            else:
                if not queue.is_empty():
                    queue.dequeue()

        end_time = timeit.default_timer()
        times.append(end_time - start_time)

    return times

# Measure performance
array_queue_times = performance_test(ArrayQueue)
linked_list_queue_times = performance_test(LinkedListQueueCorrected)

# Plotting the distribution of times
plt.figure(figsize=(10, 6))
plt.hist(array_queue_times, bins=20, alpha=0.5, label='ArrayQueue')
plt.hist(linked_list_queue_times, bins=20, alpha=0.5, label='LinkedListQueueCorrected')
plt.legend(loc='upper right')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.title('Performance Distribution of Queue Implementations')
plt.savefig('ex4.jpeg')

'''
Depending on the specific operations (enqueue and dequeue) and their complexity
in each implementation, one might outperform the other. The ArrayQueue's insert(0, item)
operation has a linear complexity because it needs to move all other elements. Conversely,
the LinkedListQueue can add an element at the head in constant time, but removing an element
from the tail requires traversing the list unless it's the only element.
'''

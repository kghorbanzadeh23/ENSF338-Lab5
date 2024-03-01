import random
import timeit

class ArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = -1
        self.tail = -1

    def enqueue(self, item):
        if (self.tail + 1) % self.capacity == self.head:
            print("Queue is full. Unable to enqueue item.")
            return
        elif self.is_empty():
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = item
        self.merge_sort(self.queue)
    
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]

            self.merge_sort(L)
            self.merge_sort(R)

            i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Unable to dequeue item.")
            return None
        item = self.queue[self.head]
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.capacity
        return item
    
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        if len(self.queue) == 0:
            self.queue.append(item)
        else:
            index = 0
            while index < len(self.queue) and self.queue[index] < item:
                index += 1
            self.queue.insert(index, item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Unable to dequeue item.")
            return None
        return self.queue.pop(0)
    
    def is_empty(self):
        return self.head == -1
    
def generate_random_tasks():
    tasks = []
    for i in range(1000):
        if random.random() < 0.7:
            tasks.append("enqueue")
        else:
            tasks.append("dequeue")
        return tasks
    
num_lists = 100
sort_time = timeit.timeit(stmt="pq.enqueue('task')", setup="from __main__ import ArrayQueue; pq = ArrayQueue(1000); import random; random.seed(42); tasks = generate_random_tasks()", globals=globals(), number=num_lists)
insert_time = timeit.timeit(stmt="pq.enqueue('task')", setup="from __main__ import PriorityQueue; pq = PriorityQueue(); import random; random.seed(42); tasks = generate_random_tasks()", globals=globals(), number=num_lists)

print("Time taken for ArrayQueue with sorting:", sort_time)
print("Time taken for PriorityQueue with insertion:", insert_time)
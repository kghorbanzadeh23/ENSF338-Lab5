import random
import timeit

class PriorityQueueMergeSort:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)
        self.queue = self.merge_sort(self.queue)
    
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)
    
    def merge_sort(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            left_half = array[:mid]
            right_half = array[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    array[k] = left_half[i]
                    i += 1
                else:
                    array[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                array[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                array[k] = right_half[j]
                j += 1
                k += 1
        return array

class PriorityQueueSortedInsert:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        if not self.queue:
            self.queue.append(value)
        else:
            for i in range(len(self.queue)):
                if value < self.queue[i]:
                    self.queue.insert(i, value)
                    break
            else:
                self.queue.append(value)
    
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

def generate_tasks():
    tasks = []
    for _ in range(1000):
        if random.random() < 0.7:
            tasks.append(('enqueue', random.randint(0, 100)))
        else:
            tasks.append(('dequeue', None))
    return tasks

def execute_tasks(tasks, pq_class):
    pq = pq_class()
    for operation, value in tasks:
        if operation == 'enqueue':
            pq.enqueue(value)
        elif operation == 'dequeue':
            pq.dequeue()

def measure_performance(task_lists, pq_class):
    times = []
    for tasks in task_lists:
        start_time = timeit.default_timer()
        execute_tasks(tasks, pq_class)
        end_time = timeit.default_timer()
        times.append(end_time - start_time)
    return sum(times) / len(times)

# Generating 100 random lists of tasks
task_lists = [generate_tasks() for _ in range(100)]

# Measuring the performance
average_time_merge_sort = measure_performance(task_lists, PriorityQueueMergeSort)
average_time_sorted_insert = measure_performance(task_lists, PriorityQueueSortedInsert)

print(f"Average time for MergeSort-based PQ: {average_time_merge_sort}")
print(f"Average time for SortedInsert-based PQ: {average_time_sorted_insert}")

"""
5) SortedInsert is faster than MergeSort because of the time complexities between the two sorts.
MergeSort has a time complexity of O(nlogn) for sorting an array of n elements. When applied
to each enqueue operation, this complexity can add up, especially as the size of the queue grows.
The time complexity for inserting an element into a sorted array is O(n) in the worst case
(if every insertion happens at the very end). However, the average case can be much more
efficient if elements are often inserted nearer to their correct position.
"""

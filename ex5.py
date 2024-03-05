
class ArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = -1
        self.tail = -1

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return (self.tail + 1) % self.capacity == self.head

    def enqueue(self, item):
        if self.is_full():
            print("Enqueue None")
            return
        elif self.is_empty():
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = item
        print("enqueue", item)

    def dequeue(self):
        if self.is_empty():
            print("Dequeue None")
            return None
        item = self.queue[self.head]
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.capacity
        
        print("dequeue", item)
        return item

    def peek(self):
        if self.is_empty():
            print("Peek None")
            return None
        print("peek", self.queue[self.head])

        return self.queue[self.head]

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularQueue:
    def __init__(self, capacity):
        self.tail = None  
        self.size = 0     
        self.capacity = capacity

    def enqueue(self, value):
        new_node = Node(value)
        if(not self.is_full()):
            if self.tail is None:
                new_node.next = new_node
            else:
                new_node.next = self.tail.next
                self.tail.next = new_node
        else:
            print("enqueue None")
            return None
        self.tail = new_node  
        self.size += 1
        print("enqueue", value)


    def dequeue(self):
        if self.is_empty():
            print("Dequeue None")
            return None
        head = self.tail.next
        if self.tail == head:
            self.tail = None
        else:
            self.tail.next = head.next
        self.size -= 1
        print("dequeue", head.value)
        return head.value

    def peek(self):
        if self.is_empty():
            print ("Peek None")
            return None
        
        print("peek", self.tail.next.value)
        return self.tail.next.value

    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        if(self.size == self.capacity):
            return True
        return False

    def __len__(self):
        return self.size
    
array = ArrayQueue(5)
circular = CircularQueue(5)

array.enqueue(1)
print("Array queue after enqueue into empty queue expected value: 1. Actual Value:", array.peek())
circular.enqueue(1)
print("Linked List queue after enqueue into empty queue expected value: 1. Actual Value:", circular.peek(), "\n")


array.dequeue()
print("Array queue after dequeue expected value: Peek None. Actual Value:", array.peek())
circular.dequeue()
print("Linked List queue after dequeue expected value: Peek None. Actual Value:", circular.peek(), "\n")

array.enqueue(1)
array.enqueue(2)
array.enqueue(3)
print("Array queue after enqueue then dequeue expected value: 1. Actual Value:", array.dequeue())

circular.enqueue(1)
circular.enqueue(2)
circular.enqueue(3)
print("Linked List queue after enqueue then dequeue expected value: 1. Actual Value:", circular.dequeue(), "\n")

print("Array queue after another dequeue expected value: 2. Actual Value:", array.dequeue())
print("Linked List queue another dequeue expected value: 2. Actual Value:", circular.dequeue(), "\n")

print("Array queue peek value: 3. Actual Value:", array.peek())
print("Linked List peek value: 3. Actual Value:", circular.peek(), "\n")

array.enqueue(2)
array.enqueue(3)
array.enqueue(4)
array.enqueue(5)
print("Pushing into full array queue. Expected: enqueue None.")
array.enqueue(6)

circular.enqueue(2)
circular.enqueue(3)
circular.enqueue(4)
circular.enqueue(5)
print("Pushing into full circular queue. Expected: enqueue None.")
circular.enqueue(6)
print()

print("dequeueing array. Expected 3,2,3,4,5, none dequeue")
array.dequeue()
array.dequeue()
array.dequeue()
array.dequeue()
array.dequeue()
array.dequeue()

print("dequeueing circular. Expected 3,2,3,4,5, none dequeue")
circular.dequeue()
circular.dequeue()
circular.dequeue()
circular.dequeue()
circular.dequeue()
circular.dequeue()
print()

print("Multiple enqueues and dequeues and peek with array. Expected: Enqueue 5,4,3. Dequeue 5,4. Peek 3")
array.enqueue(5)
array.enqueue(4)
array.enqueue(3)
array.dequeue()
array.dequeue()
array.peek()

print("Multiple enqueues and dequeues and peek with Circular. Expected: Enqueue 5,4,3. Dequeue 5,4. Peek 3")
circular.enqueue(5)
circular.enqueue(4)
circular.enqueue(3)
circular.dequeue()
circular.dequeue()
circular.peek()
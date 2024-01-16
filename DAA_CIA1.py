1. STACK USING ARRAY
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop from an empty stack.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty. Cannot peek an empty stack.")

    def size(self):
        return len(self.items)
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack size:", stack.size())
print("Top of the stack:", stack.peek())

popped_item = stack.pop()
print("Popped item:", popped_item)

print("Stack size after pop:", stack.size())

2. STACK USING LINKED LIST
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Cannot peek.")
            return None
        return self.top.data

    def display(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack after pushes:")
stack.display()

print("Peek:", stack.peek())

popped = stack.pop()
print("Popped element:", popped)

print("Stack after pop:")
stack.display()

3.QUEUE USING ARRAY
class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        print(f"Enqueued {item} to the queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        print(f"Dequeued {item} from the queue")
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue elements:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print()
queue = Queue(5)

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()

queue.dequeue()
queue.display()

queue.enqueue(4)
queue.display()
print("Front element:", queue.peek())

4. QUEUE USING LINKED LIST
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def peek(self):
        if self.is_empty():
            return None
        return self.front.data

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue:")
queue.display()

print("Peek:", queue.peek())

print("Dequeue:", queue.dequeue())
print("Dequeue:", queue.dequeue())

print("Queue after dequeue:")
queue.display()

5.Priority queue

import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty priority queue")
        _, item = heapq.heappop(self.heap)
        return item

    def is_empty(self):
        return len(self.heap) == 0
priority_queue = PriorityQueue()

priority_queue.push("Task 1", 3)
priority_queue.push("Task 2", 1)
priority_queue.push("Task 3", 2)

while not priority_queue.is_empty():
    task = priority_queue.pop()
    print(f"Processing: {task}")

6.CIRCULAR QUEUE

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        elif self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = item
        print(f"Enqueued {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None

        item = self.queue[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        print(f"Dequeued {item}")
        return item

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        current = self.front
        while True:
            print(self.queue[current], end=" ")
            if current == self.rear:
                break
            current = (current + 1) % self.capacity
        print()
capacity = 5
cq = CircularQueue(capacity)

cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)

cq.display()

cq.dequeue()
cq.dequeue()

cq.display()

cq.enqueue(6)
cq.enqueue(7)

cq.display()


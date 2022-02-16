import sys


class Queue:
    """Queue data structure implementation"""
    
    def __init__(self, size: int) -> None:
        """Initialize the Queue with given size"""
        self.elements = [None] * (size + 1)
        self.head = 0
        self.tail = 0
    
    def is_empty(self) -> bool:
        """check if queue is empty"""
        return self.head == self.tail
    
    def is_full(self) -> bool:
        """check if queue is full, i.e. head = (tail + 1) mod n"""
        if (self.head == self.tail + 1) \
            or (self.tail ==len(self.elements) - 1 and self.head == 0):
            return True
        return False
    
    def enqueue(self, value:int) -> None:
        """insert an element with given value to the queue"""
        if self.is_full():
            raise Exception("queue overflow")
        self.elements[self.tail] = value
        self.tail += 1
        if self.tail == len(self.elements):
            self.tail = 0
    
    def dequeue(self):
        """get an element from the stack"""
        if self.is_empty():
            raise Exception("queue underflow")
        else:
            ret_val = self.elements[self.head]
            if self.head == len(self.elements) - 1:
                self.head = 0
            else:
                self.head += 1
            return ret_val
    
    def __str__(self):
        if self.is_empty():
            return "No element in the queue"
        else:
            start_idx = self.head
            end_idx = self.tail
            if end_idx < start_idx:
                end_idx += len(self.elements)

            return ", ".join([
                f"queue[{i%(len(self.elements))}] = {self.elements[i % len(self.elements)]}" for i in range(start_idx, end_idx)])


# TODO: Add unittest

if __name__ == "__main__":
    """Run the tests when the module is executed as main"""
    QUEUE_SIZE = 5
    q = Queue(QUEUE_SIZE)
    
    print(q)

    if q.is_empty():
        print("Queue is empty")
    else:
        print("Problem with is_empty() method")
        sys.exit(1)
    
    q.enqueue(5)
    if q.is_empty():
        print("Queue is empty. Problem with enqueue() method")
        sys.exit(1)
    else:
        print(q)

    q.enqueue(10)
    a = q.dequeue()
    if a == 5:
        print("Queue enqueued correct value")
    else:
        print("Indexing problem with enqueue()-dequeue() methods")
        sys.exit(1)
    
    a = q.dequeue()
    if a == 10:
        print("Queue enqueued correct value")
    else:
        print("Indexing problem with enqueue()-dequeue() methods")
        sys.exit(1)
    
    try:
        a = q.dequeue()
    except:
        print("dequeue() method raised exception for empty queue")
    else:
        print("Exception problem with dequeue() on empty stack")
        sys.exit(1)
    
    for i in range(QUEUE_SIZE):
        q.enqueue(i)
    
    print("After filling queue:")
    print(q)

    try:
        q.enqueue(10)
    except:
        print("enqueue() method raised exception for full queue")
    else:
        print("Exception problem with enqueue() on full queue")
        sys.exit(1)



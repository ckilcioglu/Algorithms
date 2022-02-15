import sys

class Stack:
    """Stack data structure implementation"""
    
    def __init__(self, size: int) -> None:
        """Initialize the stack with given size"""
        self.elements = [None] * size
        self.top = -1
    
    def is_empty(self) -> None:
        """check if stack is empty"""
        return self.top == -1
    
    def push(self, value:int) -> None:
        """insert an element with given value to the stack"""
        if self.top == len(self.elements) - 1:
            raise Exception("stack overflow")
        self.top += 1
        self.elements[self.top] = value
    
    def pop(self):
        """get an element from the stack"""
        if self.is_empty():
            raise Exception("stack overflow")
        else:
            self.top -= 1
            return self.elements[self.top+1]
    
    def __str__(self):
        if self.is_empty():
            return "No element in the stack"
        else:
            return ", ".join([f"stack[{i}] = {self.elements[i]}" for i in range(self.top+1)])


# TODO: Add unittest

if __name__ == "__main__":
    """Run the tests when the module is executed as main"""
    STACK_SIZE = 5
    s = Stack(STACK_SIZE)
    
    print(s)

    if s.is_empty():
        print("Stack is empty")
    else:
        print("Problem with is_empty() method")
        sys.exit(1)
    
    s.push(5)
    if s.is_empty():
        print("Stack is empty. Problem with push() method")
        sys.exit(1)
    else:
        print(s)

    s.push(10)
    a = s.pop()
    if a == 10:
        print("Stack poped correct value")
    else:
        print("Indexing problem with push()-pop() methods")
        sys.exit(1)
    
    a = s.pop()
    if a == 5:
        print("Stack poped correct value")
    else:
        print("Indexing problem with push()-pop() methods")
        sys.exit(1)
    
    try:
        a = s.pop()
    except:
        print("pop() method raised exception for empty stack")
    else:
        print("Exception problem with pop() on empty stack")
        sys.exit(1)
    
    for i in range(STACK_SIZE):
        s.push(i)
    
    print("After filling stack:")
    print(s)

    try:
        s.push(10)
    except:
        print("push() method raised exception for full stack")
    else:
        print("Exception problem with push() on full stack")
        sys.exit(1)



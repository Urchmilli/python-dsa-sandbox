class LinkedQueue:
    """FIFO queue implementation using a singly Linked list for storage"""
    class _Node:
        """Lightweight nonpublic class for storing a singly linked node"""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Create an empty queue"""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of element in the queue"""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty"""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the queue. """
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._head._element

    def dequeue(self):
        """Remove and return the first element in the Queue

        Raise Exception if queue is empty"""
        if self.is_empty():
            raise Exception("Queue is empty")
        answer = self._head._element
        self._head = self._head._element
        self._size-= 1
        if self.is_empty():
            self._tail = None
        return answer
    def enqueue(self, e):
        """Add a new element to the end of the queue"""
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1



if __name__ == "__main__":
    s = LinkedQueue()
    s.enqueue("Uche")
    print(s.dequeue())



class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def enqueue(self, item):
        node = Node(item)
        if self.head == None and self.tail == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.tail
            self.tail.prev = node
            self.tail = node
        self.length += 1
    
    def dequeue(self):
        if self.head == None and self.tail == None:
            return None
        else:
            self.length -= 1
            if self.head == self.tail:
                item = self.head.item
                self.head = None
                self.tail = None
                return item
            else:
                item = self.head.item
                self.head.prev.next = None
                self.head = self.head.prev
                return item
    
    def to_list(self):
        current = self.head
        items = []
        while current != None:
            items.append(current.item)
            current = current.prev
        return items

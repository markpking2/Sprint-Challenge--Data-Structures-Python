from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            if not self.current:
                self.current = self.storage.head
        else:
            self.current.value = item
            self.current = self.current.next if self.current != self.storage.tail else self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        node = self.storage.head
        while node:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity

    def append(self, item):
        self.storage[self.current] = item
        self.current = self.current + 1 if self.current != self.capacity - 1 else 0

    def get(self):
        return [x for x in self.storage if x != None]

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None

    def inserted_at_beginning(self, value):
        if self.start is None:
            self.start = Node(value)
        else:
            temp = self.start
            while temp is not None:
                temp = temp.next
            temp = Node(value)


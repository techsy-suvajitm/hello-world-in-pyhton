class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None

    def inserted_at_end(self, value):
        if self.start is None:
            self.start = Node(value)
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(value)
            print("temp.next", temp.next)

    def inserted_at_beginning(self, value):
        if self.start is None:
            self.start = Node(value)
        else:
            temp = self.start
            self.start = Node(value)
            self.start.next = temp

    def inserted_at_any_position(self, value, position):
        idx = 1
        if self.start is None:
            self.start = Node(value)
            return
        temp = self.start
        while temp.next is not None:
            if idx == position:
                curr = Node(value)
                curr.next = prev.next
                prev.next = curr
                return

            prev = temp
            temp = temp.next
            idx += 1
        self.inserted_at_end(value)

    def swap_two_nodes(self, i, j):
        if i == j:
            return
        prev1 = None
        curr1 = self.start
        idx = 1
        while curr1.next is not None and idx < i:
            prev1 = curr1
            curr1 = curr1.next
            idx += 1
        prev2 = None
        curr2 = self.start
        idx = 1
        while curr2.next is not None and idx < j:
            prev2 = curr2
            curr2 = curr2.next
            idx += 1
        if prev1 is not None:
            prev1.next = curr2
        else:
            self.start = curr2
        if prev2 is not None:
            prev2.next = curr1
        else:
            self.start = curr1

        temp = curr1.next
        curr1.next = curr2.next
        curr2.next = temp
        return

    def display_linkedList(self):
        if self.start is None:
            print("Linked List is empty..")
            return
        else:
            temp = self.start
            while temp is not None:
                print(temp.data)
                temp = temp.next
            return


res = LinkedList()
res.display_linkedList()
res.inserted_at_end(4)
res.inserted_at_end(5)
res.inserted_at_end(6)
res.inserted_at_beginning(8)
res.display_linkedList()
res.inserted_at_any_position(11, 3)
res.display_linkedList()
print("---------------------------------------")
res.swap_two_nodes(3, 5)
res.display_linkedList()
# print(res.start)
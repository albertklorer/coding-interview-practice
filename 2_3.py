# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node. 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)

        else:
            node = self.head
            while node.next != None:
                node = node.next

            node.next = Node(data)

    def deleteMiddle(self, data):
        node = self.head
        previous = None
        count = 0

        while node != None:
            if count >= 1 and data == node.data:
                previous.next = node.next

            count = count + 1
            previous = node
            node = node.next

    def print(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next

linkedList = LinkedList()
linkedList.insert(3)
linkedList.insert(1)
linkedList.insert(2)
linkedList.insert(4)
linkedList.deleteMiddle(1)
linkedList.print()
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

    def removeDuplicates(self):
        node = self.head
        previous = None
        values = set()
    
        while node != None:
            if node.data in values:
                previous.next = node.next
            else:
                values.add(node.data)
                previous = node
            
            node = node.next

    def print(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next

linkedList = LinkedList()
linkedList.insert(1)
linkedList.insert(4)
linkedList.insert(0)
linkedList.insert(1)
linkedList.removeDuplicates()
linkedList.print()
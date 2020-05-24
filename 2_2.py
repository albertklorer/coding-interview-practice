# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list. 

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

    def kToLast(self, k):
        dic = {}
        node = self.head

        count = 0
        while node != None:
            dic[count] = node
            node = node.next
            count = count + 1

        return dic[count - 1 - k].data

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
print(linkedList.kToLast(2))
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        # check to make sure value does not already exist in list
        if self.search(value) == True:
            return

        # insert new node at head
        node = Node(value)
        node.next = self.head
        self.head = node

    def search(self, value):
        node = self.head
        while node != None:
            if node.value == value:
                return True
            node = node.next

        return False

    def print(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

class HashMap:
    def __init__(self):
        self.list = [LinkedList(), LinkedList(), LinkedList(), LinkedList()]

    def insert(self, value):
        # add up ASCII values of all characters to find index
        total = 0
        for char in value:
            total = total + ord(char)
        key = total % 4

        # call LinkedList insert operation on correct index
        self.list[key].insert(value)

    def search(self, value):
         # add up ASCII values of all characters to find index
        total = 0
        for char in value:
            total = total + ord(char)
        key = total % 4

        # call LinkedList search operation on correct index
        return self.list[key].search(value)

hashMap = HashMap()
hashMap.insert('good man !    d gg h aa s ')
hashMap.insert('of all the things')
hashMap.insert('GGsss! ##')
hashMap.insert('')

print(hashMap.search('aa'))
print(hashMap.search('of all the things'))




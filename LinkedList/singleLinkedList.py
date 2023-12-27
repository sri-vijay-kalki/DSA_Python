class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        newNode = Node(value)
        if(self.head is None):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode

        self.length += 1

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str( temp_node.value)
            if temp_node.next is not None:
                result += '-> '
            temp_node = temp_node.next
        return result
    
    def prepend(self, value):
        new_node = Node (value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node (value)
        if index<0 and index>=self.length:
            return False
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        if index ==0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for i in range(index-1):
                temp_node= temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True
    
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next



newLinkedList = LinkedList()
newLinkedList.append("a")
newLinkedList.prepend("b")
print(newLinkedList)
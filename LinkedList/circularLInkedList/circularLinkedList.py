class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
            newNode.next = self.head
        self.length += 1

    def prepend(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
        else:
            newNode.next = self.head
            self.tail.next = newNode
            self.head = newNode
        self.length += 1

    def get(self,index):
        if index < 0 or index > self.length:
            print ("index out of range")
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def __str__(self):
        result = ""
        tempNode = self.head
        while tempNode is not None:
            result += str(tempNode.value)
            tempNode = tempNode.next
            if(tempNode == self.head):
                break
            result +="->"
        return result
cll = CLinkedList()
cll.append(1)
cll.append(2)
cll.prepend(3)
print(cll.get(1).value)
print(cll)
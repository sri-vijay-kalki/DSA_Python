class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def listToNode(list):
    dummy = Node(0)
    ite = dummy
    for i in list:
        ite.next = Node(i)
        ite = ite.next 
    return dummy.next

def printNodeList(head):
    tempHead = head
    while tempHead:
        print(str(tempHead.value) + "->")
        tempHead = tempHead.next
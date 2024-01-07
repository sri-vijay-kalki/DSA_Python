def removeNthFromEnd( head, n):
    returnPointer = None
    returnHead = head
    i=0
    while(i<n and head !=None):
        head = head.next
        i+=1
    # if(i!=n):
    #     return returnHead
    # if(head == None):
    #     return returnHead.next
    returnPointer = returnHead
    prev = None
    while(head != None):
        head = head.next
        prev = returnPointer
        returnPointer = returnPointer.next
    prev.next = returnPointer.next
    return returnHead


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
        print(str(tempHead.value) + "->",end =" ")
        tempHead = tempHead.next

nums = [1,2,3,4,5]
n = 6
newHead =removeNthFromEnd(listToNode(nums), n)

printNodeList(newHead)

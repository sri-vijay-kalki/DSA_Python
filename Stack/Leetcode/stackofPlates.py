import ast
class DinnerPlates(object):

    def __init__(self, capacity):
        self.items = []
        self.maxCap = capacity
        
    def __str__(self):
        print(self.items)
    def push(self, val):
        iter = 0
        isAppended = False
        while iter != len(self.items):
            if(len(self.items[iter]) is not self.maxCap):
                self.items[iter].append(val)
                isAppended  = True
            iter +=1
        if isAppended == False:
            if(len(self.items) ==0 or len(self.items[-1])==self.maxCap):
                self.items.append([val])
            else:
                self.items[-1].append(val)
        print(self.items)
    def pop(self):
        while self.items and len(self.items[-1]) ==0:
            self.items.pop()
        print(self.items[-1][-1] if len(self.items)!= 0 else -1)
        return self.items[-1].pop() if len(self.items)!= 0 else -1
        

    def popAtStack(self, index):
        print(self.items[index][-1] if len(self.items)!= 0 else -1)
        return self.items[index].pop() if len(self.items)!= 0 else -1

D = DinnerPlates(2)
D.push(1)
D.push(2)
D.push(3)
D.push(4)
D.push(5)
D.popAtStack(0)
D.push(20)
D.push(21)
D.popAtStack(0)
D.popAtStack(2)
D.pop()
D.pop()
D.pop()
D.pop()
D.pop()

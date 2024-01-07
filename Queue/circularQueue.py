class Queue:
    def __init__(self, maxSize):
        self.items = maxSize*[None]
        self.start = -1
        self.top = -1
        self.maxSize = maxSize

    def __str__(self):
        values =[str(x) for x in self.items]
        return "".join(values)
    def isFull(self):
        if (self.top+1 == self.start) or (self.start ==0 and self.top == self.maxSize):
            return True
        else:
            return False
        
    def isEmpty(self):
        if(self.top ==-1):
            return True
        return False
    
    def enqueue(self,value):
        if self.isFull():
            return "maxSize reached"
        else:
            if(self.top+1 == self.maxSize):
                self.top = 0
            else:
                self.top += 1
                if(self.start ==-1):
                    self.start = 0
            self.items[self.top] = value

    def dequeue(self):
        if self.isEmpty():
            return " No elements"
        val = self.items[self.start]
                
        if(self.start == self.top):
            self.start = self.top = -1
        elif(self.start+1 == self.maxSize):
            self.start  = 0
        else:
            self.start += 1

        return val
    
    def peek(self):
        if self.isEmpty():
            return "no Element present"
        
        else:
            return self.items[self.start]
        
    def delete(self):
        self.items = self.maxSize*[None]
        self.start = self.top = -1


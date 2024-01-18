import math
def evalRPN( tokens):
    numStack = []
    operators = {"+","-","*","/"}
    for i in tokens:
        if i in operators:
            op2 = numStack.pop()
            op1 = numStack.pop()
            if i =="+":
                numStack.append(op1 + op2)
            if i =="-":
                numStack.append(op1 - op2)
            if i =="*":
                numStack.append(op1 * op2)
            if i =="/":
                numStack.append(int(op1 / op2))
        else:
            numStack.append(int(i))
    return numStack.pop()
numArray =["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(numArray))
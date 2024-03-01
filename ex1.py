import sys

class MyListStack:
    def __init__(self):
        self._head = None
    def push(self, value):
        node = ListNode(value)
        node.setNext(self._head)
        self._head = node
    def pop(self):
        if self._head is None:
            return None
        else:
            retval = self._head.getData()
            self._head = self._head.getNext()
            return retval
    def peek(self):
        if self._head is None:
            return None
        else:
            return self._head.getData()
        
class ListNode:
    def __init__(self, value):
        self._value = value
        self._next = None

    def getData(self):
        return self._value

    def setData(self, value):
        self._value = value

    def getNext(self):
        return self._next

    def setNext(self, next):
        self._next = next

    def toString(self):
        return str(self._value)
    
operations = sys.argv

opStack = MyListStack()
numStack = MyListStack()
resultStack = MyListStack()
result = 0
numsLen = 0

for i in sys.argv[1]:
    if i == ')':
        op = opStack.pop()
        if(numsLen > 0):
            result = int(numStack.pop())
            numsLen -= 1
        else:
            result = resultStack.pop()

        while op != '(':
            num1 = int(numStack.pop())
            numsLen -= 1

            if op == "+":
                result += num1
            elif op == "-":
                result =- num1
            elif op == "*":
                result *= num1
            elif op == "/":
                result /= num1 
        
            op = opStack.pop()
        
        if numsLen == 0:
            resultStack.push(result)
        numStack.push(result)
        continue

    if(i.isdigit()):
        numStack.push(str(i))
        numsLen += 1
    elif (not i.isspace()):
        opStack.push(str(i))

if numsLen == 1:
    result = numStack.pop()

print("The result is:",result)
class Node(object):
    def __init__(self, data= None,next=None):
        self.data = data
        self.next = next
        
        
def findLengthRec(head, count):
    if head is None: return count
    return findLengthRec(head.next, count+1)

class LinkedList(object):
    def findLength(self, head):
        count = 0
        return findLengthRec(head, count)
    
    
# Sample run
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

sol = LinkedList()
result = sol.findLength(head)
print(result)
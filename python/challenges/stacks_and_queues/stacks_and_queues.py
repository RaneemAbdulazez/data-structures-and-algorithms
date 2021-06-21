class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
        
class Node: 
  def __init__(self, value=None):
    self.value = value
    self.next = None
    
class Stack :
  def __init__(self):
    self.top = None
    
  def push(self, value):
    node = Node(value)
    if self.top is None:
     self.top = node
    else:
      node.next = self.top
  
      self.top =node
  def pop(self):
    if not self.top:
      return "stack is empty"
    else:
      temp = self.top
      self.top = self.top.next
      temp.next = None
      return temp.value
  def peek(self):
    if self.top is None:
      return "stack is empty"
    else:
      return self.top.value
  def __str__(self):
    current = self.top
    while current:
      print(current.value)
      current = current.next
    return "done"
stack = Stack()
stack.push('one')
stack.push("two")
stack.push("three")
print(stack.pop())
print("-"*10)
print(stack)

def test_empty_queue_peek():
    queue = PseudoQueue()
    with  pytest.raises(EmptyStackException):
        queue.peek()
class EmptyStackException(Exception):
  pass


queue = Queue()
queue.enqueue('Raneem')
queue.enqueue('Raneem')
queue.dequeue()
queue.dequeue()
print(queue)
print(queue.peek())
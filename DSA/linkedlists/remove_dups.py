class LinkedList:
  def _init_(self,value):
    self.value = value
    self.next = None
#1->2->3->3->4->5->6->6->7 --> 1->2->3->4->5->6->7
#currentNode
#NextDistinctNode
#o(n)time | o(1)space 
def reomveDupsInLinkedList(linkedList):
  currentNode = linkedList
  while currentNode is not None:
    nextDistinctNode = currentNode.Next
    while nextDistinctNode is not None and currentNode.value == nextDistinctNode.value:
      nextDistinctNode = nextDistinctNode.next
      currentNode.next = nextDistinctNode
    return LinkedList
  

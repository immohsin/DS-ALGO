#  Reverse linked List
from linkedlist import SinglyLinkedList

def createList():
	ll = SinglyLinkedList()
	for i in range(1,11):
		ll.addFront(i)
	return ll

def printl(res):
	while(res != None):
		print(res.data, end= ' ')
		res = res.next

def recursiveApproach(head):
	if(head == None):
		return None
	elif(head.next == None):
		return head
	curr = head.next
	head.next = None
	newList = recursiveApproach(curr)
	curr.next = head
	return newList

def iterativeApproach(head):
	curr, prev = None, None
	while(head != None):
		curr  = head.next
		head.next = prev
		prev = head
		head = curr
	return prev



if __name__ == '__main__':
	ll = createList()
	head = ll.head
	res = recursiveApproach(head)
	printl(res)
	head1 = ll.head
	res1 = iterativeApproach(head1)
	printl(res1)
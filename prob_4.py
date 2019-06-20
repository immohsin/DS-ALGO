# Insert a node in sorted linkedlist


from linkedlist import SinglyLinkedList, Node

def createList():
	ll = SinglyLinkedList()
	for i in range(10, 0,-2):
		ll.addFront(i)
	return ll 

def addToSortedList(ll, data):
	newNode = Node(data)
	prev, curr = None, ll.head
	while(curr != None and curr.data < data):
		prev = curr
		curr = curr.next
	if prev:
		prev.next = newNode
	else:
		ll.head = newNode
	newNode.next = curr
	ll.print()




if __name__ == '__main__':
	ll = createList()
	addToSortedList(ll, 1)
	addToSortedList(ll, 1)
	addToSortedList(ll, 3)
	addToSortedList(ll, 3)
	addToSortedList(ll, 5)
	addToSortedList(ll, 7)
	addToSortedList(ll, 9)
	addToSortedList(ll, 10)


from linkedlist import SinglyLinkedList
import copy

# Delete nth node from end of the linked list
def bruteForceDeleteNode():
	ll = SinglyLinkedList()
	for i in range(10, 0, -1):
		ll.addFront(i)
	ll.print()
	try:
		while(1):
			p = int(input())
			c,pos = 0, 1
			temp, curr, prev = ll.head, ll.head, ll.head

			while temp != None:
				c+=1
				temp = temp.next

			if(p > c):
				print("No node at position given to delete")
			else:
				positionOfDeleteNode = c - p + 1
				if(positionOfDeleteNode == 1):
					ll.head =curr.next
				else:
					while curr != None and pos < positionOfDeleteNode:
						pos+=1
						prev = curr
						curr = curr.next
					prev.next = curr.next
				del curr
			ll.print()
	except KeyboardInterrupt:
		pass


# Find nth node from end of the linked list
def bruteForceFindNode():
	ll = SinglyLinkedList()
	for i in range(10, 0, -1):
		ll.addFront(i)
	ll.print()
	try:
		while(1):
			p = int(input())
			c = 0
			temp, curr = ll.head, ll.head

			while temp != None:
				c+=1
				temp = temp.next

			if(p > c):
				print("No node at position given position")
			else:
				for i in range(1, c - p + 1):
					curr = curr.next
				print("Node data at pos {} in reverse order is {}".format(p, curr.data))
	except KeyboardInterrupt:
		pass

# Find nth node from end of the linked list efficiently using dictionary
def hashTableFindNode():
	ll = SinglyLinkedList()
	for i in range(10, 0, -1):
		ll.addFront(i)
	ll.print()
	d = {}
	try:
		while(1):
			p = int(input())
			c = 0
			temp, curr = ll.head, ll.head

			while temp != None:
				c+=1
				d[c] = temp.data
				temp = temp.next
			print("Node data at pos {} in reverse order is {}".format(p, d[c - p + 1]))
	except KeyboardInterrupt:
		pass


# Find nth node from end of the linked list efficiently using 2 Pointers
def efficientFindNode():
	ll = SinglyLinkedList()
	for i in range(10, 0, -1):
		ll.addFront(i)
	ll.print()
	try:
		while(1):
			p = int(input())
			c = 0
			main = ll.head
			search = ll.head
			while main != None and c < p:
				c+=1
				main = main.next

			while main != None:
				search = search.next
				main = main.next

			print("Node data at pos {} in reverse order is {}".format(p, search.data))				
	except KeyboardInterrupt:
		pass

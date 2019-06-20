#  Find if Linked List is either null-terminated or ends in cycle

from linkedlist import SinglyLinkedList

def createList():
	ll = SinglyLinkedList()
	for i in range(1,11):
		ll.addFront(i)
	return ll 

def create_cyclic_list(single_node=False):
	cylic_ll = createList()
	temp = cylic_ll.head
	if(single_node):
		temp.next = temp
	else:
		while temp.next:
			print(temp.data)
			temp = temp.next
	return temp

# This approach will not work even when cycle is in any other node beside head
def bruteForce(ll):
	head_pos, temp = ll.head, ll.head
	if(temp):
		temp = temp.next
	while temp:
		if temp == head_pos:
			return "Linked List has cycle"
		temp = temp.next 
	if temp == None:
		return "Linked List has no cyle"

# This approach works even when cycle is in any other node beside head
def hashtableApproach(ll):
	ht = {}
	temp = ll.head
	while temp:
		if ht.get(temp) == "PRESENT":
			return "Linked List has cycle"
		ht[temp] = "PRESENT"
		temp = temp.next
	return "Linked List has no cyle"

# This approach is called floyd's cycle finding algorithm and it works even when cycle is in any other node beside head
def effcientApproach(ll):
	slow, fast = ll.head, ll.head
	while(fast and fast.next):
		fast = fast.next.next
		slow = slow.next
		if fast == slow:
			return "Linked List has cycle"
	return "Linked List has no cyle"

if __name__ == '__main__':
	ll = createList()
	print("Efficient approach, ", effcientApproach(ll))
	# Create a loop for testing
	ll.head.next.next.next.next.next.next = ll.head.next.next
	print("Efficient approach, ", effcientApproach(ll))

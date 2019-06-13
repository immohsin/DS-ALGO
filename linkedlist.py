# Base linnked list class that will be used for solving problems

class Node: 
    def __init__(self, data): 
        self.next = None
        self.data = data

class SinglyLinkedList:
	def __init__(self, head=None):
		self.head = head

	# Add Node at the beginning 
	def addFront(self, data):
		newNode = Node(data)
		if self.head is None:
			self.head = newNode
		else:
			newNode.next = self.head
			self.head = newNode

	# Delete Node at the beginning 
	def deleteFront(self):
		if self.head is not None:
			delNode = self.head
			self.head = delNode.next
			del delNode

	def print(self):
		temp = self.head
		if temp == None:
			print("List is empty")
		while(temp != None):
			print(temp.data, end= " ")
			temp = temp.next
		print()

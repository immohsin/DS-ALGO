# Implement stack using Linked List

from linkedlist import SinglyLinkedList

ll = SinglyLinkedList()

# Assingment to have Stack push & pop operation to reflect Naming convention
push = ll.addFront
pop = ll.deleteFront

# stack operation
print("push 10: ", end="")
push(10)
ll.print()
print("push 9: ", end="")
push(9)
ll.print()
print("push 20: ", end="")
push(20)
ll.print()
print("Linked list is: ", end="")
ll.print()
print("pop 20: ", end= "")
pop()
ll.print()
print("pop 9: ", end= "")
pop()
ll.print()
print("pop 10: ", end= "")
pop()
ll.print()
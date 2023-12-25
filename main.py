class Node:
    """
    
    Node class represent the element of the linked list
    """
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def empty(self):
        return self.head is None

    def append(self, node):
        """

        append the node at the end of the linked list
        node: type Node: instance of Node class
        """
        if self.empty():  # Edge case : when the append method is called to append the head node
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
            
    def appendleft(self, node):
        """
        
        append the node at the start of the linked list
        node:type Node: instance of Node class
        """
        node.next = self.head
        self.head = node
        

    def print_linked_list(self):
        if self.empty():  # Edge case : if the LinkedList is empty we cannot proceed
            print('Underflow occurred! LinkedList is empty.')

        current_node = self.head

        while True:  # we guarantee that infinite loop gonna stop when we reach the last element of our LinkedList
            print(current_node.value, end=', ')
            current_node = current_node.next
            if current_node.next is None: # if we reach the last element we would print it and then break the infinite loop
                print(current_node.value)
                break
            
    def __len__(self):
        current_node = self.head
        length = 0
        while True:
            if current_node is None:
                return length
            length += 1
            current_node = current_node.next
        return length


if __name__ == '__main__':
    
    n1 = Node('ayoub')
    n2 = Node('sami')
    n3 = Node('hamadi')
    n4 = Node('fedi')
    n5 = Node('chedi')
    linkedlist1 = LinkedList()
    linkedlist1.append(n1)
    linkedlist1.append(n2)
    linkedlist1.append(n3)
    linkedlist1.append(n4)
    linkedlist1.appendleft(n5)
    linkedlist1.print_linked_list()
    print(len(linkedlist1))

    linkedlist2 = LinkedList()
    for i in range(10):
        node = Node(i)
        linkedlist2.append(node)

    linkedlist2.print_linked_list()
    print(len(linkedlist2))
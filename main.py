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
    
    def __len__(self):
        current_node = self.head
        length = 0
        while True:
            if current_node is None:
                return length
            length += 1
            current_node = current_node.next
        return length

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
            
    def append_left(self, node):
        """
        
        append the node at the start of the linked list
        node:type Node: instance of Node class
        """
        node.next = self.head
        self.head = node
    
    def append_at(self, node, index):
        """

        Args:
            node (Node): instance of the Node class implemented above
            idx (int): represents the index where the node should be inserted and it shouldn't be out of range of the linked list instance
        Note:
            LinkedList is 0-BASED indexed
        """
        if not (0 <= index < len(self)):
            raise IndexError('Linked list index out of range')
        elif index == 0:  # if we want to make the node as a head node we should simply call the append_left() method implemented above
            self.append_left(node)
        elif index == len(self) - 1:
            self.append(node)  # if we want to append at the last index of the linked list then we should simply call the append() method implemented above
        else:
            current_node = self.head
            current_index = 0
            while True:
                if current_index == index:
                    previous_node.next = node
                    node.next = current_node
                    break
                previous_node = current_node
                current_node = current_node.next
                current_index += 1

    def print_linked_list(self):
        if self.empty():  # Edge case : if the LinkedList is empty we cannot proceed
            print('Underflow occurred! LinkedList is empty.')

        current_node = self.head

        while True:  # we guarantee that infinite loop gonna stop when we reach the last element of our LinkedList
            if current_node.next is None: # if we reach the last element we would print it and then break the infinite loop
                print(current_node.value)
                break
            print(current_node.value, end=', ')
            current_node = current_node.next


if __name__ == '__main__':
    
    node1 = Node('ayoub')
    node2 = Node('sami')
    node3 = Node('hamadi')
    node4 = Node('fedi')
    node5 = Node('chedi')
    linked_list1 = LinkedList()
    linked_list1.append(node1)
    linked_list1.append(node2)
    linked_list1.append(node3)
    linked_list1.append(node4)
    linked_list1.append_left(node5)
    linked_list1.append_at(node4, len(linked_list1) - 1)
    linked_list1.print_linked_list()  # lists all the elements of the linked_list1
    print(len(linked_list1))  # prints the length of the linked_list2 using the dunder method __len__ defined in the class

    linked_list2 = LinkedList()
    for i in range(10):
        node = Node(i)
        linked_list2.append(node)

    linked_list2.print_linked_list()  # lists all the elements of the linked_list2
    print(len(linked_list2))  # prints the length of the linked_list2 using the dunder method __len__ defined in the class
class Node:
    '''
    
        Node class represent the element of the linked list
    '''
    def __init__(self, value=None):
        '''
        
        Role:
            Constructor: Initialize the instance with the value by value and the next by None
        '''
        self.value = value
        self.next = None


class LinkedList:
    '''
    
    LinkedList class represents the data structure that gonna store nodes
    Note:
        You cannot have the same node appended twice to the LinkedList
        but you can instead append different nodes that have the same value
        the reason is that each node have an address in memory and each node
        in our LinkedList should point to its next node by its address and then 
        if we have the same node appended twice we gonna have an infinite loop 
        when we iterate over the LinkedList
    '''
        
    def __init__(self):
        
        '''
        
        Role:
            Constructor: initialize the instance with the head by None and length by 0
        '''
        self.head = None
        self.length = 0
    
    def __len__(self):
        
        '''
        
        Role:
            print the length of the LinkedList
        '''
        return self.length

    def empty(self):
        '''
        
        Role:
            Check whether the LinkedList is empty or not
        '''
        return self.head is None

    def append(self, node):
        '''
            Role:
                append the node at the end of the linked list
            Args:
                node (Node): instance of the Node class implemented above
        '''
        if self.empty():  # Edge case : when the append method is called to append the head node
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
            
        self.length += 1
         
    def append_left(self, node):
        '''
        
        Role
            append the node at the start of the linked list
        Args:
            node (Node): instance of the Node class implemented above
        '''
        node.next = self.head
        self.head = node
    
        self.length += 1
    
    def append_at(self, node, index):
        '''

        Role:
            append node at specific index
        Args:
            node (Node): instance of the Node class implemented above
            idx (int): represents the index where the node should be inserted 
                        and it shouldn't be out of range of the linked list instance
        Note:
            LinkedList is 0-BASED indexed
        '''
        if not (0 <= index <= len(self)):
            raise IndexError('Linked list index out of range')
        elif index == 0:  # if we want to make the node as a head node we should simply call the append_left() method implemented above
            self.append_left(node)
        elif index == len(self):
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

            self.length += 1 

    def print_linked_list(self):
        
        '''
        
        Role:
            lists all the LinkedList elements
        '''        
        if self.empty():  # Edge case : if the LinkedList is empty we cannot proceed
            print('Underflow occurred! LinkedList is empty.')

        current_node = self.head
        i = 0

        while True:  # we guarantee that infinite loop gonna stop when we reach the last element of our LinkedList
            i += 1
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
    node6 = Node('fedi')
    linked_list1 = LinkedList()
    linked_list1.append(node1)
    linked_list1.append(node2)
    linked_list1.append(node3)
    linked_list1.append(node4)
    linked_list1.append_left(node5)
    linked_list1.append_at(node6, 3)
    linked_list1.print_linked_list()  # lists all the elements of the linked_list1
    print(len(linked_list1))  # prints the length of the linked_list2 using the dunder method __len__ defined in the class

    linked_list2 = LinkedList()
    for i in range(10):
        node = Node(i)
        linked_list2.append(node)

    linked_list2.print_linked_list()  # lists all the elements of the linked_list2
    print(len(linked_list2))  # prints the length of the linked_list2 using the dunder method __len__ defined in the class
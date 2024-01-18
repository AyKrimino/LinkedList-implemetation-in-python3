from typing import Any, Optional, TypeVar


NodeObject = TypeVar('NodeObject')


class Node:
    '''
    
        Node class represent the element of the linked list
    '''
    def __init__(self, value: Optional[Any]=None):
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
        self.length: int = 0
    
    def __len__(self) -> int:
        
        '''
        
        Role:
            print the length of the LinkedList
        '''
        return self.length

    def empty(self) -> bool:
        '''
        
        Role:
            Check whether the LinkedList is empty or not
        '''
        return self.head is None

    def append(self, node: NodeObject) -> None:
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
         
    def append_left(self, node: NodeObject) -> None:
        '''
        
        Role
            append the node at the start of the linked list
        Args:
            node (Node): instance of the Node class implemented above
        '''
        node.next = self.head
        self.head = node
    
        self.length += 1
    
    def append_at(self, node: NodeObject, index: int) -> None:
        '''

        Role:
            append node at specific index
        Args:
            node (Node): instance of the Node class implemented above
            index (int): represents the index where the node should be inserted 
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
            
    def pop_left(self) -> Any:
        '''
        
        Role:
            Removes the head node depending on which case it gonna do some logic
            if the LinkedList is empty it returns None
            if the LinkedList have one node it removes this node and returns its value
            otherwise if the LinkedList have more than one node it removes the head node 
            and it makes next node as the head node and then it return the value of the 
            head node removed 
        '''
        if self.empty():
            return None
        
        val = self.head.value
        if len(self) == 1:
            self.head = None
        else:
            self.head = self.head.next
        self.length -= 1
        return val 
            
    def pop(self) -> Any:
        '''
        
        Role:
            Removes the last node of the LinkedList if it exists(LinkedList not empty) 
            and returns its value
            if the LinkedList is empty it returns None 
        '''
        if self.empty():
            return None
        
        if len(self) == 1:
            return self.pop_left()
        else:
            self.length -= 1
            current_node = self.head
            while True:
                if current_node.next is None:
                    previous_node.next = None
                    return current_node.value
                previous_node = current_node
                current_node = current_node.next   
                
    def pop_at(self, index: int) -> Any:
        '''
        
        Role:
            removes the node at a specific index from the LinkedList
        Args:
            index (int): represents the index where the node should be removed 
                        and it shouldn't be out of range of the linked list instance
        Note:
            LinkedList is 0-BASED indexed
        '''
        if not (0 <= index <= len(self) - 1):
            raise IndexError('Linked list index out of range')
        
        if index == 0:        
            return self.pop_left()
        elif index == len(self) - 1:
            return self.pop()
        else:
            current_index = 0
            current_node = self.head
            self.length -= 1
            while True:
                if current_index == index:
                    previous_node.next = current_node.next
                    return current_node.value
                current_index += 1
                previous_node = current_node
                current_node = current_node.next
                
    def find(self, value: Any) -> int:
        '''
        
        Role:
            Checks if the given value of a node exist in the LinkedList instance
            if so it returns the index of the first occurence of that value
            (remember values of nodes can be duplicate in the same LinkedList instance
            but duplicate nodes cannot be appended to the same LinkedList instance)
            else it returns -1 to help the user understand that node doesn't exist
        Args:
            value (any): represents the value of the desired node
        Note:
            LinkedList is 0-BASED indexed
        '''
        current_node = self.head
        current_index = 0
        while current_node is not None:
            if value == current_node.value:
                return current_index
            current_node = current_node.next
            current_index += 1
        return -1
                

    def print_linked_list(self) -> None:
        '''
        
        Role:
            lists all the LinkedList nodes and if the LinkedList is empty it shows that
        '''        
        if self.empty():  # Edge case : if the LinkedList is empty we cannot proceed
            print('Underflow occurred! LinkedList is empty.')
            return

        current_node = self.head

        while True:  # we guarantee that infinite loop gonna stop when we reach the last element of our LinkedList
            if current_node.next is None: # if we reach the last element we would print it and then break the infinite loop
                print(current_node.value)
                break
            print(current_node.value, end=', ')
            current_node = current_node.next


def main() -> None:
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
    linked_list1.pop_left()
    linked_list1.print_linked_list()  # lists all the elements of the linked_list1
    print(linked_list1.find('fedi'))
    print(linked_list1.find('fsdjjflks'))
    print(len(linked_list1))  # prints the length of the linked_list2 using the dunder method __len__ defined in the class

    linked_list2 = LinkedList()
    for i in range(10):
        node = Node(i)
        linked_list2.append(node)

    linked_list2.print_linked_list()  # lists all the elements of the linked_list2
    print(linked_list2.pop_at(3))
    linked_list2.print_linked_list()  # lists all the elements of the linked_list2


if __name__ == '__main__':
    main()
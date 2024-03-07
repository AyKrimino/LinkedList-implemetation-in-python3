# Python Linked List Implementation

This repository contains a Python implementation of a linked list data structure, including a Node class and a LinkedList class. The project demonstrates essential concepts in data structures and showcases proficiency in Python coding conventions.

## Features

- **Node Class:** Represents the elements of the linked list.
- **LinkedList Class:** Stores nodes and provides essential operations.
  - Append node at the end of the linked list.
  - Append node at the start of the linked list.
  - Append node at a specific index.
  - Remove the head node or a node at a specific index.
  - Find the index of a node with a specific value.
  - Print the elements of the linked list.

## Usage

1. **Instantiate a Linked List:**
    ```python
    linked_list = LinkedList()
    ```

2. **Create Nodes and Append to the List:**
    ```python
    node1 = Node('ayoub')
    node2 = Node('sami')
    linked_list.append(node1)
    linked_list.append(node2)
    ```

3. **Perform Operations:**
    ```python
    linked_list.print_linked_list()
    linked_list.pop_left()
    print(linked_list.find('sami'))
    ```

## Examples

Check the provided `main` function in the script for examples of creating and manipulating linked lists.

Feel free to explore the code for more details. Contributions are welcome!

## Author

Ayoub Krimi

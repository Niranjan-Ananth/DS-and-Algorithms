class Node:
    def __init__(self, element) -> None:
        self.data = element
        self.next = None

class CircularLinkedList:
    def __init__(self) -> None:
        self.__start = None
        self.__tail = None
    
    def insert_node_at_beginning(self, element):
        node = Node(element)
        if self.__start is None:
            node.next = node
            self.__tail = node
        else:
            node.next = self.__start
        self.__start = node
        self.__tail.next = self.__start

    def insert_node_at_end(self, element):
        node = Node(element)
        if self.__tail:
            self.__tail.next = node
        self.__tail = node
        node.next = self.__start

    def insert_node_at_index(self, element, index):
        node = Node(element)
        temp = self.__start
        for i in range(0, index-1):
            if temp.next:
                temp = temp.next
            else:
                raise RuntimeError("Invalid index")
        node.next = temp.next
        temp.next = node

    def delete_node_at_beginning(self):
        if self.__start is None:
            return   
        self.__start = self.__start.next
        self.__tail.next = self.__start

    def delete_node_at_end(self):
        if self.__tail is None:
            return
        temp = self.__start
        while temp.next != self.__tail:
            temp = temp.next
        self.__tail = temp
        temp.next = self.__start

    def delete_node_at_index(self, index):
        temp = self.__start
        for i in range(0, index-1):
            if temp.next:
                temp = temp.next
            else:
                raise RuntimeError("Invalid index")
        temp.next = temp.next.next

    def size(self):
        len = 0
        temp = self.__start
        if not temp:
            return len
        len = 1
        temp = temp.next
        while temp and temp != self.__start:
            len += 1
            temp = temp.next
        return len

    def display(self):
        temp = self.__start
        if not temp:
            return
        print(temp.data, end=' ')
        temp = temp.next
        while temp and temp != self.__start:
            print(temp.data, end=' ')
            temp = temp.next
        print()

if __name__ == '__main__':
    circular_linked_list = CircularLinkedList()
    circular_linked_list.insert_node_at_beginning(1)
    circular_linked_list.insert_node_at_beginning(2)
    circular_linked_list.insert_node_at_beginning(3)
    circular_linked_list.insert_node_at_end(4)
    circular_linked_list.insert_node_at_end(5)
    circular_linked_list.insert_node_at_end(6)
    circular_linked_list.insert_node_at_index(11, 3)
    circular_linked_list.insert_node_at_index(15, 6)
    circular_linked_list.insert_node_at_index(19, 3)
    circular_linked_list.display()
    print("Size of list is " + str(circular_linked_list.size()))
    circular_linked_list.delete_node_at_beginning()
    circular_linked_list.delete_node_at_end()
    circular_linked_list.delete_node_at_index(3)
    circular_linked_list.display()
    print("Size of list is " + str(circular_linked_list.size()))

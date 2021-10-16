class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.__start = None
    
    def insert_node_at_begining(self, element):
        node = Node(element)
        node.next = self.__start
        self.__start = node
    
    def insert_node_at_end(self, element):
        node = Node(element)
        temp = self.__start
        while temp.next:
            temp = temp.next
        temp.next = node

    def insert_node_at_index(self, element, index: int):
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
        if self.__start:
            self.__start = self.__start.next
    
    def delete_node_at_end(self):
        if self.__start:
            if self.__start.next is None:
                self.__start = None
            else:
                temp = self.__start
                while temp.next.next:
                    temp = temp.next
                temp.next = None
    
    def delete_node_at_index(self, index: int):
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
        while temp:
            len += 1
            temp = temp.next
        return len

    def display(self):
        temp = self.__start
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()


if __name__ == '__main__':
    try:
        linked_list = LinkedList()
        linked_list.insert_node_at_begining(1)
        linked_list.insert_node_at_begining(2)
        linked_list.insert_node_at_begining(3)
        linked_list.insert_node_at_begining(8)
        linked_list.insert_node_at_begining(6)
        linked_list.insert_node_at_end(11)
        linked_list.insert_node_at_end(15)
        linked_list.insert_node_at_end(17)
        linked_list.insert_node_at_index(21, 3)
        linked_list.insert_node_at_index(23, 7)
        linked_list.insert_node_at_index(25, 3)
        linked_list.display()
        print("Size of linked list is " + str(linked_list.size()))
        linked_list.delete_node_at_beginning()
        linked_list.delete_node_at_beginning()
        linked_list.delete_node_at_beginning()
        linked_list.delete_node_at_end()
        linked_list.delete_node_at_end()
        linked_list.delete_node_at_end()
        linked_list.delete_node_at_index(3)
        linked_list.delete_node_at_index(2)
        linked_list.display()
        print("Size of linked list is " + str(linked_list.size()))
    except:
        print("There was an exception while running the program")
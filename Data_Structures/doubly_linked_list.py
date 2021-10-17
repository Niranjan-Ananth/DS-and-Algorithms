class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.back = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.__start = None
        self.__tail = None
    
    def insert_node_at_begining(self, element):
        node = Node(element)
        node.next = self.__start
        if self.__start:
            self.__start.back = node
        else:
            self.__tail = node
        self.__start = node
    
    def insert_node_at_end(self, element):
        node = Node(element)
        temp = self.__start
        while temp.next:
            temp = temp.next                
        temp.next = node
        node.back = temp
        self.__tail = node

    def insert_node_at_index(self, element, index: int):
        node = Node(element)
        temp = self.__start
        for i in range(0, index-1):
            if temp.next:
                temp = temp.next
            else:
                raise RuntimeError("Invalid index")
        node.next = temp.next
        temp.next.back = node
        node.back = temp
        temp.next = node
    
    def delete_node_at_beginning(self):
        if self.__start:
            self.__start = self.__start.next
            self.__start.back = None
    
    def delete_node_at_end(self):
        if self.__start:
            if self.__start.next is None:
                self.__start = None
            else:
                temp = self.__start
                while temp.next.next:
                    temp = temp.next
                temp.next.back = None
                temp.next = None
                self.__tail = temp
    
    def delete_node_at_index(self, index: int):
        temp = self.__start
        for i in range(0, index-1):
            if temp.next:
                temp = temp.next
            else:
                raise RuntimeError("Invalid index")
        del_node = temp.next
        temp.next.next.back = temp        
        temp.next = temp.next.next
        del_node.next = None
        del_node.back = None

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

    def display_reverse(self):
        temp = self.__tail
        while temp:
            print(temp.data, end=' ')
            temp = temp.back
        print()
        
if __name__ == '__main__':
    try:
        double_linked_list = DoublyLinkedList()
        double_linked_list.insert_node_at_begining(1)
        double_linked_list.insert_node_at_begining(2)
        double_linked_list.insert_node_at_begining(3)
        double_linked_list.insert_node_at_begining(8)
        double_linked_list.insert_node_at_begining(6)
        double_linked_list.insert_node_at_end(11)
        double_linked_list.insert_node_at_end(15)
        double_linked_list.insert_node_at_end(17)
        double_linked_list.insert_node_at_index(21, 3)
        double_linked_list.insert_node_at_index(23, 7)
        double_linked_list.insert_node_at_index(25, 3)
        double_linked_list.display()
        double_linked_list.display_reverse()
        print("Size of linked list is " + str(double_linked_list.size()))
        double_linked_list.delete_node_at_beginning()
        double_linked_list.delete_node_at_beginning()
        double_linked_list.delete_node_at_beginning()
        double_linked_list.delete_node_at_end()
        double_linked_list.delete_node_at_end()
        double_linked_list.delete_node_at_end()
        double_linked_list.delete_node_at_index(3)
        double_linked_list.delete_node_at_index(2)
        double_linked_list.display()
        double_linked_list.display_reverse()
        print("Size of linked list is " + str(double_linked_list.size()))
    except Exception as e:
        print("There was an exception while running the program")
        print(e)
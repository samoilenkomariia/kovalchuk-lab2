class Node:
    def __init__(self, data: str):
        self.data = data
        self.next = None

# variant 20 % 4 = 0: single circular linked list

class circular_single_ll:
    def __init__(self):
        self.head = None

    def append(self, data: str) -> None:
        if not isinstance(data, str):
            raise TypeError("Data must be of type str")
        
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head

    def length(self) -> int:
        if self.head is None:
            return 0

        count = 1
        current = self.head.next # start from 2d node
        while current != self.head:
            current = current.next
            count+=1
        return count 

    def insert(self, data: str, index: int) -> None:
        if not isinstance(data, str):
            raise TypeError("Data must be of type str")

        if not isinstance(index, int):
            raise TypeError("Index must be an integer")

        if index > self.length() or index < 0:
            raise IndexError("Index out of boundaries")
        
        if self.head is None:
            self.append(data)
            return
        
        current = self.head
        new_node = Node(data)

        if index == 0:
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node
            return

        for _ in range(index-1):
            current = current.next
       
        new_node.next = current.next
        current.next = new_node
    
    def delete(self, index: int) -> str:
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")

        if index >= self.length() or index < 0:
            raise IndexError("Index out of boundaries")
        
        if self.head is None:
            return None

        if self.head.next == self.head:
            data = self.head.data
            self.head = None
            return data

        current = self.head

        if index == 0:
            data = self.head.data
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return data
        
        prev = None
        for _ in range(index):
            prev = current
            current = current.next
        
        prev.next = current.next
        data = current.data
        return data 
    
    def delete_all(self, data: str) -> None:
        if self.head is None:
            return
        
        while self.head and self.head.data == data:
            self.delete(0)
            if self.head is None:
                return

        current = self.head
        while current.next != self.head:
            if current.next.data == data:
                current.next = current.next.next
            else:
                current = current.next

    def get(self, index: int) -> str:
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")

        if index >= self.length() or index < 0:
            raise IndexError("Index out of boundaries")
        
        current = self.head

        for _ in range(index):
            current = current.next
        return current.data
    
    def clone(self) -> 'circular_single_ll':
        new_list = circular_single_ll()

        if self.head is not None:
            current = self.head
            for _ in range(self.length()):
                new_list.append(current.data)
                current = current.next
        return new_list

    def reverse(self) -> None:
        if self.head is None or self.head.next == self.head:
            return
        '''
        The approach: making the current node point to the previous one 
        in a loop until the last node is reached, 
        then making the last node point to the previous one, 
        making the initial head (the original first node) point to the last node, 
        and making the last node the new head of the list.
        
        example list: 1 2 3 4 5
        '''
        current = self.head # 1->2
        prev = None
        next_node = current.next # 2->3
        while next_node != self.head:
            current.next = prev # 1->None # 2->1 # 3->2 #4->3
            prev = current # 1->None # 2->1 # 3->2 #4->3
            current = next_node # 2->3 # 3->4 # 4->5 #5->1
            next_node = next_node.next # 3->4 #4->5 #5->1 #1->None
        
        current.next = prev # 5->4
        self.head.next = current # 1->5
        self.head = current # 5->4

    def print_list(self) -> None:
        if self.head is None:
            print("")
            return
        current = self.head
        print(current.data, end=" ")
        current = current.next
        while current != self.head:
            print(current.data, end=" ")
            current = current.next
        print()
        
            
    def find_first(self, data: str) -> int:
        if self.head is None:
            return -1
        current = self.head
        for i in range(self.length()):
            if current.data == data:
                return i
            current = current.next
        return -1
    
    def find_last(self, data: str) -> int:
        if self.head is None:
            return -1
        
        current = self.head
        res = -1
        for i in range(self.length()):
            if current.data == data:
                res = i
            current = current.next
        return res

    def clear(self) -> None:
        if self.head is None:
            return
        
        current = self.head
        while True:
            next_node = current.next
            current.next = None
            if next_node == self.head:
                break
            current = next_node
        
        self.head = None

    def extend(self, list: 'circular_single_ll') -> None:
        if list.head is None:
            return
        current = list.head
        for i in range(list.length()):
            self.append(current.data)
            current = current.next

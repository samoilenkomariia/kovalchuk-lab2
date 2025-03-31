class Node:

    def __init__(self, data: str):
        self.data = data
        self.next = None


# variant 20 % 4 = 0: single circular linked list


class circular_single_ll:

    def __init__(self):
        self.head = None
        self.list = []

    def append(self, data: str) -> None:
        if not isinstance(data, str):
            raise TypeError("Data must be of type str")

        new_node = Node(data)

        if not self.list:
            self.head = new_node
            new_node.next = 0
            self.list.append(new_node)
        else:
            last_index = len(self.list) - 1
            new_node.next = 0
            self.list[last_index].next = len(self.list)
            self.list.append(new_node)

    def length(self) -> int:
        return len(self.list)

    def insert(self, data: str, index: int) -> None:
        if not isinstance(data, str):
            raise TypeError("Data must be of type str")

        if not isinstance(index, int):
            raise TypeError("Index must be an integer")

        if index > len(self.list) or index < 0:
            raise IndexError("Index out of boundaries")

        if not self.list:
            self.append(data)
            return

        new_node = Node(data)

        new_node.next = index + 1
        for i in range(index, len(self.list) - 1):
            self.list[i].next += 1

        if index == len(self.list):
            self.list[len(self.list) - 1].next = len(self.list)
            new_node.next = 0

        self.list.insert(index, new_node)

        if index == 0:
            self.head = new_node

    def delete(self, index: int) -> str:
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")

        if index >= self.length() or index < 0:
            raise IndexError("Index out of boundaries")

        if len(self.list) == 1:
            data = self.head.data
            self.head = None
            self.list.clear()
            return data

        for i in range(index + 1, len(self.list) - 1):
            self.list[i].next -= 1

        if index == len(self.list) - 1:
            self.list[index - 1].next = 0
        data = self.list.pop(index)
        if index == 0:
            self.head = self.list[0]

        return data

    def delete_all(self, data: str) -> None:
        if len(self.list) == 0:
            return

        while self.head and self.head.data == data:
            self.delete(0)
            if self.head is None:
                return

        i = 0
        for _ in range(self.length()):
            if self.list[i].data == data:
                self.delete(i)
            else:
                i = self.list[i].next

    def get(self, index: int) -> str:
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")

        if index >= self.length() or index < 0:
            raise IndexError("Index out of boundaries")

        return self.list[index].data

    def clone(self) -> 'circular_single_ll':
        res = circular_single_ll()
        if not self.list:
            return res
        res.list = self.list.copy()
        res.head = res.list[0]
        return res

    def reverse(self) -> None:
        if self.length() <= 1:
            return

        self.list.reverse()
        i = 1
        for node in self.list:
            node.next = i
            i += 1
        self.list[self.length() - 1].next = 0
        self.head = self.list[0]

    def find_first(self, data: str) -> int:
        if self.head is None:
            return -1
        for i in range(self.length()):
            if self.list[i].data == data:
                return i
        return -1

    def find_last(self, data: str) -> int:
        if self.head is None:
            return -1

        res = -1
        for i in range(self.length()):
            if self.list[i].data == data:
                res = i
        return res

    def clear(self) -> None:
        if not self.list:
            return
        self.head = None
        self.list.clear()

    def extend(self, cll: 'circular_single_ll') -> None:
        if cll.head is None:
            return
        for i in range(cll.length()):
            self.append(cll.list[i].data)

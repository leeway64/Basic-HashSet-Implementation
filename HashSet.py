# 11/22/2020
class HashSet:
    def __init__(self, capacity):
        self.__data = []
        self.__hash_table_length = capacity / 0.75  # Load factor: 0.75
        # print(self.__hash_table_length)
        # print(capacity)
        self.__initialize_data(int(self.__hash_table_length))
        self.__size = 0

    def add(self, value):
        if not self.contains(value):
            i = self.__index_of(value)
            self.__data[i] = self.__HashNode(value, self.__data[i])
            self.__size += 1

    def remove(self, value):
        if self.contains(value):
            i = self.__index_of(value)
            if self.__data[i].value == value:
                self.__data[i] = self.__data[i].next
            else:
                current = self.__data[i]
                while current.next.value != value:
                    current = current.next
                current.next = current.next.next
            self.__size -= 1

    def contains(self, value):
        i = self.__index_of(value)
        current = self.__data[i]
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def size(self):
        return self.__size

    def __index_of(self, value):
        return int(abs(hash(value) % self.__hash_table_length))

    def __initialize_data(self, size):
        for i in range(size):
            self.__data.append(self.__HashNode())

    class __HashNode:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

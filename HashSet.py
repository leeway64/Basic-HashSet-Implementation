class HashSet:
    def __init__(self, capacity):
        self.__data = []
        self.__hash_table_length = capacity / 0.75
        self.__size = 0

    def add(self, value):
        if not self.contains(value):
            i = self.__index_of(value)
            self.data[i] = self.HashNode(value, self.data[i])
            self.__size += 1

    def contains(self, value):
        i = self.__index_of(value)
        current = self.__data[i]
        while current is not None:
            if current.data == value:
                return True
            current = current.next
        return False

    def __size(self):
        return self.__size

    def __index_of(self, value):
        return abs(hash(value) % self.__hash_table_length)

    class HashNode:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

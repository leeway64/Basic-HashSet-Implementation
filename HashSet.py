# 11/24/2020
class HashSet:
    def __init__(self, capacity):
        self.__data = []
        self.__hash_table_length = int(capacity / 0.75)  # Load factor: 0.75
        # print(self.__hash_table_length)
        # print(capacity)
        self.__initialize_data(self.__hash_table_length)
        self.__size = 0

    def add(self, *values):
        for value in values:
            if not self.contains(value):  # Does not allow any duplicates
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
        # print(int(abs(hash(value) % self.__hash_table_length)))
        return int(abs(hash(value) % self.__hash_table_length))  # Hash code is the same for ints

    def __initialize_data(self, table_length):
        for i in range(table_length):
            self.__data.append(self.__HashNode())

    def __str__(self):
        result = "{\n"
        for i in range(self.__hash_table_length):
            if self.__data[i].value is not None:
                current = self.__data[i]
                while current.value is not None:
                    result += str(i) + ': ' + str(current.value) + '\n'
                    current = current.next
        result += "}"
        return result

    class __HashNode:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

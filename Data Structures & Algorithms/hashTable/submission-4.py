class __Node__:
    key: int
    value: int

    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    storage: list[None | __Node__] = []
    size = 0

    def __init__(self, capacity: int):
        self.storage = [None] * capacity
        print("init with {capacity}".format(capacity=capacity))

    def insert(self, key: int, value: int) -> None:
        print("insert {key},{value}".format(key=key, value=value))
        index = self.__storageIndex(key)
        storedAtIndex = self.storage[index]
        if storedAtIndex != None and storedAtIndex.key != key:
            self.resize()
            self.insert(key, value)
            return


        newNode = __Node__(key, value)
        self.storage[index] = newNode
        
        if storedAtIndex == None or (storedAtIndex != None and storedAtIndex.key != key):
            self.size += 1
        
        if self.size >= len(self.storage) / 2:
            self.resize()

    def get(self, key: int) -> int:
        stored = self.storage[self.__storageIndex(key)]
        if stored == None or stored.key != key:
            return -1

        return stored.value

    def remove(self, key: int) -> bool:
        stored = self.storage[self.__storageIndex(key)]
        if stored == None or stored.key != key:
            return False

        self.storage[self.__storageIndex(key)] = None
        self.size -= 1
        return True

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return len(self.storage)

    def resize(self) -> None:
        print("resizing")
        newStorageLen = len(self.storage) * 2
        self.__sizeToCapacity(newStorageLen)

    def __sizeToCapacity(self, capacity: int):
        newStorage: list[None | __Node__] = [None] * capacity
        oldStorage = self.storage
        self.storage = newStorage
        for element in oldStorage:
            if element == None:
                continue
            newIndex = self.__findEmptyIndex(self.__storageIndex(element.key), newStorage, element.key) 
            if newIndex == None:
                print("couldn't find index...")
                self.storage = oldStorage
                self.__sizeToCapacity(capacity * 2 - 1)
            else: newStorage[newIndex] = element

    def __storageIndex(self, key):
        return key % len(self.storage)


    def __findEmptyIndex(self, start: int, store: list, key: int) -> int | None:
        for i in range(0,len(store)):
            index = (start + i) % len(store)
            if store[index] == None:
                return index
        return None

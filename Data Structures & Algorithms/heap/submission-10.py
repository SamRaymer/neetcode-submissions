class MinHeap:
    storage: list[int | None]

    def __init__(self):
        self.storage = [None]

    def push(self, val: int) -> None:
        self.storage.append(val)
        lastIndex = len(self.storage) - 1

        # print("appended {v} at {i}".format(v=val,i=lastIndex))
        currentIndex: int = lastIndex
        while currentIndex > 1:
            parentIndex = int(currentIndex / 2)
            parentValue = self.storage[parentIndex]
            currentValue = self.storage[currentIndex]
            if parentValue == None or currentValue == None:
                # print("ERROR: a value is 'None'")
                return
            if parentValue < currentValue:
                return
            else:
                self.storage[parentIndex] = currentValue
                self.storage[currentIndex] = parentValue
            currentIndex = int(currentIndex / 2) # truncates remainder (b^_^)b

    def pop(self) -> int:
        minValue = self.top()
        # print("top is "+ str(minValue))
        if len(self.storage) == 1:
            return minValue

        lastIndex = len(self.storage) - 1
        self.storage[1] = self.storage[lastIndex]
        self.storage.pop()
        # print("Start: " +self.__storageToStr())
        initialIndex = 1
        if (len(self.storage) > 2):
            self.__percolateDown(initialIndex)
        # print("Final:" + self.__storageToStr())
        return minValue

    def __storageToStr(self) -> str:
        return ",".join("None" if item == None else str(item) for item in self.storage)

    def __percolateDown(self, index):
        leftIndex = index * 2
        rightIndex = leftIndex + 1
        curValue = self.storage[index]
        # print("current "+str(curValue))
        if len(self.storage) <= leftIndex:
            return
        left = self.storage[leftIndex]
        # print("left "+str(left))
        if len(self.storage) <= rightIndex:
            if (curValue < left): return
            # print("swap {a} and {b}".format(a=curValue, b=left))
            self.storage[index] = left
            self.storage[leftIndex] = curValue
            # print(self.__storageToStr())
            return
        right = self.storage[rightIndex]
        # print("right "+str(right))
        if left == None or right == None:
            print("ERROR: array inconsistency")
            return -20000
        if right < left:
            if (curValue < right): return
            # print("swap {a} and {b}".format(a=curValue, b=right))
            self.storage[rightIndex] = curValue
            self.storage[index] = right
            # print(self.__storageToStr())
            self.__percolateDown(rightIndex)
        else:
            if (curValue < left): return
            # print("swap {a} and {b}".format(a=curValue, b=left))
            self.storage[leftIndex] = curValue
            self.storage[index] = left
            # print(self.__storageToStr())
            self.__percolateDown(leftIndex)

    def top(self) -> int:
        if len(self.storage) == 1:
            return -1
        minValue = self.storage[1]
        if minValue == None:
            print("ERROR: min value is 'None'")
            return -20000
        return minValue

    def heapify(self, nums: List[int]) -> None:
        for num in nums:
            self.push(num)
        return
        
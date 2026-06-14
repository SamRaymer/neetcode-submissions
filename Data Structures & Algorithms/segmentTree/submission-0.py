class Node:
    total: int
    leftIndex: int
    L: 'Node | None'
    rightIndex: int
    R: 'Node | None'

    def __m__(self) -> int:
        return (self.rightIndex + self.leftIndex) // 2

    def __init__(self, nums: list[int], L: int, R: int):
        self.leftIndex = L
        self.rightIndex = R

        if L == R:
            self.total = nums[L]
            return

        self.L = Node(nums, L, self.__m__())
        self.R = Node(nums, self.__m__() + 1, R)
        self.total = self.L.total + self.R.total

    def update(self, index: int, val: int):
        if (self.leftIndex == self.rightIndex):
            self.total = val
            return
        
        if index <= self.__m__():
            if self.L == None:
                print("ERROR: updating nonexistent node")
                return
            self.L.update(index, val)
        else: # index > self.__m__()
            if self.R == None:
                print("ERROR: updating nonexistent node")
                return
            self.R.update(index, val)
        self.total = 0
        if self.R != None:
            self.total += self.R.total
        if self.L != None:
            self.total += self.L.total

    def query(self, L: int, R: int) -> int:
        print("query {L},{R} for node w/ range {LL},{RR}".format(L=L,R=R,LL=self.leftIndex,RR=self.rightIndex))
        if L == self.leftIndex and R == self.rightIndex:
            return self.total
        if (self.L == None or self.R == None):
            print("FATAL: tree structure bad during query")
            return -10000000
        M = self.__m__()
        if R <= M:
            print("running L subquery since {L},{R} <= {M}".format(L=L,R=R,M=M))
            return self.L.query(L, R)
        if L >= M + 1:
            print("running R subquery since {L},{R} >= {M}+1".format(L=L,R=R,M=M))
            return self.R.query(L, R)
        print("splitting {L},{R} across {M}".format(L=L,R=R,M=M))
        return self.L.query(L, M) + self.R.query(M+1, R)


class SegmentTree:
    root: Node
    
    def __init__(self, nums: list[int]):
        self.root = Node(nums, 0, len(nums) - 1)
    
    def update(self, index: int, val: int) -> None:
        return self.root.update(index, val)
    
    def query(self, L: int, R: int) -> int:
        return self.root.query(L, R)


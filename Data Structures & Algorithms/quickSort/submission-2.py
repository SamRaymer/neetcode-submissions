# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.partition(pairs, 0, len(pairs))
        return pairs
    
    def partition(self, pairs: List[Pair], start: int, end: int) -> None:
        if end - start < 1:
            return

        pivotIndex = end - 1
        pivotElement = pairs[end-1]
        print("pivot: {k},{v}".format(k=pivotElement.key, v=pivotElement.value))
        leftIndex = start
        print("to partition: [{r}]".format(r=",".join(pairToStr(pair) for pair in pairs[start:end])))                      
        for i in range(start, end-1):
            if pairs[i].key < pivotElement.key:
                oldLeftPair = pairs[leftIndex]
                pairs[leftIndex] = pairs[i]
                pairs[i] = oldLeftPair
                leftIndex += 1
        print("swapping element {p} with {l}".format(p=pairToStr(pivotElement), l=pairToStr(pairs[leftIndex])))
        pairs[pivotIndex] = pairs[leftIndex]
        pairs[leftIndex] = pivotElement
        
        print("partitioned around {p}: [{r}]".format(p=pivotElement.key,r=",".join(pairToStr(pair) for pair in pairs[start:end])))                      
        print("sorting start={s} end={e}".format(s=start, e=leftIndex))
        self.partition(pairs, start, leftIndex)
        print("sorting start={s} end={e}".format(s=leftIndex + 1, e=end))
        self.partition(pairs, leftIndex + 1, end)
        print("sorted: [{r}]".format(r=",".join(pairToStr(pair) for pair in pairs[start:end])))                      
    
def pairToStr(p: Pair) -> str:
    return "({k},{v})".format(k=p.key,v=p.value)





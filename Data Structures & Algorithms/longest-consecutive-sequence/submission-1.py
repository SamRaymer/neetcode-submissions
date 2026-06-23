class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        while len(numSet) > 0:
            curNum = numSet.pop()
            numSet.add(curNum)
            while curNum - 1 in numSet:
                curNum = curNum - 1
            start = curNum
            while curNum + 1 in numSet:
                numSet.remove(curNum)
                curNum += 1
            numSet.remove(curNum)
            length = curNum - start + 1
            if length > longest:
                longest = length
        return longest

        # class Sequence:
        #     parent: 'Sequence | None' = None
        #     start: int
        #     end: int
        #     def __init__(self, startAndEnd: int):
        #         self.start = startAndEnd
        #         self.end = startAndEnd
        # numberToSeq: Dict[int, Sequence] = {}

        # for num in nums:
        #     if num in numberToSeq:
        #         continue
        #     seqEnd = num
        #     seqStart = num
        #     currentSeq: Sequence
        #     if num + 1 in numberToSeq:
        #         currentSeq = numberToSeq[num + 1]
        #         numberToSeq[num] = currentSeq
        #         seqEnd = currentSeq.end
        #         currentSeq.start = num
        #     else: currentSeq = Sequence(num)
        #     if num - 1 in numberToSeq:
        #         currentSeq.parent = numberToSeq[num - 1]
        #     numberToSeq[num] = currentSeq
        
        # longest = 0
        # for num, seq in numberToSeq.items():
        #     curLength = seq.end - seq.start + 1
        #     while seq.parent is not None:
        #         seq = seq.parent
        #         curLength += seq.end - seq.start + 1
        #     if curLength > longest:
        #         longest = curLength
        # return longest


            


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        class Sequence:
            parent: 'Sequence | None' = None
            start: int
            end: int
            def __init__(self, startAndEnd: int):
                self.start = startAndEnd
                self.end = startAndEnd
        numberToSeq: Dict[int, Sequence] = {}

        for num in nums:
            if num in numberToSeq:
                continue
            seqEnd = num
            seqStart = num
            currentSeq: Sequence
            if num + 1 in numberToSeq:
                currentSeq = numberToSeq[num + 1]
                numberToSeq[num] = currentSeq
                seqEnd = currentSeq.end
                currentSeq.start = num
            else: currentSeq = Sequence(num)
            if num - 1 in numberToSeq:
                currentSeq.parent = numberToSeq[num - 1]
            numberToSeq[num] = currentSeq
        
        longest = 0
        for num, seq in numberToSeq.items():
            curLength = seq.end - seq.start + 1
            while seq.parent is not None:
                seq = seq.parent
                curLength += seq.end - seq.start + 1
            if curLength > longest:
                longest = curLength
        return longest


            


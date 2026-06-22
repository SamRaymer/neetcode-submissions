
import heapq
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCounter = collections.Counter(nums)
        return list(map(lambda numTuple: numTuple[0], freqCounter.most_common(k)))
        # frequency: Dict[int, int] = {}
        # for num in nums:
        #     if num not in frequency: frequency[num] = 0
        #     frequency[num] += 1
        # frequencyTuples: List[tuple[int, int]] = list(map(lambda itemTuple: (itemTuple[1], itemTuple[0]), frequency.items()))
        # heapq.heapify(frequencyTuples)
        # result = []
        # return list(map(lambda itemTuple: itemTuple[1], heapq.nlargest(k, frequencyTuples)))
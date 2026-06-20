class Solution:
    # * We have a list of ints and a target.
    # * We could theoretically record occurrences of each int in a dictionary
    # * Since we only need to check for one occurence, for each number we could check
    #   if indicesByInt[target-currentNumber] has an index stored
    # * Since there is exactly one pair of numbers, we only need to store one location
    #   for each possible number, so the index value is a single int.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indicesByInt: Dict[int, int] = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in indicesByInt:
                # We are guaranteed to run into the smaller index first.
                return [indicesByInt[difference], i]
            indicesByInt[nums[i]] = i
            
        print("We should never reach here...")
        return []
# We need some way of updating previous values with the new values
# We can't linearly do that without going to O(n^2)
# Making one big product that is divided by each element seems most obvious
# ( 2n^2 => O(n) )

# *Without* the division though? That's getting crazy...
# Is there a data structure that updates a bunch of numbers simultaneously

# I gotta see what the answer is. Let's do the division way first.
# If there is a zero, we need to track the zeroes.
# If there's more than one the product will always be zero.

    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     totalProduct = 1
    #     zeroIndex = None
    #     allZeroProducts = False
    #     for i in range(len(nums)):
    #         num = nums[i]
    #         if num == 0 and zeroIndex != None:
    #             return [0 for _ in range(len(nums))]
    #         if num == 0:
    #             zeroIndex = i
    #             continue
    #         totalProduct *= num
    #     result = []
    #     for i in range(len(nums)):
    #         toAppend: int
    #         if zeroIndex != None:
    #             toAppend = totalProduct if i == zeroIndex else 0
    #         else:
    #             toAppend = totalProduct // nums[i]
    #         result.append(toAppend)
    #     return result


# Just read about the prefix/suffix approach, let's do that.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = []
        for i in range(len(nums)):
            if i == 0:
                prefixes.append(1)
                continue
            
            prevPrefix = prefixes[i - 1]
            prevValue = nums[i - 1]
            prefixes.append(prevValue * prevPrefix)
        
        reverseNums = nums.copy()
        reverseNums.reverse()

        suffixes = []
        for i in range(len(reverseNums)):
            if i == 0:
                suffixes.append(1)
                continue
            
            prevSuffix = suffixes[i - 1]
            prevValue = reverseNums[i - 1]
            suffixes.append(prevValue * prevSuffix)
        suffixes.reverse()
        results = []
        for i in range(len(prefixes)):
            results.append(prefixes[i] * suffixes[i])
        return results


# We need some way of updating previous values with the new values
# We can't linearly do that without going to O(n^2)
# Making one big product that is divided by each element seems most obvious
# ( 2n^2 => O(n) )

# *Without* the division though? That's getting crazy...
# Is there a data structure that updates a bunch of numbers simultaneously

# I gotta see what the answer is. Let's do the division way first.
# If there is a zero, we need to track the zeroes.
# If there's more than one the product will always be zero.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        zeroIndex = None
        allZeroProducts = False
        for i in range(len(nums)):
            num = nums[i]
            if num == 0 and zeroIndex != None:
                return [0 for _ in range(len(nums))]
            if num == 0:
                zeroIndex = i
                continue
            totalProduct *= num
        result = []
        for i in range(len(nums)):
            toAppend: int
            if zeroIndex != None:
                toAppend = totalProduct if i == zeroIndex else 0
            else:
                toAppend = totalProduct // nums[i]
            result.append(toAppend)
        return result


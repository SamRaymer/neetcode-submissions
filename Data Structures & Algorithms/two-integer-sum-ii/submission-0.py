class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        curSum = numbers[i] + numbers[j]
        while curSum != target:
            if curSum < target:
                i += 1
            else:
                j -= 1
            curSum = numbers[i] + numbers[j]
        return [i + 1, j + 1]

            

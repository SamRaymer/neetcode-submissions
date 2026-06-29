class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # This is crazy!!! Hell yeah!
        # I can only think of N^3 solutions to this, let's do better

        # * Nums is unsorted :(

        # * Each "visited" group of 3 can go into a set
        # * Iterating like we're doing the N^3 solution, we skip the
        #     already-visited numbers
        #   * How in the hell are we supposed to know we already 
        #       visited before we iterate??
        # Let's... store all the pairs of indices??
        # Oh, and if we store it as a dict of a sum and an index set, we can iterate
        # The dict value should be a list since there could be more than one tuple
        # indicesBySum: Dict[int, List[set[int]]] = {}
        # for i in range(len(nums)):
        #     for jInitial in range(len(nums) - i - 1):
        #         j = jInitial + i + 1
        #         if nums[i] + nums[j] not in indicesBySum:
        #             indicesBySum[nums[i] + nums[j]] = []
        #         indicesBySum[nums[i] + nums[j]].append({i, j})

        # for curSum, curList in indicesBySum.items():
        #     for sumSet in curList:
        #         print("{s}: {u}".format(s=curSum, u=sumSet))
        
        # results: set[frozenset[int]] = set()
        # for i in range(len(nums)):
        #     num = nums[i]
        #     if -num in indicesBySum:
        #         for sumSet in indicesBySum[-num]:
        #             if i not in sumSet:
        #                 searchResult = sumSet.copy()
        #                 searchResult.add(i)
        #                 results.add(frozenset(searchResult))        
        # return list(list(result) for result in results)

        # OK that sucked.
        # Let's sort the nums first and then we can do stuff.

        nums.sort()
        result = []
        for i in range(len(nums))[:-2]:
            # leaving 2, making room for j and k
            if i > 0 and nums[i] == nums[i-1]: continue
            iVal = nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = iVal + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    result.append([iVal, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1]: r -= 1
                    l += 1
                    r -= 1
        return result

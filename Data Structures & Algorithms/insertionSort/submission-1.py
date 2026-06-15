# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: list[Pair]) -> list[list[Pair]]:
        index = 0
        sortedLen = 0
        states: list[list[Pair]] = []
        lastInsert = None
        for index in range(len(pairs)):
            curVal = pairs[index].key
            print("sorting {i}: {p}".format(i=index,p=curVal))
            j = index - 1
            while pairs[j].key > pairs[j+1].key and j >= 0:
                toMoveDown = pairs[j+1]
                pairs[j+1] = pairs[j]
                pairs[j] = toMoveDown 
                j -= 1
            states.append(pairs.copy())
            

        return states
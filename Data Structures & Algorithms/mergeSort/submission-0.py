# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        sublistSize = 1
        sublists: List[List[Pair]] = []
        for pair in pairs:
            sublists.append([pair])
        while (len(sublists) > 1):
            print("Lists: " + ",".join(
                pairListStr(pairs) for pairs in sublists
            ))
            mergeState: List[List[Pair]] = []
            for i in range(len(sublists) // 2):
                A = sublists[i * 2]
                B = sublists[(i * 2) + 1]
                jA = 0
                jB = 0
                mergeAB: List[Pair] = []
                while jA < len(A) or jB < len(B):
                    if jB < len(B) and (jA == len(A) or A[jA].key > B[jB].key):
                        mergeAB.append(B[jB])
                        jB += 1
                    else:
                        mergeAB.append(A[jA])
                        jA += 1
                mergeState.append(mergeAB)
                print("merged: " + pairListStr(mergeAB))
            if len(sublists)%2 == 1:
                mergeState.append(sublists.pop())
            sublists = mergeState
        if len(sublists) == 0: return []
        return sublists[0]

def pairListStr(pairs: List[Pair]) -> str:
    return "[{x}]".format(
        x=",".join(
            "({k},{v})".format(k=pair.key,v=pair.value)for pair in pairs
        )
    )

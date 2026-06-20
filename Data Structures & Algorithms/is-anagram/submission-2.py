class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def buildDict(strIn: str) -> Dict[str, int]:
            result = {}
            for curChar in strIn:
                if curChar in result:
                    result[curChar] += 1
                else:
                    result[curChar] = 1
            return result
        sDict = buildDict(s)
        tDict = buildDict(t)
        for curChar, occurrences in sDict.items():
            if curChar not in tDict: return False
            if tDict[curChar] != occurrences: return False
            tDict.pop(curChar)
            
        return True if len(tDict) == 0 else False




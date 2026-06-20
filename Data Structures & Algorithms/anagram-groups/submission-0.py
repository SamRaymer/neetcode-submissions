class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def encodeStr(toEncode: str) -> str:
            occurrences: Dict[str, int] = {}
            for curChar in toEncode:
                if curChar not in occurrences:
                    occurrences[curChar] = 0
                occurrences[curChar] += 1
            occurenceList = list(occurrences.items())
            occurenceList.sort()
            result = ""
            for indexedChar, timesUsed in occurenceList:
                result += "{u}{v}".format(u=indexedChar, v=timesUsed)
            return result
        indexedByOccurrences: Dict[str, List[str]] = {}
        for curStr in strs:
            encoded = encodeStr(curStr)
            if encoded not in indexedByOccurrences:
                indexedByOccurrences[encoded] = []
            indexedByOccurrences[encoded].append(curStr)

        return list(indexedByOccurrences.values())
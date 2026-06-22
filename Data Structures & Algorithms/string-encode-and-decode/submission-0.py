class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeFragment = lambda x: str(len(x)) + "_" + x
        encoded = ""
        for curStr in strs:
            encoded += encodeFragment(curStr)
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        while len(s) > 0:
            delimiterIndex = s.find("_")
            fragmentLen = int(s[0 : delimiterIndex])
            fragmentIndex = delimiterIndex + 1
            fragment = s[fragmentIndex : fragmentIndex + fragmentLen]
            result.append(fragment)
            s = s[fragmentIndex + fragmentLen:]
        return result

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    def decode(self, s: str) -> List[str]:
        l,r = 0,1
        res = []
        while l < len(s):
            while s[r] != "#":
                r += 1
            s_length = int(s[l:r])
            res.append(s[r+1:r+1+s_length])
            l = r+1+s_length
            r = l+1
        return res

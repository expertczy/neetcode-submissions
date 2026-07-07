class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable={}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in hashtable:
                hashtable[sorted_s].append(s)
            else:
                hashtable[sorted_s]=[s]
        return list(hashtable.values())
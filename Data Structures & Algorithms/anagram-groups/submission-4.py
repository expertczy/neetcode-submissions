class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')]+=1
            count_tuple = tuple(count)
            if count_tuple in hashtable:
                hashtable[count_tuple].append(s)
            else:
                hashtable[count_tuple]=[s]
        return list(hashtable.values())
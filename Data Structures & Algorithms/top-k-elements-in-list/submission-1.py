class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num] = count.get(num,0)+1
        sorted_count = sorted(count.items(),key=lambda count:count[1], reverse=True)
        res = []
        for i in range(k):
            res.append(sorted_count[i][0])
        return res
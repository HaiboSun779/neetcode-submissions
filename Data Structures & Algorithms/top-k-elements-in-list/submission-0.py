class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        sorted_key = sorted(count, key = count.get, reverse = True)

        return sorted_key[:k]
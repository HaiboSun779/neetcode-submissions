class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        used = set()

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for num in nums:
                if num not in used:
                    perm.append(num)
                    used.add(num)

                    dfs()

                    perm.pop()
                    used.remove(num)
        dfs()
        return res
                


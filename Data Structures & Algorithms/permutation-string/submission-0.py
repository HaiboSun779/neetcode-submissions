class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = {}
        count2 = {}

        for ch in s1 :
            count1[ch] = count1.get(ch, 0) + 1
        
        for ch in s2[:len(s1)]:
            count2[ch] = count2.get(ch, 0) + 1
        
        if count1 == count2:
            return True
        for right in range(len(s1), len(s2)):
            ch = s2[right]
            count2[ch] = count2.get(ch, 0) + 1
            old = s2[right - len(s1)]
            count2[old] -= 1

            if count2[old] == 0:
                del count2[old]

            if count1 == count2:
                return True
        return False
        
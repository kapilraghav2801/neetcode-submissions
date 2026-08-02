from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1
        for c in t:
            count[ord(c) - ord('a')] -= 1
        
        # for c in count:
        #     if c != 0:
        #         return False
        # return True

        return all(c == 0 for c in count)
        # count_s = Counter(s)
        # count_t = Counter(t)


        # return count_s == count_t

        #return sorted(s) == sorted(t)

        
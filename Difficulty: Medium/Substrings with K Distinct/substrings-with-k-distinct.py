class Solution:
    def countSubstr(self, s, k):
        def atMostK(s, k):
            count = {}
            left = 0
            res = 0
            for right in range(len(s)):
                count[s[right]] = count.get(s[right], 0) + 1
                while len(count) > k:
                    count[s[left]] -= 1
                    if count[s[left]] == 0:
                        del count[s[left]]
                    left += 1
                res += right - left + 1
            return res
        
        return atMostK(s, k) - atMostK(s, k - 1)

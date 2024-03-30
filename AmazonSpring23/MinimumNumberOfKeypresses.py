class Solution:
    def minimumKeypresses(self, s: str) -> int:
        count = [0] * 26
        for i in range(0, len(s)):
            count[(ord(s[i]) % 97)] += 1
        count.sort(reverse=True)
        s = 1*sum(count[0:9]) + 2*sum(count[9:18]) + 3*sum(count[18:])
        return s
 
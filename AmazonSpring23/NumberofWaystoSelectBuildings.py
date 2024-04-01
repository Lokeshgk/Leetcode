class Solution:
    def numberOfWays(self, s: str) -> int:

        possible_ways = 0

        # count no of zeroes and ones
        n_zeroes = s.count('0')
        n_ones = len(s) - n_zeroes

        # count no of zeroes before index i
        zero_i = 0
        one_i = 0

        if s[0] == '0':
            zero_i += 1
        else:
            one_i += 1

        for i in range(1, len(s)-1):
            if s[i] == '1':
                possible_ways += (zero_i * (n_zeroes - zero_i))
                one_i += 1
            elif s[i] == '0':
                possible_ways += (one_i * (n_ones - one_i))
                zero_i += 1
        
        return possible_ways

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        len_s = len(s)
        len_t = len(t)

        s_index = 0
        t_index = 0
        while s_index < len_s and t_index < len_t:
            if s[s_index] == t[t_index]:
                s_index += 1
                t_index += 1
            else:
                s_index += 1
        return len_t - t_index

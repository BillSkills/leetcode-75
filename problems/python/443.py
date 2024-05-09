# [AC 05/09/2024]
# 443. String Compression
# https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0 # i tracks chars[] index
        ans = 0 # ans tracks compressed index

        # iterates through chars[]
        while i < len(chars):
            letter = chars[i]
            count = 0
            
            # iterates through a repeat sequence
            while i < len(chars) and chars[i] == letter:
                count += 1
                i += 1

            chars[ans] = letter
            ans += 1

            if count > 1:
                for c in str(count): # copy back to chars[]
                    chars[ans] = c
                    ans += 1

        return ans
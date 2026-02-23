class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_hash = {}

        for letter in s:
            if letter not in word_hash:
                word_hash[letter] = 1
            else:
                word_hash[letter] += 1

        for letter in t:
            if letter not in word_hash:
                return False
            else:
                word_hash[letter] -= 1
                if word_hash[letter] < 0:
                    return False

        return sum(word_hash.values()) == 0

        # Time complexity (O(s) + O(t), represent length of both s and t, if same O(s=t) since 2O(s=t) is constant of O(s=t)
        # Space complexity (O(s))

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        counts = collections.Counter()
        for right in range(1,len(s) + 1):
            counts[s[right - 1]] += 1
            
            most_common_char_k = counts.most_common(1)[0][1]
            
            if right - left - most_common_char_k > k:
                counts[s[left]] -= 1
                left += 1
        
        return right - left
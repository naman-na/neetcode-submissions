from collections import Counter
import itertools
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        #print(freq)

        return [item[0] for item in freq.most_common(k)]        
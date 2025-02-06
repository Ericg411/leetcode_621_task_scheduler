from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_freq = max(freq.values())
        max_freq_count = list(freq.values()).count(max_freq)
        gap_count = max_freq - 1
        gap_length = n - max_freq_count + 1
        empty_spaces = gap_count * gap_length
        available_tasks = len(tasks) - (max_freq * max_freq_count)
        idles = max(0, (empty_spaces - available_tasks))
        
        return len(tasks) + idles
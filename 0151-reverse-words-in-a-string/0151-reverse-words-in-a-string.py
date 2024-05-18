class Solution:
    def reverseWords(self, s: str) -> str:
        lists = s.split()
        return ' '.join(lists[~i] for i in range(len(lists)))
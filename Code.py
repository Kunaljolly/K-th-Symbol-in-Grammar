class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1:
            return 0

        parent = self.kthGrammar(n - 1, (k + 1) // 2)
        return 0 if parent == 1 and k % 2 == 0 or parent == 0 and k % 2 == 1 else 1

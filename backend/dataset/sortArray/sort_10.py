class Solution:
    def sortArray(self, N):
        L = len(N)
        return [N.pop(min(range(L-i), key = lambda x: N[x])) for i in range(L)]
		
		

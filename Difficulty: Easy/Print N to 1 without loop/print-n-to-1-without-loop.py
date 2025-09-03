class Solution:
    def printNos(self, n):
        # Base case
        if n == 0:
            return
        # Print current number
        print(n, end=' ')
        # Recursive call with n-1
        self.printNos(n - 1)

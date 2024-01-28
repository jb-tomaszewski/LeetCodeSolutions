class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n

sol = Solution()
x = float(input("x = "))
n = int(input("n = "))
print(sol.myPow(x, n))


class Solution(object):
    def reverse(self, x):
        s = (x>0)-(x<0)
        r = int(repr(s * x)[::-1])
        return s * r * (r < 2 ** 31)

solu = Solution()
print(solu.reverse(123))
print(solu.reverse(-123))
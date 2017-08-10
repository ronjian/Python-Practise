import numpy as np
import itertools

class Solution(object):
    def matrixReshape(self, nums, r, c):
        try:
            return np.reshape(nums, (r, c)).tolist()
        except:
            return nums

    def matrixReshape2(self, nums, r, c):
        flat = sum(nums, [])
        if len(flat) != r * c:
            return nums
        tuples = zip(*([iter(flat)] * c))
        return map(list, tuples)

    def matrixReshape3(self, nums, r, c):
        if r * c != len(nums) * len(nums[0]):
            return nums
        it = itertools.chain(*nums)
        return [list(itertools.islice(it, c)) for _ in range(r)]

solu = Solution()
r = solu.matrixReshape([[1,2],[3,4]],1,4)
print(type(r))
print(r)
r2 = solu.matrixReshape2([[1,2],[3,4]],1,4)
print(type(r2))
print(r2)
r3 = solu.matrixReshape3([[1,2],[3,4]],1,4)
print(type(r3))
print(r3)
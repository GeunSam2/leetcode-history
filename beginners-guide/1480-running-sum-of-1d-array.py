# running sum은 누계를 의미하는 듯

# my solution
# Time: O(N^2), Space: O(N)
# sum() 함수를 사용하면 시간복잡도가 O(N)이므로, 이중 for문을 사용하면 O(N^2)이 된다.
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.append(sum(nums[:i+1]))
        return result
# 리스트컴프리헨션을 사용하면 더 간단하게 표현할 수 있다.
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[:i+1]) for i in range(len(nums))]
    
# optimal solution
# Time: O(N), Space: O(N)
# 이중 for문을 사용하지 않고, 누계를 구하는 방법
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        sum = 0
        for num in nums:
            sum += num
            result.append(sum)
        return result
    
# optimal solution 2
from itertools import accumulate
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))
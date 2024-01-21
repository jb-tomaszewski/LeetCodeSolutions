from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) < 1 or len(nums) > 3 * (10 ** 4):
            return 0

        currentNums = []

        for num in nums:
            if num < -3 * (10 ** 4) or num > 3 * (10 ** 4):
                return 0

            if num not in currentNums:
                currentNums.append(num)
            else:
                currentNums.remove(num)

        return currentNums[0]

sol = Solution()
value = input("nums = ")

if "[" in value and "]" not in value:
    print(0)
elif "]" in value and "[" not in value:
    print(0)
else:
    value = value.replace("[", "")
    value = value.replace("]", "")
    value = value.split(",")
    output = sol.singleNumber(list(map(int, value)))
    print(output)
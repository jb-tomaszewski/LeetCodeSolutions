from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numDict = {}

        if len(nums) > 100:
            return 0


        for num in nums:
            if num < 1 or num > 100:
                return 0

            if num not in numDict:
                numDict[num] = 1
            else:
                numDict[num] += 1

        output = 0
        for num in numDict:
            numPairs = (numDict[num] * (numDict[num] - 1)) / 2
            output += numPairs

        return int(output)


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
    output = sol.numIdenticalPairs(list(map(int, value)))
    print(output)


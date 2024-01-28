from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output = [-1, -1]

        for index in range(len(nums)):
            if nums[index] == target:
                if output[0] == -1:
                    output[0] = index
                    output[1] = index
                else:
                    output[1] = index

        return output

sol = Solution()
nums = input("nums = ")
target = int(input("target = "))

if "[" in nums and "]" not in nums:
    print("[-1,-1]")
elif "]" in nums and "[" not in nums:
    print("[-1,-1]")
else:
    nums = nums.replace("[", "")
    nums = nums.replace("]", "")
    nums = nums.split(",")
    output = sol.searchRange(list(map(int, nums)), target)
    print(output)
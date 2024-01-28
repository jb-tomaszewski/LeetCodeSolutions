class Solution:
    def intToRoman(self, num: int) -> str:
        romanDict = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400,
                     "D": 500, "CM": 900, "M": 1000}

        output = ""
        while num > 0:
            currentKey = ""
            for key in romanDict:
                if num >= romanDict[key]:
                    currentKey = key
                else:
                    break

            num -= romanDict[currentKey]
            output += currentKey

        return output

sol = Solution()
num = int(input("num = "))
print(sol.intToRoman(num))
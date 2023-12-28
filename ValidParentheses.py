class Solution:
    def isValid(self, s: str) -> bool:
        openParentheses = ["(", "[", "{"]
        closedParentheses = [")", "]", "}"]
        currentOpenIndex = -1
        previousOpenIndeces = []
        if len(s) <= 1 or len(s) % 2 != 0:
            return False

        for i in range(len(s)):
            if s[i] in openParentheses:
                if currentOpenIndex > -1:
                    previousOpenIndeces.append(currentOpenIndex)
                currentOpenIndex = i
            elif s[i] in closedParentheses:
                if currentOpenIndex == -1 or not self.compareOpenAndClosed(s[currentOpenIndex], s[i]):
                    return False
                else:
                    if len(previousOpenIndeces) > 0:
                        currentOpenIndex = previousOpenIndeces.pop()
                    else:
                        currentOpenIndex = -1
            else:
                return False

        if len(previousOpenIndeces) > 0:
            return False

        # If we make it here, the string is valid.
        return True

    def compareOpenAndClosed(self, open: str, closed: str) -> bool:
        match open:
            case "(":
                if closed == ")":
                    return True
            case "[":
                if closed == "]":
                    return True
            case "{":
                if closed == "}":
                    return True
        return False


sol = Solution()
value = input("Input: ")

output = sol.isValid(value)
if output:
    print("true")
else:
    print("false")
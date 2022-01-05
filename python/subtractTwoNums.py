# Example 1:

# Input: num1 = [3, 4, 5], num2 = [2, 2, 1] 
# Output: [1, 2, 4]
# Example 2:

# Input: num1 = [1, 0], num2 = [9]
# Output: [1]
# 1<= num1.length , num2.length<=100
# Digits in the array are Non - negative

class Solution(object):
    def subtractTwoNums(self, num1, num2):
        tempString1 = ""
        tempString2 = ""
        if len(num1) == 0:
            tempString1 = "0"
        else:
            for element in num1:
                tempString1 += str(element)
        if len(num2) == 0:
            tempString2 = "0"
        else:
            for element in num2:
                tempString2 += str(element)
        wholeNumber1 = int(tempString1)
        wholeNumber2 = int(tempString2)
        output = wholeNumber1 - wholeNumber2
        print(output)
        return output
        
        
def main():

    num1 = [200, 200, 560]
    num2 = [100000, 620] 

    result = Solution()

    result.subtractTwoNums(num1, num2)

if __name__ == "__main__":
    main()
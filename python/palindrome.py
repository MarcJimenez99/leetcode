class Solution(object):
    def isPalindrome(self, x):
        if (x < 0):
            print("Number negative. False")
            return False
        else:
            numToString = str(x)
            reverseString = numToString[::-1]
            if (numToString == reverseString):
                print("True")
                return True
            else:
                print("False")
                return False
 
        
        
def main():

    input = 120000

    result = Solution()

    result.isPalindrome(input)


if __name__ == "__main__":
    main()
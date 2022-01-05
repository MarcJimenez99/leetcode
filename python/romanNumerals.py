import math

class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        # Initialize our dictionary with all of our existing roman numerals
        output = 0
        # Initialize our output. 
        if len(s) == 0:
            return 0
        for i in range(0, len(s) - 1):
            # Iterate from the beginning of our string to the second to last character
            currentCharValue = romanDict[s[i]]
            nextCharValue = romanDict[s[i+1]]
            if currentCharValue >= nextCharValue:
                # Check if the current character value is greater than the next character value. If so add it to our total output
                output += currentCharValue
            else:
                # Else, subtract the current character value from our output
                output -= currentCharValue
        # Finally add the value of the last character to our output since we know it must be an addition case since no roman numeral follows it.
        lastCharValue = romanDict[s[-1]]
        output += lastCharValue
        return output 
            
        

def main():

    s = "MCMXCIV"
    result = Solution()
    romanNumeralValue = result.romanToInt(s)
    print(romanNumeralValue)

if __name__ == "__main__":
    main()


# Roman to Integer
# Given a roman numeral covert to an integer.
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

#   Symbol       Value
#   I             1
#   V             5
#   X             10
#   L             50
#   C             100
#   D             500
#   M             1000
#   For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. 
# Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#   I can be placed before V (5) and X (10) to make 4 and 9. 
#   X can be placed before L (50) and C (100) to make 40 and 90. 
#   C can be placed before D (500) and M (1000) to make 400 and 900.

# Solution:
# Making use of a dictionary we can easily identify the numeral value of each character as we iterate through. Now we must iterate through the string in order to identify the summation of 
# Roman numerals. We know that subtraction will only occur when the following roman numeral is greater than the current roman numeral. For example with the Roman Numeral "MDC", we know that
# it translates to 1000+500+100. This gives us the roman numeral value of 1600. Since each roman numeral is greater than the following roman numeral we will always just add across. In addition,
# we know that no matter what we will add the very last roman numeral in our given string since subtraction will only occur if another roman numeral follows our current roman numeral. Therefore,
# we can iterate from the beginning of our string to the second to last character and do the operations of addition and subtraction depending on what follows our current roman numeral and then
# finally just add the last character to our total. 
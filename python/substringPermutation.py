import math

class Solution:

    def substringCompare(s1, s2, i, permDict) -> bool:
        tempStr = s2[i:(i+len(s1))]
        print(tempStr)
        lengthString1 = len(s1)
        for letter in tempStr:
            if letter in permDict:
                lengthString1 -= 1
                if lengthString1 == 0:
                    return True
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        permDict = {}
        for letter in s1:
            permDict[letter] = 1
        if len(s1) == len(s2):
            tempStr = s2[0:(0+len(s1))]
            print(tempStr)
            lengthString1 = len(s1)
            for letter in tempStr:
                if letter in permDict:
                    lengthString1 -= 1
                    if lengthString1 == 0:
                        return True
        else:
            for i in range(0, len(s2)-len(s1)):
                tempStr = s2[i:(i+len(s1))]
                print(tempStr)
                lengthString1 = len(s1)
                print(lengthString1)
                for letter in tempStr:
                    permDictCopy = dict(permDict)
                    if (letter in permDictCopy) and permDictCopy[letter] == 1:
                        lengthString1 -= 1
                        permDictCopy[letter] -= 1
                        if lengthString1 == 0:
                            return True
        return False
                    
                
        

def main():

    s1 = "hello"
    s2 = "ooolleoooleh"
    result = Solution()
    isPermutation = result.checkInclusion(s1, s2)
    if isPermutation:
        print(f'"{s2}" Contains a permutation of "{s1}"')
    else:
        print(f'"{s2}" Does not contain a permutation of "{s1}"')

if __name__ == "__main__":
    main()

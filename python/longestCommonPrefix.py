class Solution(object):
    def longestCommonPrefix(self, strs):
        min = len(strs[0])
        prefix = strs[0]
        for element in strs:
            if len(element) < min:
                min = len(element)
                prefix = element[0:min]
    
        if prefix == "":
            return prefix

        for i in range(min, 0, -1):
            foundMisMatch = False
            for j in range(0, len(strs)):
                if strs[j][0:i] != prefix:
                    foundMisMatch = True
                    break
            if foundMisMatch:
                if len(prefix) == 1:
                    return ""
                else:
                    prefix = prefix[:-1]
                    foundMisMatch = False
            else:
                return prefix
          
                
                
            # for element in strs:
            #     if element[0:i] != prefix:
            #         prefix = element[0:i-1]
            #     else:
            #         continue
 

def main():

    result = Solution()

    strs = ["poop", "polar bear", "pomegranite"]

    prefix = result.longestCommonPrefix(strs)

    print(prefix)

if __name__ == "__main__":
    main()
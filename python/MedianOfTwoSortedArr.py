import math

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        mergedArray = sorted(nums1 + nums2)
        print(mergedArray)
        if len(mergedArray) % 2 == 0:
            leftIndex = int((len(mergedArray) / 2) - 1)
            leftValue = mergedArray[leftIndex]
            rightIndex = leftIndex = int((len(mergedArray) / 2))
            rightValue = mergedArray[rightIndex]
            medianValue = (leftValue+rightValue)/2
            print(medianValue)
            return medianValue
        else:
            medianIndex = int(math.ceil(len(mergedArray) / 2))
            medianValue = mergedArray[medianIndex-1]
            print(medianValue)
            return medianValue
        

def main():

    nums1 = [1, 3]
    nums2 = [2]

    result = Solution()

    result.findMedianSortedArrays(nums1, nums2)


if __name__ == "__main__":
    main()
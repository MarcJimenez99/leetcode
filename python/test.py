import math

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        mergedArray = sorted(nums1 + nums2)
        if len(mergedArray) % 2 == 0:
            midRightIndex = int(len(mergedArray)/2)
            midLeftIndex = int(midRightIndex - 1)
            median = (mergedArray[midLeftIndex] + mergedArray[midRightIndex]) / 2
            return median
        else:
            return mergedArray[(len(mergedArray)/2)]
        

def main():

    nums1 = [1, 2]
    nums2 = [3, 4]

    result = Solution()

    print(result.findMedianSortedArrays(nums1, nums2))


if __name__ == "__main__":
    main()


# Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log(m+n)).
# # This means that the algorithm's running time should grow in proportion to the logarithm of the input size. 
# # So, as the size of our two arrays represented as m and n, grow exponentially, the time it which it takes to solve  
# # for the median of the combined array (in this case merged array), will be O(log(m + n))

# For simplicity sake we will 
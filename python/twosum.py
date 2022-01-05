class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for index, element in enumerate(nums):
            print(f'Index: {index}')
            print(f'Element: {element}')
            second_element = target - element
            print(f'Second Element: {second_element}')
            if second_element in d:
                print([d[second_element], index])
                print(f'Final Dictionary: {d}')
                return [d[second_element], index]
            else:
                d[element] = index
            print(f'Dictionary: {d}')

def main():

    numList = [11,2,7,15]

    target = 9

    result = Solution()

    result.twoSum(numList, target)



if __name__ == "__main__":
    main()
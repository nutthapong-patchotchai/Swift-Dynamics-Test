"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 4

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list) -> int | str:
        if not numbers:
            return "list can not blank"
        return numbers.index(max(numbers))
    
def main():
    numbers = [1,2,1,3,5,6,4]
    print(Solution().find_max_index(numbers))

    numbers = []
    print(Solution().find_max_index(numbers))

if __name__ == "__main__":
    main()

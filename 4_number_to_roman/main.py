"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_roman(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        if number > 10_000_000:
            return "number exceeds maximum limit"
        
        val = [
            1000000, 900000, 500000, 400000, 100000, 90000, 50000, 40000, 10000, 9000, 5000, 4000, 1000, 900, 500, 400,
            100, 90, 50, 40, 10, 9, 5, 4, 1
        ]
        syb = [
            "M̅", "C̅M̅", "D̅", "C̅D̅", "C̅", "X̅C̅", "L̅", "X̅L̅", "X̅", "ĪX̅", "V̅", "ĪV̅", "M", "CM", "D", "CD",
            "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
        ]
        
        roman_num = ''
        i = 0
        while number > 0:
            for _ in range(number // val[i]):
                roman_num += syb[i]
                number -= val[i]
            i += 1
        return roman_num
    
def main():
    number = 101
    print(Solution().number_to_roman(number))

    number = -1
    print(Solution().number_to_roman(number))

if __name__ == "__main__":
    main()

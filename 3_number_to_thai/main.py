"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        if number > 1000:
            return "number exceeds maximum limit"

        thai_numerals = ["ศูนย์", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
        thai_units = ["", "สิบ", "ร้อย", "พัน"]

        def convert_to_thai_text(num):
            if num == 0:
                return thai_numerals[0]
            
            result = ""
            num_str = str(num)
            length = len(num_str)

            for i, digit in enumerate(num_str):
                digit_int = int(digit)
                if digit_int != 0:
                    if digit_int == 1:
                        if i == length - 1:
                            result += "เอ็ด"
                        elif i == length - 2:
                            result += ""
                        else:
                            result += thai_numerals[digit_int]
                    elif digit_int == 2 and i == length - 2:
                        result += "ยี่"
                    else:
                        result += thai_numerals[digit_int]
                    
                    result += thai_units[length - i - 1]

            return result

        return convert_to_thai_text(number)
    
def main():
    number = 1000
    print(Solution().number_to_thai(number))

    number = 101
    print(Solution().number_to_thai(number))

    number = -1
    print(Solution().number_to_thai(number))


if __name__ == "__main__":
    main()
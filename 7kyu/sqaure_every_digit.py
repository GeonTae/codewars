"""
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 9^2 is 81 and 1^2 is 1.

Note: The function accepts an integer and returns an integer
"""


def square_digits(num):
    num = str(num)   #"9119"
    new_num = ''
    for i in num:
        i = int(i)
        new_num = new_num + str(i*i)
    return int(new_num)

print(square_digits(9119))
print(square_digits(0))


# string = [81, 1, 1, 81]
# string = str(string)
# k = ''
# for i in string:
#     print(i)
#     k = k + i
# print(k)
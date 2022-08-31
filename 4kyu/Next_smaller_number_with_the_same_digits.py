'''
Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

For example:

next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017
Return -1 (for Haskell: return Nothing, for Rust: return None), when there is no smaller number that contains the same digits. 
Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.

next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
some tests will include very large numbers.
test data only employs positive integers.
The function you write for this challenge is the inverse of this kata: "Next bigger number with the same digits."
'''



"""
https://stackoverflow.com/questions/59005190/find-next-smallest-number-with-same-digits-python
Starting from the right, find the first digit that has at least one smaller digit to its right. We'll call that digit X.
Then find the largest digit that is to the right of X, and is smaller than X. We'll call that digit Y.
Swap X and Y. This makes the number smaller.
Then sort all of the digits to the right of Y in descending order. This makes the number as big as possible, without making it bigger than the original.
"""

from itertools import permutations as permutations # for permutations
 

def next_smaller(n):
    num = str(n)
    num_arr = []

    for i in num:
        num_arr.append(i)

    num_permutations = list(permutations(num_arr, len(num_arr)))
    num_permutations = set(num_permutations)
    num_permutations = list(num_permutations)

    for i in range(len(num_permutations)):
        num_permutations[i] = ''.join(num_permutations[i])

    #removing dupplicates 1   => this method takes so much time

    # new_num_permutations = []
    # for i in num_permutations:
    #     if i not in new_num_permutations:
    #         new_num_permutations.append(i)
    # new_num_permutations.sort(reverse=True)

    #removing dupplicates 2 
    num_permutations.sort(reverse=True)

    #when the next smaller number doesn't exist
    if num_permutations.index(num) == len(num_permutations)-1:
        return -1
    else:
        tmp = num_permutations[num_permutations.index(num)+1] # next smaller number
        # when the next smaller number starts with 0
        if tmp[0] == '0':
            return -1
        else:
            return int(tmp)



print(next_smaller(907))    # 790)
print(next_smaller(531))    # 513)
print(next_smaller(135))    # -1)
print(next_smaller(2071))   # 2017)
print(next_smaller(414))    # 144)
print(next_smaller(123456798))  # 123456789)
print(next_smaller(123456789))  # -1)
print(next_smaller(1234567908)) # 1234567890)

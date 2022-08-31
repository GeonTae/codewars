'''
Description
Given a list of integers A, for each pair of integers (first, last) in list ranges, calculate the sum of the values in A between indices first and last (both inclusive), and return the greatest resulting sum.

Example
A = [1, -2, 3, 4, -5, -4, 3, 2, 1]
ranges = [(1, 3), (0, 4), (6, 8)]

result = 6
For ranges[0] = (1, 3) the sum is A[1] + A[2] + A[3] = 5
For ranges[1] = (0, 4) the sum is A[0] + A[1] + A[2] + A[3] + A[4] = 1
For ranges[2] = (6, 8) the sum is A[6] + A[7] + A[8] = 6
The greatest sum is 6
Notes
The list of ranges will never be empty;
This is a challenge version, you should implement an efficient algorithm to avoid timing out;
If this task is too difficult for you, try the simple version.
About random testcases
Small tests: 100 testcases
each integers-list : 5-20 elements
each ranges-list : 1-6 elements
Big tests: 50 testcases
each integers-list : 100000 elements
each ranges-list : 10000 elements
'''


def max_sum(a, ranges):

    tmp = 0
    m_s = 0
    for ran in ranges:
        for i in range(ran[0], ran[1]+1):
            tmp = tmp + a[i]
        if m_s < tmp:
            m_s = tmp
        tmp = 0
    return m_s




# def max_sum(a, ranges):
    # max = float("-inf") # -infinity
    # for range in ranges:
    #     sum_range = sum(a[range[0]:range[1]+1])
    #     if max > sum_range:
    #         max = max
    #     else:
    #         max = sum_range
    # return max


    # def max_sum(a, ranges):
    # sum_arr = []
    # for range in ranges:
    #     sum_arr.append(sum(a[range[0]:range[1]+1]))
    # return max(sum_arr)


print(max_sum([1, -2, 3, 4, -5, -4, 3, 2, 1], [(1, 3), (0, 4), (6, 8)]))    # 6)
print(max_sum([1, -2, 3, 4, -5, -4, 3, 2, 1], [(1, 3)]))    # 5)
print(max_sum([1, -2, 3, 4, -5, -4, 3, 2, 1], [(1, 4), (2, 5)]))    # 0)





# a = [(1, 3), (0, 4), (6, 8)]

# for i in a:
#     print(i)
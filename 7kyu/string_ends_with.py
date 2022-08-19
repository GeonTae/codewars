# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
# Examples:
# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def solution(string, ending):
    if ending == '':
        return True
    else:
        if string[-len(ending):] == ending:
            return True
        else:
            return False

print(solution('abcde', 'cde'))
print(solution('abcde', 'abc'))
print(solution('abcde', ''))



# string = 'abcde'
# print(string[-1])
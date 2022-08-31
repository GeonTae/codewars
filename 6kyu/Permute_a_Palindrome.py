'''
Write a function that will check whether ANY permutation of the characters of the input string is a palindrome. 
Bonus points for a solution that is efficient and/or that uses only built-in language functions. 
Deem yourself brilliant if you can come up with a version that does not use any function whatsoever.

Example
madam -> True
adamm -> True
junk -> False

Hint
The brute force approach would be to generate all the permutations of the string and check each one of them whether it is a palindrome. 
However, an optimized approach will not require this at all.
'''
# solution: if the number of odd numbers of the input string is greater than 1, then it is not a palindrome.

def permute_a_palindrome (input):
    
    output = True
    oddnum_count_arr = []

    for i in input:
        if input.count(i)%2 == 0:
            output = True

        else: # input.count(i)%2 == 1:
            if i not in oddnum_count_arr:  
                oddnum_count_arr.append(i)
                # in the case same number appears more than once 
                # ex)'aaa' or ababa' => oddnum_count_arr = ['a', 'a', 'a'] => 3 > 1 : false  => wrong answer
                # so we need to put the number in the array only once
    
    if len(oddnum_count_arr) > 1: # check if the number of odd numbers is greater than 1
        output = False

    return output






print(permute_a_palindrome("a"))    # True)
print(permute_a_palindrome("aa"))   # True)
print(permute_a_palindrome("baa"))  # True)
print(permute_a_palindrome("aab"))  # True)
print(permute_a_palindrome("baabcd"))   # False)
print(permute_a_palindrome("racecars")) # False)
print(permute_a_palindrome("abcdefghba"))   # False)
print(permute_a_palindrome("")) # True)
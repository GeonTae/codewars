'''
Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

Examples
Valid arrays
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 2
5921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:

a = [121, 144, 19, 161, 19, 144, 19, 11] 
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
Invalid arrays
If, for example, we change the first number to something else, comp is not returning true anymore:

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 132 is not the square of any number of a.

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 36100 is not the square of any number of a.

Remarks
a or b might be [] or {} (all languages except R, Shell).
a or b might be nil or null or None or nothing (except in C++, COBOL, Crystal, D, Dart, Elixir, Fortran, F#, Haskell, Nim, OCaml, Pascal, Perl, PowerShell, Prolog, PureScript, R, Racket, Rust, Shell, Swift).
If a or b are nil (or null or None, depending on the language), the problem doesn't make sense so return false.

Note for C
The two arrays have the same size (> 0) given as parameter in function comp.
'''
def comp(array1, array2):
    check = True
    if array1 == None or array2 == None:
        check = False
        return check

    if len(array1) != len(array2):
        check = False

    else:
        for i in array1:
            if i**2 in array2 and array1.count(i) == array2.count(i**2):  # checking if the number is in the array and the number of times it appears is the same in both arrays
                continue
            else:
                check = False
    return check

# a = [121, 144, 19, 161, 19, 144, 19, 11]  
# b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
# print(comp(a, b))	
# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
# print(comp(a1, a2)) # True
# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
# print(comp(a1, a2)) #False
# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
# print(comp(a1, a2)) #False

a1 = None
a2 = None
print(comp(a1, a2)) #False

'''
Traceback (most recent call last):
  File "/workspace/default/.venv/lib/python3.10/site-packages/codewars_test/test_framework.py", line 112, in wrapper
    func()
  File "/workspace/default/tests.py", line 25, in basics
    test.assert_equals(comp(a1, a2), False)
  File "/workspace/default/solution.py", line 3, in comp
    if len(array1) != len(array2):
TypeError: object of type 'NoneType' has no len()
'''
# => guessing it gave list a1 or a2 = None 
# => so I added a1 or array1 == [] or array2 == []:


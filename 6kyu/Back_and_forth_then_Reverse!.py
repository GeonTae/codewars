'''
A list S will be given. You need to generate a list T from it by following the given process:

Remove the first and last element from the list S and add them to the list T.
Reverse the list S
Repeat the process until list S gets emptied.
The above process results in the depletion of the list S. Your task is to generate list T without mutating the input List S.

Example
S = [1,2,3,4,5,6]
T = []

S = [2,3,4,5] => [5,4,3,2]
T = [1,6]

S = [4,3] => [3,4]
T = [1,6,5,2]

S = []
T = [1,6,5,2,3,4]
return T
Note
size of S goes up to 10^6
Keep the efficiency of your code in mind.
Do not mutate the Input.
'''


# def arrange(S):   # time limit exceeded
#     T = []
#     K = S.copy()
#     while K:
#         T.append(K.pop(0))
#         if len(K) >0:
#             T.append(K.pop(-1))
#         K.reverse()

#     return T

def arrange(S):
    T = []
    k = 0
    if len(S)%2 == 0:
        for i in range(int(len(S)/2)):
            if k%2 == 0:
                T.append(S[i])
                T.append(S[-1-i])
            else:
                T.append(S[-1-i])
                T.append(S[i])
            k += 1
            
    
    else: #len(S)%2 == 1
        for i in range(int(len(S)/2)+1):
            if k%2 == 0:
                T.append(S[i])
                if i != int(len(S)/2):
                    T.append(S[-1-i])
            else:
                T.append(S[-1-i])
                if i != int(len(S)/2):
                    T.append(S[i])
            k += 1
    return T

            

TESTS = [
    ([1,2], [1,2]),
    ([4, 3, 2], [4, 2, 3]),
    ([9, 7, -2, 8, 5, -3, 6, 5, 1], [9, 1, 5, 7, -2, 6, -3, 8, 5]),
    ([1], [1]),
    ([], []),
    ([2, 4, 3, 4],[2, 4, 3, 4]),
]

for i,(inp,exp) in enumerate(TESTS,1):
    inp2 = inp[:]
    # print(exp)
    if arrange(inp) == exp:
        print("True\n")
        pass
    else:
        print("test"+str(i))
        print(arrange(inp))
        print("false\n")
    if inp != inp2:
        print("Don't mutate the input")




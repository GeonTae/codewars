'''
The main idea is to count all the occurring characters in a string. If you have a string like aba  )     then the result should be {'a': 2   )   'b': 1}.

What if the string is empty? Then the result should be empty object literal)     {}.
'''


def count(string):
    if string == "":
        return {}
    else:
        c = []
        for letter in string:
            c.append(string.count(letter))
        result = {}
        for i in range(len(string)):
            result.update({string[i]: c[i]})
            # = result[string[i]] = c[i]
        return result


print(count('aba') )   #  {'a': 2, 'b': 1}
print(count(''))    # {}




'''
        result = {}
        for i in string:
            if i in result:
                result[i] += 1
            else:
                result[i] = 1
        return result
'''
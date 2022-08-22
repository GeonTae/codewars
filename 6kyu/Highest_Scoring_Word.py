'''
Given a string of words)    # you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1)   # b = 2)    # c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same)    # return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
'''

import string
global letters
letters = []


def high(sentence):
    sentence = sentence.split(" ")

    overall = []
    for word in sentence:
        score = 0

        for letter in word:
            score = score + letters.index(letter) + 1 
        overall.append(score)

    highest_index = overall.index(max(overall))
    print(overall)

    return sentence[highest_index]

    # return the word that appears earliest in the original string.
    # it didn't mean the word appears the ealiest in dictionary order, but the word that appears the earliest in the original string.
    # ha....

    # if overall.count(max(overall)) == 1:
    #     return sentence[highest_index]

    # else:  # > 1
    #     words = []  # list of words with the highest score
    #     for i in range(len(sentence)):
    #         if overall[i] == max(overall):
    #             words.append(sentence[i])

        
    #     first_letter_score =[] 
    #     for word in words: 
    #         first_letter_score.append(letters.index(word[0]))

    #     final_word = words[first_letter_score.index(min(first_letter_score))] # min location is the earliest location
    #     return final_word



for i in string.ascii_lowercase:
    letters.append(i)


# print(high('man i need a taxi up to ubud'))  # 'taxi')
# print(high('what time are we climbing up the volcano')) # 'volcano')
# print(high('take me to semynak'))   # 'semynak')
# print(high('aa b')) # 'aa')
# print(high('b aa')) # 'b')
# print(high('bb d')) # 'bb')
# print(high('d bb')) # 'd')
# print(high("aaa b"))    # "aaa")



# [96, 104, 70, 93, 104]
# 'hmynest' should equal 'trsvax'
print(high('hmynest trsvax')) 

# [112, 118, 68, 130, 50, 113, 79, 83, 44, 77, 81, 79, 130, 70, 68, 50, 48, 54, 106, 115, 41, 67, 121, 98]
# 'osoqoqms' should equal 'kizvghxqf'
print(high('osoqoqms kizvghxqf'))


# [132, 49, 161, 140, 60, 36, 59, 46, 149, 53, 63, 121, 99, 92, 100, 75, 76, 57, 161, 113, 75, 85, 119]
# 'iezncztrqw' should equal 'prwpenplpy'
print(high('iezncztrqw prwpenplpy'))

# [68, 118, 22, 61, 61, 76, 91, 78, 110, 114, 94, 118, 110, 33, 48, 15, 48, 38, 62, 75]
# 'pznzeghp' should equal 'dumwzvi'
print(high('pznzeghp dumwzvi'))

print(high('vdtb bvbrhhuja ccbw vinhh okgxufvcyn xkz edkqs gtxlqcwiv njcda bfmkoh kmne vbpc lxwh rjwegoz gxewdfre ijne rqprezsg vjtmluwir cafgie iebzafwax'))
# [48, 92, 31, 61, 148, 61, 56, 137, 32, 55, 43, 43, 67, 104, 92, 38, 126, 148, 31, 97]
# 'vjtmluwir' should equal 'okgxufvcyn'
print(high('vjtmluwir okgxufvcyn'))





# not the version of summation score of each letter in each word
# this is the version of finding the max score of each letter in each word
'''
def high(sentence):
    sentence = sentence.split(" ")

    overall = []

    for word in sentence:
        score = []

        for letter in word:
            score.append(letters.index(letter) + 1)

        overall.append(max(score))

    highest_index = overall.index(max(overall))
    print(overall)

    if overall.count(max(overall)) == 1:
        return sentence[highest_index]

    else:  # > 1
        words = []  # list of words with the highest score
        for i in range(len(sentence)):
            if overall[i] == max(overall):
                words.append(sentence[i])
                sentence.pop(i)
        
        location =[] # list of the location info of the highest score letter in each word
        for word in words:

            score = []
            for letter in word:
                score.append(letters.index(letter) + 1)
            
            location.append(score.index(max(score)))  
        final_word = words[location.index(min(location))] # min location is the earliest location
        return final_word
'''
'''
Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

Assumptions:
A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
Matches should be case-insensitive, and the words in the result should be lowercased.
Ties may be broken arbitrarily.
If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.
Examples:
top_3_words("In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.")
# => ["a", "of", "on"]

top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# => ["e", "ddd", "aa"]

top_3_words("  //wont won't won't")
# => ["won't", "wont"]
Bonus points (not really, but just for fun):
Avoid creating an array whose memory footprint is roughly as big as the input text.
Avoid sorting the entire array of unique words.
'''

# count -> find max 3
# ord(97~122), chr(97~122)
# ' = chr(39)

global a_z
global a_z_plus
a_z = []
for i in range(97, 123):
    a_z.append(chr(i))
a_z_plus = a_z + ['\'']

def top_3_words(text):
    text = text.lower()

    for letter in text:
        if letter not in a_z_plus:
            text = text.replace(letter, ' ')  # aa.a => aa a
    
    text = text.split()
    each_text = list(set(text)) # deleting same words for saving only one each word
    for word in each_text:
        a = set(word) & set(a_z)
        if bool(a) == False:
            each_text.remove(word)
    # for i in range(len(each_text)):  # to remove an element that includes only '
    #     if each_text[i] not in a_z:
    #         each_text.remove(each_text[i])
    text_count = []

    for word in each_text:
        text_count.append(text.count(word))
    
    #mose frequetly used three words
    most_3 = []
    if text_count:
        count_index = text_count.index(max(text_count)) #index of most frequently used word
        most_3.append(each_text[count_index]) 
        text_count[count_index] = 0

        for i in range(2): # in the case that there are less than 3 words
            if max(text_count) != 0 and len(text_count) != 1: # in the case that there is only one word
                count_index = text_count.index(max(text_count))
                most_3.append(each_text[count_index]) 
                text_count[count_index] = 0

    return most_3


print(top_3_words("a a a  b  c c  d d d d  e e e e e")) # ["e", "d", "a"])
print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")) # ["e", "ddd", "aa"])
print(top_3_words("  //wont won't won't ")) # ["won't", "wont"])
print(top_3_words("  , e   .. "))   # ["e"])
print(top_3_words("  ...  "))   # [])
print(top_3_words("  '  ")) # [])
print(top_3_words("  '''  "))   # [])
print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
        mind, there lived not long since one of those gentlemen that keep a lance
        in the lance-rack, an old buckler, a lean hack, and a greyhound for
        coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
        on Sundays, made away with three-quarters of his income.""")) # ["a", "of", "on"])






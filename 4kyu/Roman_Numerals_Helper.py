'''
Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API demonstrated in the examples below. 
Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. 
In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 
2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

Examples
RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
'''

import roman


class RomanNumerals:


    def to_roman(val):
        return roman.toRoman(val)

    def from_roman(roman_num):
        return roman.fromRoman(roman_num)




print(RomanNumerals.to_roman(1000)) # 'M', '1000 should == "M"')
print(RomanNumerals.to_roman(4))    # 'IV', '4 should == "IV"')
print(RomanNumerals.to_roman(1))    # 'I', '1 should == "I"')
print(RomanNumerals.to_roman(1990)) # 'MCMXC', '1990 should == "MCMXC"')
print(RomanNumerals.to_roman(2008)) # 'MMVIII', '2008 should == "MMVIII"')

print(RomanNumerals.from_roman('XXI'))  # 21, 'XXI should == 21')
print(RomanNumerals.from_roman('I'))    # 1, 'I should == 1')
print(RomanNumerals.from_roman('IV'))   # 4, 'IV should == 4')
print(RomanNumerals.from_roman('MMVIII'))   # 2008, 'MMVIII should == 2008')
print(RomanNumerals.from_roman('MDCLXVI'))  # 1666, 'MDCLXVI should == 1666')


# import roman

# class RomanNumerals:

#     def to_roman(val):
#         return roman.toRoman(val)

#     def from_roman(roman_num):
#         return roman.fromRoman(roman_num)



# 1	I
# 2	II
# 3	III
# 4	IV
# 5	V
# 6	VI
# 7	VII
# 8	VIII
# 9	IX
# 10	X
# 11	XI
# 12	XII
# 13	XIII
# 14	XIV
# 15	XV
# 16	XVI
# 17	XVII
# 18	XVIII
# 19	XIX
# 20	XX
# 21	XXI
# 22	XXII
# 23	XXIII
# 24	XXIV
# 30	XXX
# 40	XL
# 50	L
# 60	LX
# 70	LXX
# 80	LXXX
# 90	XC
# 100	C
# 101	CI
# 102	CII
# 200	CC
# 300	CCC
# 400	CD
# 500	D
# 600	DC
# 700	DCC
# 800	DCCC
# 900	CM
# 1,000	M
# 1,001	MI
# 1,002	MII
# 1,003	MIII
# 1,900	MCM
# 2,000	MM
# 2,001	MMI
# 2,002	MMII
# 2,100	MMC
# 3,000	MMM
# 4,000	MMMMor M V
# 5,000	V
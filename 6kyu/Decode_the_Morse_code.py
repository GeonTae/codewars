"""
In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice and digital data communication channels, it still has its use in some applications around the world.
The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the code A is coded as ·−, code Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital codes are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

In addition to codes, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···. These special codes are treated as single special characters, and usually are transmitted as separate words.

Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

For example:

decode_morse('.... . -.--   .--- ..- -.. .')
#should return "HEY JUDE"
"""


def morse_code(code):
    if code == '.-':
        return 'A'
    elif code == '-...':
        return 'B'
    elif code == '-.-.':
        return 'C'
    elif code == '-..':
        return 'D'
    elif code == '.':
        return 'E'
    elif code == '..-.':
        return 'F'
    elif code == '--.':
        return 'G'
    elif code == '....':
        return 'H'
    elif code == '..':
        return 'I'
    elif code == '.---':
        return 'J'
    elif code == '-.-':
        return 'K'
    elif code == '.-..':
        return 'L'
    elif code == '--':
        return 'M'
    elif code == '-.':
        return 'N'
    elif code == '---':
        return 'O'
    elif code == '.--.':
        return 'P'
    elif code == '--.-':
        return 'Q'
    elif code == '.-.':
        return 'R'
    elif code == '...':
        return 'S'
    elif code == '-':
        return 'T'
    elif code == '..-':
        return 'U'
    elif code == '...-':
        return 'V'
    elif code == '.--':
        return 'W'
    elif code == '-..-':
        return 'X'
    elif code == '-.--':
        return 'Y'
    elif code == '--..':
        return 'Z'
    elif code == '-----':
        return '0'
    elif code == '.----':
        return '1'
    elif code == '..---':
        return '2'
    elif code == '...--':
        return '3'
    elif code == '....-':
        return '4'
    elif code == '.....':
        return '5'
    elif code == '-....':
        return '6'
    elif code == '--...':
        return '7'
    elif code == '---..':
        return '8'
    elif code == '----.':
        return '9'
    elif code == '.-.-.-':
        return '.'
    elif code == '--..--':
        return ','
    elif code == '..--..':
        return '?'
    elif code == '.----.':
        return '\''
    elif code == '-.-.--':
        return '!'

def decode_morse(morsecode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    for i in range(len(morsecode)): # delete extra spaces at the beginning and at the end of the string
        # morsecode = morsecode.strip()
        if morsecode.startswith(' '):
            morsecode = morsecode[1:]
        if morsecode.endswith(' '):
            morsecode = morsecode[:-1]
    
    for i in range(len(morsecode)): # replace 3 spaces with 2 spaces 
        if '   ' in morsecode:
            morsecode = morsecode.replace('   ', '  ')  

    # if '  ' in morsecode:
    #     morsecode = morsecode.replace('  ', ' ')

    morsecode = morsecode.split(' ') #['....', '.', '-.--', '', '.---', '..-', '-..', '.']
    decode = ''
  
    for code in morsecode: #decode the morse code

        if code == '...---...':  # Titanic special code
            decode = decode + 'SOS'

        elif code == '':
            decode = decode + str(' ')

        else:
            decode = decode + morse_code(code)

    return decode


print(decode_morse('.... . -.--   .--- ..- -.. .')) #HEY JUDE
print(decode_morse('...---...'))  # SOS special code

print(decode_morse(' . '))
print(decode_morse(' .  . '))


print(decode_morse('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   \
    -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   \
    - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '))
#'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')



# string = ' . '
# string2 = '  . .  '
# if string.startswith(' '):
#     string = string[1:-1]
# print(string)



# string = '     k      k       k'
# print(string.replace('   ', '  '))

# string = '  k  k'   
# print(string.split(' '))

'''
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. 
Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
'''


def rgb(r, g, b):
    if r > 255:
        r = 255
    if g > 255:
        g = 255
    if b > 255:
        b = 255
    if r < 0:
        r = 0
    if g < 0:
        g = 0
    if b < 0:
        b = 0
    return "{:02x}{:02x}{:02x}".format(r, g, b).upper() 




print(rgb(0,0,0)) #"000000", "testing zero values")
print(rgb(1,2,3))   #"010203", "testing near zero values")
print(rgb(255,255,255)) # "FFFFFF", "testing max values")
print(rgb(254,253,252)) # "FEFDFC", "testing near max values")
print(rgb(-20,275,125)) # "00FF7D", "testing out of range values")


'''
    a=r%16
    b=int(r/16)
    val2=str(l[a])
    val1=str(l[b])
    fin1=val1+val2
    a=g%16
    b=int(g/16)
    val2=str(l[a])
    val1=str(l[b])
    fin2=val1+val2
    a=bl%16
    b=int(bl/16)
    val2=str(l[a])
    val1=str(l[b])
    fin3=val1+val2
    return fin1+fin2+fin3
'''
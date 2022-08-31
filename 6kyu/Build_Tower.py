'''
Build a pyramid-shaped tower given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
'''

def tower_builder(n_floors):
    tower = []
    for i in range(n_floors):
        stars_num = ((i+1)*2-1)
        space_num = int((n_floors*2 - 1 - stars_num)/2)
        line = " "*space_num + "*"*stars_num + " "*space_num 
        tower.append(line)
    return tower



print(tower_builder(1)) # ['*', ])
print(tower_builder(2)) #  [' * ', '***'])
print(tower_builder(3)) # ['  *  ', ' *** ', '*****'])

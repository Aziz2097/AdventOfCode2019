import math

input_file = open('input','r')

def calc_fuel(mass):
    result = math.floor(( mass / 3 )) - 2
    if result > 0:
        return result
    else: 
        return 0

data = []
for i in input_file.readlines():
    data.append( int( i.strip('\n') ) )

# Part 1
part1 = 0 
for i in data:
    part1 += calc_fuel(int(i))


print("Part1: {0}".format(part1))

part2 = 0
# Part 2
for i in data:
    subtotal = calc_fuel(i) 
    part2 += subtotal 
    while( subtotal > 0 ):
        subtotal = calc_fuel(subtotal) 
        part2 += subtotal 
    
print("Part2: {0}".format(part2)) 

    



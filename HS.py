import operator

HS_dict = {}

with open("HS.txt") as f:
    for line in f:
        (key, val) = line.split("|")
        HS_dict[(key)] = int(val.rstrip('\n'))

print(HS_dict)

sorted_HS = sorted(HS_dict.items(), key=operator.itemgetter(-1))

print(sorted_HS)
    
x = 0
y = 0
spaces = ' '


# spaces_20 = spaces * 20
spaces_40 = spaces * 40
print(spaces_40)

# length_of_key = int(len(key))
# length_of_val = int(len(val))
# number_of_spaces = 50 - length_of_key - length_of_val
# print(number_of_spaces)

# trailing_spaces = int(number_of_spaces) * spaces
# print(trailing_spaces)

print(sorted_HS)
print('                    ', "Hall of Fame")
print('Name', '                                        ', ' Score')

for key, val in sorted_HS:
    length_of_key = len(key)
    # print(length_of_key)
    val_str = str(val)
    length_of_val = len(val_str)
    number_of_spaces = 50 - length_of_key - length_of_val
    trailing_spaces = int(number_of_spaces) * spaces
    print(key, trailing_spaces, val)
    # print(val, spaces_40, key)

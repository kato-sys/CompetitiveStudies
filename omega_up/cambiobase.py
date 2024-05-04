og_num = input("Enter a number: ")
og_base = int(input("Enter original base: "))
new_base = int(input("Enter new base: "))

# Create a symbol-to-value table.
STR2INT = {'0': 0,
           '1': 1,
           '2': 2,
           '3': 3,
           '4': 4,
           '5': 5,
           '6': 6,
           '7': 7,
           '8': 8,
           '9': 9,
           'A': 10,
           'B': 11,
           'C': 12,
           'D': 13,
           'E': 14,
           'F': 15,
           'a': 10,
           'b': 11,
           'c': 12,
           'd': 13,
           'e': 14,
           'f': 15, }

og_num_int = 0
for character in og_num:
    num_int = STR2INT[character]
    og_num_int *= og_base
    og_num_int += num_int

INT2STR = dict(map(reversed, STR2INT.items()))

new_num = ''
while og_num_int:
    value = divmod(og_num_int, new_base)
    new_num += (INT2STR[value[1]])
    og_num_int = value[0]

print(''.join(reversed(new_num)))

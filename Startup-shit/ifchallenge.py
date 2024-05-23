#if challenge
#for challenge
# parrot = 'Norwegian Blue'
# for character in parrot:
#     print(character)
    
# number = "9,223;372:036 854,775;807"
# separators = ""

# for char in number: 
#     if not char.isnumeric():
#         separators = separators + char

# print(separators)

# values = "".join(char if char not in separators else " " for char in number).split()
# print([int(val) for val in values])

# for i in range(1,20):
#     print("i is now{}".format(i))
# for i in range(0,10,2):
#     print("i is now{}".format(i))

for i in range(1,13):
    for j in range(1,11):
        print("{0} times {1} is {2}".format(i,j,i*j))
        
        
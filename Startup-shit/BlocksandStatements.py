# for i in range(1,14):
#     print("Person:{0},Someone:{1},Something:{2}".format('Kid','Brother','Bike'))
#     print("No. {} Square is {} Cube is {:4}".format(i,i**2,i**3))
    
name = input('What is your name?')
age = int(input('How old are you,{}?'.format(name)))
# print(name, age)
if age>=18:
    print('You are an adult')
elif age<18 and age>0:
    print('You are a child')
else:
    print('You are negative')
    
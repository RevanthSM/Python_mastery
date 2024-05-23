available_parts = ["computer",
                   "monitor",
                   "Keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi cable",
                   "Dvd drive"]
current_choice = "-"
computer_parts = []
while current_choice != '0':
    if current_choice in "12345":
        print("Adding {}".format(current_choice))
    else:
        print("Please add options from the list below:\n1.Computer\n2.Monitor\n3.Keyboard\n4.Mouse\n5.Mouse Mat\n0.Exit")
    
    current_choice = input()

for part in available_parts:
    print("{0}: {1}".format(available_parts.index(part)+1,part))

#Enumerate function
for number, part in enumerate(available_parts):
    print("{0}: {1}".format(number+ 1,part))

for index,alpha in enumerate("abcdefgh"):
    print(index,alpha)
    

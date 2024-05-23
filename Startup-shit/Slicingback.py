backwards_alpha = 'abcdefghijklmnopqrstuvwxyz'

back = backwards_alpha[25::-1]
print(back)
print(backwards_alpha[:-9:-1]) # zyxwvts - [25::-1]
print(backwards_alpha[4::-1]) #edcba - backwards_alpha[4::-1]
print(backwards_alpha[-10:-13:-1]) #qpo - [16:13:-1]

list = ['back',2,'hey']

print(list)
days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])
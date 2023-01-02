import random
num1 = random.randrange(0, 10)
num2 = random.randrange(0, 10)
num3 = random.randrange(0, 10)
num4 = random.randrange(0, 10)
num5 = random.randrange(0, 10)
num6 = random.randrange(0, 10)
num7 = random.randrange(0, 10)
num8 = random.randrange(0, 10)
num9 = random.randrange(0, 10)
num10 = random.randrange(0, 10)
num11 = random.randrange(0, 10)

card = (f"{num1}{num2}{num3}{num4}{num5}{num6}{num7}{num8}{num9}{num10}{num11}")
amount = random.randrange(100, 1000, 100)
code = '*555*'
complete = (code + card + '#')
recharge = ''
print(f"""Pin: {card}
Code: {code} 
example: {code}pin#
proudly sponsored by 'Anadu'""")
while recharge != complete:
    i = 0
    while i < 5:
        i += 1
        recharge = input(f"Enter Your recharge pin here use {code}pin#: ")
        if recharge == complete:
            print(f"your rechage of {amount} naira was sucessful")
            break
        else:
            print('Recharge unsucessful!')

        print(f"You only have 5 trials '{5 - i}' remaining")

    else:
        print("Sorry your line has been suspended for 5s")
        break

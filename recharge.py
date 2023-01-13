import random

card = (f"{random.randrange(100_000_000_00)}")
amount =(f"{ random.randrange(100, 10_000, 100)}")
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
            print(f"your recharge of {amount} naira was successful")
            break
        else:
            print('Recharge unsuccessful!')

        print(f"You only have 5 trials '{5 - i}' remaining")

    else:
        print("Sorry your line has been suspended for an invalid action")
        break
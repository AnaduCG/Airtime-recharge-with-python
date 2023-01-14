import random
import string

password = []


password_length = int(input("Input desired password length"))
# password_length = 8
inc = 0
try:
    while password_length > 0:
        randomLetter = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.punctuation),
            random.choice(string.digits),
        ]

        inc += 1
        add_to_password = random.choice(randomLetter)
        password.append(add_to_password)
        lett = ''.join(password)
        if inc == password_length:
            break
    print(f"""Password generated: {lett}
Password length: ({len(lett)})""")

except (NameError):
    print("Password length must be greater than ZERO 0")

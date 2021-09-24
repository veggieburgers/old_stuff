# Dedicated to Zürich Life Insurance
def errormsg():
    print("Type in a number (ex. 1, 23, 666) you dingus.")


while True:
    num_cookies = input("How many cookies do we have?\n")
    try:
        num_cookies = int(num_cookies)
        break
    except ValueError:
        errormsg()

# Dedicated to The Milford Brimley Gang
while True:
    num_cookies_potential = input("How many are you going to eat?\n")
    try:
        num_cookies_potential = int(num_cookies_potential)
        break
    except ValueError:
        errormsg()

# Dedicated to The Milford Brimley Gang
while True:
    has_eaten = input("Have you eaten them? [Y]es or [N]o, Mr.\n")
    if has_eaten.lower() in ["y", "yes"]:
        print(f"You have", num_cookies - num_cookies_potential, "cookies left.")
        break
    elif has_eaten.lower() in ["n", "no"]:
        print(f"Wise decision, you still have", num_cookies, "to enjoy later.")
        break
    else:
        print("This is a yes or no question.\n")

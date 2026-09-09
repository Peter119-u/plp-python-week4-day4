age = int(input("Enter your age: "))

if age < 18:
    consent = input("Do you have parental consent? (yes/no): ").strip().lower()

    # A person under 13 is not eligible, even if they have consent
    if age < 13 or not consent == "yes":
        print("Sorry, you are not eligible yet.")
    # A person aged 13 to 17 is eligible only with parental consent
    elif age >= 13 and consent == "yes":
        print("Welcome to the club!")
else:
    # Anyone 18 or older is eligible without parental consent
    if age >= 18 and not age < 18:
        print("Welcome to the club!")

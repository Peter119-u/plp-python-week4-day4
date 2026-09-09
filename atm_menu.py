balance = 1000
correct_pin = "1234"

pin = input("Enter your 4-digit PIN: ")

# Check whether the PIN entered by the user is correct
if pin != correct_pin:
    print("Incorrect PIN")
else:
    # The PIN is correct, so ask for the withdrawal amount
    amount = float(input("Enter amount to withdraw: "))

    # Check whether the requested amount is within the available balance
    if amount <= balance:
        balance = balance - amount
        print(f"Withdrawal successful. New balance: {balance:.2f}")
    else:
        print("Insufficient funds")

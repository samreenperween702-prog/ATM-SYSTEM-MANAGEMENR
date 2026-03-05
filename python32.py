# ATM MANAGEMENT SYSTEM
print("------welcome to ATM------")
balance=10000
pin="12345"

entered_pin=input("entrered your pin:")
if entered_pin!=pin:
    print("wrong pin")

else:
    while True:
        print("\n----ATM menu-----")
        print("1. check balance")
        print("2. Deposit money")
        print("3. withdraw money")
        print("4. changing pin")
        print("5. Exit")

        choice=input("enter choice:")

        if choice=="1":
            print("your balance is:",balance)
            
        elif choice=="2":
            amount=int(input("enter deposit automatically"))

            balance+=amount
            print("money deposited successfully.")

        elif choice=="3":
            amount=int(input("enter withdraw amount."))
            if amount<=balance:
                print("please collect your cash.")
            else:
                print("insufficient balance")

        elif choice=="4":
            new_pin=int(input("enter new pin"))
            pin==new_pin
            print("pin changing successfully." )

        elif choice=="5":
            print("thank you for using ATM")
            break
        else:
            print("invalid choice,try again.")
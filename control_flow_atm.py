#!/usr/bin/python3

#creating variables
balance = 10000
pin = 2030

attempts = 0
number_of_attempts_allowed = 3


#prompting the user to input their pin
while attempts < number_of_attempts_allowed:
    user_pin = int(input("please enter your pin: "))
    if user_pin == pin:
        print("access granted. welcome to the main menu")
        break
    else:
        attempts += 1
        if attempts == number_of_attempts_allowed:
            print("too many incorrect attempts. Access blocked.")
            exit()
        

total_deposits = 0
total_withdrawals = 0

#using the while true loop to display the main menu options
while True:
    print("\nMain Menu: ")
    print("\n 1. Check Balance", "\n 2. Deposit Funds", "\n 3. withdraw Funds", "\n 4. Change Pin", "\n 5. Exit")
    

#using the if-elif and else statements for checking balance, depositing funds, withdrawing funds, changing pin, and exiting the program.
    
    option = int(input("choose options (1-5): "))
    if option == 1:
        print(f" you have ${balance} left")
    elif option == 2:
        deposited_fund = float(input("Input deposit amount: "))
        if deposited_fund > 0:
          balance += deposited_fund
          total_deposits += deposited_fund
          print(f"you have deposited ${deposited_fund}. Your new balance is: ${balance}")
        else:
          print("please enter a positive number.")

    elif option == 3:
         amount_withdrawn = float(input("input amount to withdraw: "))
         if amount_withdrawn > 0:
             if amount_withdrawn <= balance:
                 balance -= amount_withdrawn
                 total_withdrawals += amount_withdrawn
                 print(f"you have withdrawn $ {amount_withdrawn}. new balance is: ${balance}")
             else:
                 print("insufficient funds.")
         else:
             print("please enter a positive number.")

    elif option == 4:
        current_pin = int(input("enter your current_pin: "))
        if current_pin == pin:
            while True:
                new_pin = int(input("enter your new four digit pin: "))
                if 1001 <= new_pin <= 9001:
                    comfirm_pin = int(input("confirm your new pin: "))
                    if new_pin == comfirm_pin:
                        pin = new_pin
                        print("your pin has been changed successfully.")
                        break
                    else:
                        print("pin do not match. please try again.")
                else:
                    print("new pin must be a four digit integer. ")
                

    elif option == 5:
        print("Thank you for using ATM.")
        print(f"total withdrawal is: ${total_withdrawals} and total deposit made is: $ {total_deposits} \n total amount left is: {balance}")
        break
    else:
        print("invalid option. please try again.")





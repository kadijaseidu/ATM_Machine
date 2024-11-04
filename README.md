# ATM Machine


## Authors
* [Khadija Seidu](https://github.com/kadijaseidu)
* [Talatu Nyande](https://github.com/talatunyande)

## Project Overview

This repository contains an interactive command-line project:

1. **ATM Machine**: A simple ATM simulator that allows users to; 
* Check balance: This displays the current account balance of the user.
* Depositing funds: It allows users to deposit money into their account and displays the total 
  amount of money in thier acount.
* Withdrawing funds: It allows users to withdraw money from their account, based on the availability
  of their balance, and it displays the amount of money withdrawn from the account and the balance left.
* Changing PIN: It enables users to change their PIN to ensure security. It first requests the user to input
   their current pin and then request the user to input their new pin. The user is then asked to confirm the
   new pin after which a message is displayed informing the user that the pin has been successfully changed.
* Exit: When the user is done with their transaction, they can then select the 'exit' option to leave the page.
 
 **Key Features**
* User authentication: Before a user can use the ATM machine, they are required to provide a pin to access the account.
* Error handling: It handles invalid inputs, insufficient funds, and incorrect pin attempts by prompting the user to make
   the right choice.
* User-friendly interface: It provides a simple and easy to navigate interface.
* Data validation: It ensures that user input is valid and appropriate.
* Security measures: It executes basic security measures like PIN verification.

## How to Use This Repository

* Clone this repository inside your local machine, inputting;
   - git clone https://github.com/kadijaseidu/ATM_Machine.git
* Navigate to the directory where you cloned it.
* Run the provided python scripts in your terminal.
* Follow the prompts in each script to interract with the programs.

## Project Structure

* control_flow_atm.py: This python script contains the ATM Machine Simulation, including user authentification, menu navigation, 
  transaction processing, and error handling.
   - The program starts by initializing two important variables, 'balance' and 'pin'. the variable balance is set to 10000, which represents the initial amount in the user's account, whereas the variable 'pin' is set to 2030, representing the default pin for the user.
   - The program then enters a loop that allows the user to enter their pin. The user has three attempts to enter the correct pin, if the pin matches the default pin, the loop breaks, and the user is given access to the account. If the pin is not correct, the program then increase the attempt counter by one and informs the user, and if the user still fails to enter the correct pin after three attempts, a message is displayed indicating that the user's access to the account is blocked and exits the program.
   - The program then presents a main menu with five options: 1. check balance, 2. deposit funds, 3. withdraw funds, 4. change pin, 5. exit. 'while True' loop is used to create an infinite loop for the main menu. this enables the user to be able to keep having access to the 'main menu' options until they enter the 'exit' option to break the loop.
   - 'If-Elif-Else statements is used to allow the program to make decisions based on the user's input. it ensures that the user entered the right option, if not it displays an error message. If the user selects the first option, it displays the current balance.
   - For the second option, the user is asked to enter an amount to deposit, the program then checks if the amount is positive before it adds it to the balance and display the new balance, and if the amount is not positive, it prompts the user to enter a valid amount.
   - For the third option, if the user chooses to withdraw funds, the program prompts for the withdrawal amount, check if it is positive and if there is sufficient funds in the account, if both conditions are met, the amount is deducted from the balance and the new balance is displaced. If there's no sufficient funds, a message is displayed to the user.
   - For the fourth option, it enables the user to change their pin. The user is first asked to enter their current pin, if it matches, they can then go ahead to enter a new four digit pin, the program check if the new pin is valid and then prompt the user to comfirm the new pin. Incase the new pin and the comfirmed pin matches, the new pin is updated, else the program displays a message indicating that the pin is invalid.
   - For the fifth option, once the user selects the 'exit' option, the program displays a 'Thank you for using ATM' message and terminates. And incase the user enters an option that is not part of the provided options, the program informs them and prompts for a valid selection again.

* README.md: This file provides a brief overview of the project, instructions on how to run the program, and any additional documentation or notes.

## Learning Objectives

 This project will enable you to be able to;
 * learn how to implement secure user authentification methods, such as pin verification.
 * Gain experience in managing the user's account data, which includes balance tracking and transaction history.
 * Develop skills in creating user-friendly interface for easy navigation.
 * Learn how to implement error handling to manage incorrect inputs and system failures accurately.
 * Understand the logic behind processing different types of transactions, such as withdrawals, deposits, and balance inquiries.
 * familialize yourself with using Git for version control, including branching and merging changes in the project.
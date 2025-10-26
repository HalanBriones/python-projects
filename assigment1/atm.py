def main():
    #Tuple with accounts informations
    '''Atributes of the accounts
    name , last name, account number, password, balance, list transactions of withdraw, list transactions of deposits'''
    accounts = (
        ['John', 'Doe', '45678','jo123', 100000,[],[]],
        ['Jane', 'Smith', '12345','ja123',200000,[],[]],
        ['Halan', 'Briones', '34567','halanbm98',50000,[],[]],
        ['Grace', 'Vanee', '12346','gv123',20000,[],[]]
    )
    #Initial message
    print("*"*30)
    print("Welcome Data Bank".center(30))
    print("*" * 30)
    list_accounts = list(accounts) #tuple transform to list
    flag = 1 #initiate the flag
    transactions_withdraw = []  # list to save transactions withdraw
    transactions_deposit = []  # list to save transactions deposit
    while flag != 0: #While to ask account number until one is founded or they try max 3 times
        account_num = input(f"Attempt N° {flag} Enter account number: ")
        flag+=1 #count the attempts to enter the account number
        for i in range(len(list_accounts)):
            if flag >= 4: #Max 3 attempts to enter account number
                print("You have exceeded the amount of attempts")
                flag = 0  # finish the first loop while to finish the program
                break
            elif account_num == list_accounts[i][2]:
                #The account was founded
                while True: #While to ask for password until it matches
                    account_pass = input("Enter password: ")
                    if account_pass == list_accounts[i][3]:
                        #The password did matched
                        print("*"*30)
                        print(("Welcome "+list_accounts[i][0]).center(30))
                        print("*"*30)
                        while True:#while with the option menu
                            option = input("[1]-Withdraw\t[2]-Deposit\n[3]-Balance\t\t[4]-Transactions\n \t\t [5]-Quit \n")
                            if option == "1":
                                print("*"*12+"Withdraw"+"*"*11)
                                while True:
                                    withdraw_value = input("Enter integer ammount to withdraw: ")
                                    if withdraw_value.isdigit(): ##Validating the string has numbers >0
                                        int_withdraw_value = int(withdraw_value) #transforming to integer
                                        if int_withdraw_value==0: #Making sure that is not 0
                                            print("Please enter a number that is greater than 0")
                                            continue
                                        else:
                                            if int_withdraw_value>list_accounts[i][4]: #Making sure the acount have enough balance to do the withdraw
                                                print("Insufficient balance please try again")
                                                print( f" Account Number \t Previous Balance \t Withdraw Amount \t Remain Balance \n {list_accounts[i][2]} \t\t\t\t {list_accounts[i][4]} \t\t\t\t {int_withdraw_value} \t\t\t\t {list_accounts[i][4]}")
                                            else:
                                                list_accounts[i][4] = list_accounts[i][4]-int_withdraw_value #updating balance
                                                print(f" Account Number \t Previous Balance \t Withdraw Amount \t Remain Balance \n {list_accounts[i][2]} \t\t\t\t {list_accounts[i][4]+int_withdraw_value} \t\t\t\t {int_withdraw_value} \t\t\t\t {list_accounts[i][4]}")
                                                transactions_withdraw.append(int_withdraw_value)#inserting the withdraw's to transaction withdraw list
                                            break
                                    else:
                                        print("Please enter integer values")
                                        continue
                            elif option=="2":
                                print("*"*12+"Deposit"+"*"*11)
                                while True:
                                    deposit_value = input("Enter amount to Deposit: ")
                                    if deposit_value.isdigit(): #Validating the string has numbers >0
                                        int_deposit_value=int(deposit_value) #transforming to integer
                                        if int_deposit_value==0: #Making sure that is not 0
                                            print("Please enter a number that is greater than 0")
                                            continue
                                        else:
                                            list_accounts[i][4] += int_deposit_value # updating balance
                                            print(f" Account Number \t Previous Balance \t Deposit Amount \t Remain Balance \n {list_accounts[i][2]} \t\t\t\t {list_accounts[i][4]-int_deposit_value} \t\t\t\t {int_deposit_value} \t\t\t\t {list_accounts[i][4]}")
                                            transactions_deposit.append(int_deposit_value) #inserting the deposit's to transaction deposit list
                                            break
                                    else:
                                        print("Please enter integer values")
                                        continue
                            elif option=="3":
                                print("*"*12+"Balance"+"*"*11)
                                print(f"Account number \t Current balance\n \t{list_accounts[i][2]} \t\t {str(list_accounts[i][4])}") #printing the updated balance
                            elif option=="4":
                                print("*" * 30)
                                if not transactions_withdraw: #Check if is there transactions in the session
                                    print("There is no withdraw transactions")
                                else:
                                    #Printing list with  withdraws transactions
                                    print("Account Number   Transaction     Withdraw")
                                    for y in range(len(transactions_withdraw)):
                                        print(f"{list_accounts[i][2]} \t\t\t  {str(y)}  \t\t\t  {str(transactions_withdraw[y])}")
                                if not transactions_deposit: #Check if is there transactions in the session
                                    print("There is no deposits transactions")
                                else:
                                    #Printing list with  deposit transactions
                                    print("Account Number  Transaction     Deposit")
                                    for p in range(len(transactions_deposit)):
                                        print(f"{list_accounts[i][2]} \t\t\t  {str(p)} \t\t\t  {str(transactions_deposit[p])}")
                            elif option=="5":
                                print("Bye "+ list_accounts[i][0])
                                list_accounts[i][5].append(transactions_withdraw)  # add transactions of withdraws to the list of accounts to keep register of all the transactions
                                list_accounts[i][6].append(transactions_deposit)  # add transaction of deposit to the list of accounts to keep a register of transaccions
                                break
                            print("*" * 30)
                        flag=0
                    else:
                        print("Incorrect Password Try Again")
                        continue
                    break

    accounts = tuple(list_accounts) #go back to tuple
if __name__=="__main__":
    main()
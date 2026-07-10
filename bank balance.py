Balance_amount=int(input("enter your balance amount:"))
withdrwal_amount=int(input("enter your withdrwal amount:"))
if(Balance_amount<withdrwal_amount<0):
    print("sufficient balance is not there","invalid amount")
else:    
    print("withdrwal succesful")
    remaining_balance=(Balance_amount-withdrwal_amount)
    print(remaining_balance)

def withdrawal(amount,balance):
    balance = balance-amount
    return balance

def deposit(amount,balance):
    balance=balance+amount
    return balance


while True:
    print("\t\t1:Input a new transaction log")
    print("\t\t2:Exit")
    ch=int(input("Enter your choice:"))
    if(ch==2):
        print("End of program")
        quit()
        break
    elif (ch==1):
        balance=0
        list1=[]
        print("Enter the transaction log of user:")
        while True:
            data=input()
            if(data==""):
                break
            list1.append(data.split())
        for transaction in list1:
            if(transaction[0]=='W'):
                if(balance<int(transaction[1])):
                    print(" Transaction Declined : Insufficient balance",(transaction[0],int(transaction[1])))
                else:
                    balance=withdrawal(int(transaction[1]),balance)
                    print("Successful Transaction",(transaction[0],int(transaction[1])))
            elif(transaction[0]=='D'):
                balance=deposit(int(transaction[1]),balance)
                print("successful Transaction",(transaction[0],int(transaction[1])))

        print("\nTotal balance in the account :Rs ",balance)
    else:
        print("wrong choice entered !: Try again")


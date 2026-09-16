""" FUCALTY OF COMPUTING ,ENGINERING AND TECHNOLOGY
DEPARTMENT OF COMPUTING IN STRUCTURED PROGRAMMING
MUNIALO DAVID BARDLEY B39929
 FOR THE ACCOUNT TYPE SELECTED
    20/U/2019/PSYCH/00001
    CITY LINK MINIBANK
    2024
"""
n=int(input("How many customers are u working on)? "))
accounts_opened = 0
total_deposit = 0

for i in range(1,n+1):
    print(f"Client {i}:")
    name=input("Name:")
    age=int(input("Age:"))
    accounttype=input("Account type(S/C/T):")
    initial_deposit=int(input(" initial deposit "))

# THIS ASSIGNMENT TESTS  A SIMPLE PROGRAM THAT PROCESSES  SEVERAL CUSTOMERS' ACCOUNTS 
    if accounttype=="S" and initial_deposit < 50000:
        print("Deposit too low.Minimum for savings is 50,000 UGX")
    elif accounttype=="C" and initial_deposit < 100000:   
        print("Deposit too low.Minimum for current is 100,000 UGX")
    elif accounttype=="T" and initial_deposit < 20000:
        print("Deposit too low.Minimum for time deposit is 20,000 UGX")
    elif accounttype=="T" and age > 25:
        print("Time deposit is only for people below 25 years")
    else:
        print(f"Account created successfully for {name}")
        print(f"Balance:{initial_deposit} UGX")
        accounts_opened += 1
        total_deposit += initial_deposit

print("Session Summary:")
print(f"Total accounts opened: {accounts_opened}")
print(f"Total deposits: {total_deposit} UGX")
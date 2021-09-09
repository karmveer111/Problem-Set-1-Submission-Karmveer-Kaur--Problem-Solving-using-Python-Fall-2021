#Problem set 1.3
#Name: Karmveer Kaur

balance=float(input("enter the outstanding balance on your credit card:Rs."))
annual_interest_rate=float(input("enter the annual credit card interest rate as a decimal:"))
min_monthly_payment=500 #minimun monthly payment 2 percent of 25000
balance=balance
while balance>=0:
    month=0
    min_monthly_payment=min_monthly_payment+2500 # with increment 5 percent of 25000
    balance=balance
    while month<=12 and balance>0:
        month=month+1
        monthly_interest_rate=annual_interest_rate/12.0
        balance=balance*(1+monthly_interest_rate)-min_monthly_payment

print("result")
print("monthly payment to payoff debt in 1 year:",min_monthly_payment)
print("number of months needed:",month)
print("balance:",balance)

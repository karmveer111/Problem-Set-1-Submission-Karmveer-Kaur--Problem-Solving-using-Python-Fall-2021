#Problem set 1.3
#Name: Karmveer Kaur

outstanding_balance=float(input('enter the outstanding balance on your credit card:'))
annual_interest_rate=float(input('enter the annual credit card interest rate as a decimal:'))
epsilon=0.01
month=1
balance=outstanding_balance
monthly_interest_rate=(annual_interest_rate)/12.0
monthly_payment_lower_rate=(outstanding_balance)/12.0
monthly_payment_upper_rate=(outstanding_balance*(1+monthly_interest_rate)**12.0)/12.0

total_payment=500.0
x=0.0

while abs(balance)>epsilon and month<12:
    month +=1
    min_monthly_payment=(monthly_payment_upper_rate+monthly_payment_lower_rate)*balance
    balance=outstanding_balance
    interest_paid=(annual_interest_rate/12)*balance
    principal_paid=min_monthly_payment-interest_paid
    remaining_balance=balance-principal_paid
    total_payment=float(total_payment + min_monthly_payment)
    while balance<=epsilon:
        monthly_payment_lower_bound=balance/12.0
        monthly_payment_upper_bound=(balance*(1+(annual_interest_rate/12.0))*12.0)/12.0
                           
print("result:")
print("1 year:",float(total_payment))
print("balance:",float(remaining_balance))
print("number of month:",month)

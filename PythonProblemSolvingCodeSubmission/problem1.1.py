#Problem set 1.1
#Name: Karmveer Kaur

balance=float(input('Enter the outstanding balance on your credit card:')) #take input form user for outstanding balance
annual_interest_rate=float(input('Enter the annual credit card interest rate as a decimal:')) #take input of annual interest rate form user 
monthly_payment_rate=float(input('Enter the minimum monthly payment rate as a decimal:')) #minimum monthly payment input from user
month=1 #first take the value for 1st month 
total_payment=0
while month<=12:#for the continuously next months
    epsilon=0.01
    print("month",month)
    month +=1 #next month
    
    Min_monthly_payment=monthly_payment_rate*balance #this the formula for minimum monthly payment
    Interest_paid=(annual_interest_rate/12)*balance 
    Principal_paid=Min_monthly_payment-Interest_paid
    Remaining_balance=balance-Principal_paid
    
    print("Minimum monthly payment : Rs.",float(Min_monthly_payment))#to print the minimum monthly payment 
    print("Principal Paid:Rs.",float(Principal_paid))# to print the principle paid monthly
    print("Remaining balance:Rs.",float(Remaining_balance)) #to print the remaining balance to pay monthly
    balance=Remaining_balance
    total_payment=float(total_payment + Min_monthly_payment)
    print("RESULT")
    print("Total amount paid:Rs." ,float(total_payment)) #total amount paid at the end 
    print("Remaining Balance:Rs." ,float(Remaining_balance)) #what amout left


# This is an Application to Find the Duration of an Investment

print("Investment System")
print("--------------------------")

name = input("Enter the Customer Name : ")
investedAmount = float(input("Enter Amount to Invest : $"))
rate = float(input("Enter the Rate : "))
duration = int(input("Enter the Duration in Years  : "))

interest = (investedAmount * rate * duration) / 100
totalAmount = interest + investedAmount

print()
print("Investment Slip")
print("--------------------")

print("Customer Name : ", name)
print("Amount Invested : $", investedAmount)
print("Interest Rate : ", rate, "%")
print("Duration ", duration, "Year")

print("Interest on Investment : ", interest)
print("Total Amount Gotten After Investment : ", interest + investedAmount)

billAmount = float(input("What was the total bill amount?"))
service = input("How was the service?(good, fair, bad) ")
totalTip = 0
if service == 'good':
    print(billAmount * 0.20)
    totalTip = billAmount * 0.20
elif service == 'fair':
    print(billAmount * 0.15) 
    totalTip = billAmount * 0.15  
elif service == 'bad':
    print(billAmount * 0.10)
    totalTip = billAmount * 0.10
else:
    print("No tip")
print(str(billAmount + totalTip))

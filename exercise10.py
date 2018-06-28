
actualcoins = 0
while True:
    coins = input("You have {} coins. Do you want another? ".format(actualcoins))
    if coins == "yes":
        actualcoins = actualcoins +1
        print(actualcoins)
    if coins == "no":
        print("bye")
        break
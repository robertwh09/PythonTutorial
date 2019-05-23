
print ("DiceEven\n")

def diceEven(X,Y):
    total = X + Y
    if total % 2 == 0:
        return "Even"
    return "Odd"
print ("DiceEven function defined\n")

X = 0
Y = 0
while X != "x":
    X = input("Please enter Roll one (x to end)")
    if X == "x":
        break
    Y = input("Please enter Roll two")
    result = diceEven(int(X),int(Y))
    print (" The total of your dice is ", result, "\n")

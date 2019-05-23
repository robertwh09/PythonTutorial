print ("Hex\n")
def Hex(number):
    if number == 10: return "A"
    if number == 11: return "B"
    if number == 12: return "C"
    if number == 13: return "D"
    if number == 14: return "E"
    if number == 15: return "F"

inputNumber = input ("Please enter a number between 0 and 255 ")
inputNumber = int(inputNumber)

if inputNumber < 0 or inputNumber > 255:
    print ("Number out of range")
    quit()

digit1 = int(inputNumber / 16)
if digit1 >=10: digit1 = Hex(digit1)

digit2 = inputNumber % 16
if digit2 >=10: digit2 = Hex(digit2)

print ("The hex for ", inputNumber, " is ", digit1, digit2)






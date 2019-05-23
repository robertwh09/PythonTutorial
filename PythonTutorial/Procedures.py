print ("Arrays\n")
continents = [['Africa', '2B'],
              ['Antarctica',100],
              ['Asia','5B'],
              ['Australia','100M'],
              ['Europe','500M'],
              ['North America','500M'],
              ['South America','1B']]

def PrintContinent(number):
    if number <0 or number > 6:
        print( "Range Error, please select between 0 and 6")
    elif number % 1 > 0:
        print("Type Error, please enter an interger only \n")
    else:
        number = int(number)
        
        print ("Continent Name is ", continents[number][0])
        print ("Continent Population is ", continents[number][1])
        print ("\n")

        #continentData = continents[number]
        #print ("Continent Name is ", continentData[0])
        #print ("Continent Population is ", continentData[1])

for i in range (0, 8):
    PrintContinent(i)


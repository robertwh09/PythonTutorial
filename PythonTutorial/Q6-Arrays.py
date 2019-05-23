print ("Q6 - Arrays\n")

MinsSpentOnPC = [[60,30,45,0],
                [180,60,0,60],
                [200,30,0,20],
                [60,10,15,15],
                [100,35,30,45]]

print ("Print each item in the Array")
for value in MinsSpentOnPC:
    print (value)
print ("\n")

total = 0
for student in range (0,3):

    for day in range (0,4):
        total = total + MinsSpentOnPC[day][student]

print ("Total = ", total)

average = total / (4 * 5)

print ("Average = ", average)


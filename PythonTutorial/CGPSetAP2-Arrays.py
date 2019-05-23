print ("CGP SetA P2 Q2d - Arrays\n")

Scores = [[7,10,3,19,7,17,4,6,12,17],
                [8,1,20,20,18,8,14,1,15,9],
                [17,7,1,20,1,3,13,20,0,17],
                [17,0,15,15,20,15,9,7,12,8],
                [19,19,0,12,19,2,9,9,6,0],
                [11,5,15,9,9,12,13,15,2,18]]

print (Scores)
print ("/n")

total = 0
for round in range (0,10):

    for player in range (0,6):

        total = total + Scores[player][round]

    average = total/6
    print ("Average for Round ",round, " is ", average)
    total = 0

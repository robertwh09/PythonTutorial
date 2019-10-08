import sys
import platform

print ('Output\n')
print ('Hello World!\n')

print(1, sys.version)
print(2, platform.python_implementation())
print(3, sys.executable)


print ('Input\n')
name = input ("What's your name?")
print ('Hello ', name)

print ('Selection\n')
age = input ("How old are you?")
age = int(age)

if age >= 17:
    print ('You are old enough to drive', name)
else:
    print ("Sorry you're not old enough to drive", name)






    



'''
def checkIfPrime (numberToCheck):
  for x in range(2, numberToCheck):
    if (numberToCheck%x == 0):
      return False
  return True
  
answer = checkIfPrime(8)
print(answer)

message1 = "Global Variable"

def myFunction():
  print("\nINSIDE THE FUNCTION")
#Global variables are accessible inside a function
  print (message1)
#Declaring a local variable
  message2 = "Local Variable"
  print (message2)

myFunction()

def someFunction(a, b, c=1, d=2, e=3):
  print(a, b, c, d, e)

someFunction(45,65,5)

'''

def addNumbers(*num):
  sum = 0
  for i in num:
    sum = sum + i
  print(sum)

addNumbers(1,2,3,4,5)


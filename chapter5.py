
myName = input('Please enter your name:')
#myAge = input("What about your age:")
#myAge = input("Hi %s, what about your age: " %(myName))
myAge = input("Hi {}, what about your age: ".format(myName))

print ("Hello World, my name is", myName, "and I am", myAge,
"years old.")

print ("Hello World, my name is %s and I am %s years old."%(myName,myAge))

print ("Hello World, my name is {} and I am {} years old.".format(myName,myAge))

print ('''Hello World
My name is James and 
I am 20 years old.''')


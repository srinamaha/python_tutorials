#pets = ["Dogs","Cats", "Hamester","Horse"]
#for mypets in pets:
 # print(mypets)


#age = {'Peter': 5, 'John':7}
#for myage in age:
  #print(myage)
 # print("Name = %s, Age = %d" %(myage, age[myage]))

#for i, j in age.items():
 # print("Name = %s, Age = %d" %(i, j))

#for i in range(1,15,2):
 # print (i)

#counter = 5
#while counter > 0 :
 # print ("Counter value is ", counter)
  #counter = counter - 1

j = 0
for i in range(5):
  j = j + 2
  print ('i = ', i, ', j = ', j)
#  if j == 6:
 #   break
  if j == 6:
    continue
    print ('I will be skipped over if j=6')
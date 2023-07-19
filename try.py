try:
  answer = 12/0
  print (answer)
#except:
 # print ("An error occurred")
except ValueError:
  print ("Error: You did not enter a number")
except Exception as e:
  print ("Unknown error: ", e)
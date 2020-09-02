count = 0 
for n in range (0,21) :
  count = count + 1
  if n % 3 == 0 :
    print("fizz",end='')
  if n % 5 == 0 : 
    print("buzz")
  print("")
  if n%3 != 0 and n % 5 != 0:
    print(n)
    
    
 or   
    
    
count = 0 
for n in range (0,21) :
  count = count + 1
  
  if n%3 == 0 and n%5 == 0 :
    print("FizzBuzz")
  elif n % 3 == 0 :
    print("fizz")
  elif n % 5 == 0 : 
    print("buzz")
  #elif n%3 != 0 and n % 5 != 0:
  else: 
      print(n)

def prime_checker(number):
  
  if number>1:
    for i in range(2,number):
      if number%i==0:
        print("It's not a prime number.")
        break
    else:
      print("It's a prime number.")
  elif number == 1 or number==0:
    print("It's not a prime number.")
      
n = int(input("Enter Number: "))
prime_checker(number=n)

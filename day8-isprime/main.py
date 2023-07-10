#Write your code below this line 👇
def prime_checker(number):
     # Numbers less than 2 are not prime
    if number < 2: 
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
    
n = int(input("Check this number: "))
isPrime = prime_checker(number=n)
if isPrime:
    print('It\'s a prime number.')
else:
    print('It\'s not a prime number.')    

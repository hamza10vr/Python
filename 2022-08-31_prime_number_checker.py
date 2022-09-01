#check if the given input is a prime number or not

def prime_checker(number):
    prime = True
    for num in range(1,number+1):
        if num ==1 or num ==number:
            continue
        else:
            if number % num ==0:
                prime = False
    
    if prime == True:
        print("It's a prime numbner")
    else:
        print("It's not a prime number")



    # if number % number ==0 and number %1 ==0:
    #     print("It's a prime numbner")
    # else:
    #     print("It's not a prime number")


n = int(input("Check this number: "))
prime_checker(number=n)
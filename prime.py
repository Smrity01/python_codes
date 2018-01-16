def check_prime(number):
    '''
    Objective       : To check whether the given number is prime or not
    Input parameter : User entered number
    Return value    : Boolean value true or false
    '''
    power = pow(2,number-1)
    if (power % number == 1):
        return True
    else:
        return False

num = int(input('Enter a number: '))
print("****USING FERMAT'S LITTLE THEOREM******")
if (check_prime(num) == True):
    print('Its is probably a prime...')
else: print('Its is NOT a prime...')
    

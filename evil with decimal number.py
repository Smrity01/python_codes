def check_evil(number):
    '''
     Objective: To check whether the input is evil or not 
     Input parameter:
         number: The input number as list
     Return value: 'evil' or 'not evil' string  
     '''
    #approach: if frequency of '1' is even then return 'evil'
            # else return 'not evil '

    count = frequency(number)
    if count % 2 == 0:
        return 'evil'
    else: return 'not evil'
    
def frequency(number):
    '''
     Objective: Calculate the frequency of '1'
     Input parameter:
         number: The input number as list
     Return value: 
     '''
    #approach: Increment the count for all "1's"
    count = 0
    while (number != 0):
        if number % 2 == 1:
            count += 1
        number = number // 2
    return count

def main():
    '''
     Objective: Take input from user
     Input values:
         number: The input number as list
     Output value: Print whether the input is evil or not
     '''
    #approach:

    number = int(input("enter the number: "))
    result = check_evil(number)
    print("This number is " , result,".....!!!!")

if (__name__=='__main__'):
    main()

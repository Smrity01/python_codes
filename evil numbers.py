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
    count1 = 0
    for i in range(0,len(number)):
        if number[i] == '1':
            count1 = count1 + 1     
    return count1   

def main():
    '''
     Objective: Take input from user
     Input values:
         number: The input number as list
     Output value: Print whether the input is evil or not
     '''
    #approach:

    number = list(input("enter the binary number: "))
    result = check_evil(number)
    print("This number is " , result,".....!!!!")

if (__name__=='__main__'):
    main()

'''
## TIDY OR NOT ##
Alisa just finished counting all positive integers in ascending order from 1 to N.
What was the last tidy number she counted?
   written by : Smrity Chaudhary
        Dated : 10/03/2018 

'''

def check_tidy(number):
    '''
    Objective        : Check whether the given number is tidy or not
    Input Parameter  : Number
    Return Value     : Flag value
    '''
    #Tidy number have digits in ascending order
    digits = list(number)
    flag = 0
    for index in range(len(digits)-1):
        if digits[index] < digits[index+1] or digits[index] == digits[index+1]:
            flag = 0
        else:
            flag = 1
    return flag
def close_tidy(number):
    '''
    Objective        : To find Last tidy number
    Input Parameter  : Number
    Return Value     : Last Tidy number
    '''
    #Keep decrementing the number and checking for tidy property
    flag = check_tidy(str(number))
    while(flag == 1):
        number = number - 1
        flag = check_tidy(str(number))
    return number
        
def main():
    '''
    Objective        : Take user input
    Input Parameter  : None
    Return Value     : None
    Output Value     : Last tidy number
    '''
    number = int(input('Enter number: '))
    tidy = close_tidy(number)
    print("Last tidy number: ",tidy)
main()

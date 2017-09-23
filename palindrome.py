def palindrome(string1,last,position=0):
    '''
    Objective: To Check whether the string is palindrome of not
    Input parameter:
            string1: The string Which need to be check for palindrome
            last: The last index of the string 
            position: To traverse the string
    '''
    #Approach: If the first and last character match
              #then call the palindrome function recusively
              # If characters does not match then it is not palindrome
    
    if(position < last):
        if(string1[position] == string1[last]):
            palindrome(string1,last-1,position+1)
        else: print('Its not a palindrome')
    else:print('Its a palindrome')

    
string1 = input('Enter the string: ')
last = len(string1)-1
palindrome(string1,last)

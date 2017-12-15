def check(string):
    '''
     Objective: To check the valid size of string
     Input Parameter:
         string : The input string 
     Return value: valid appended string
     '''
    length = len(string)
    if length >= 3:
        string = append(string)
    return string

def append(string):
     '''
     Objective: To append the prefix in the string
     Input Parameter:
         string : The input string 
     Return value: appended string
     '''

    if string[len(string)-3:] == 'ing':
        string = string + 'ly'
        return string
    else:
        string = string + 'ing'
        return string

def main():
    '''
     Objective: Take input string from user
     Input values:
         string : The input string
     Output value: to print appended string
     '''
    string = input('Enter the string: ') 
    string = check(string)
    print('New string is: ' ,string)

if (__name__ == '__main__'):
    main()

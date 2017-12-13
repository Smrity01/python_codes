def check(string):
    length = len(string)
    if length >= 3:
        string = append(string)
    return string

def append(string):
    if string[len(string)-3:] == 'ing':
        string = string + 'ly'
        return string
    else:
        string = string + 'ing'
        return string

def main():
    '''
     Objective: Take input from user
     Input values:
         number: The input number as list
     Output value: Print whether the input is evil or not
     '''
    #approach:
    string = input('Enter the string: ') 
    string = check(string)
    print('New string is: ' ,string)

if (__name__ == '__main__'):
    main()

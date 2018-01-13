def calculate(mylist):
        '''
    Objective       : To Calculate the sum of nested list
    Input Parameter :
            mylist  : Nested List of elements
    Return value    : Return sum of elements of the list
    
    '''
    sum = 0
    for pos in range(0,len(mylist)):
        if (type(mylist[pos]) == list):
            sum = sum + calculate(mylist[pos])
        else:
            sum = sum + mylist[pos]
    return sum
def main():
    '''
    Objective       : For Calling the function 
    Input Parameter : None
    Return value    : None
    
    '''
    mylist = [2,1,[5,6],3,[[1]]]
    sum = calculate(mylist)
    print('Sum of elements of the list: ',sum)
if(__name__ == '__main__'):
    main()

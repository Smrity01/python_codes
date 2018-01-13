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
def compute(dictionary):
    '''
    Objective       : To Calculate the sum of nested list
    Input Parameter :
        dictionary  : dictionary
    Return value    : The sum of values of different keys of dictionary
    
    '''
    keys = list(dictionary.values())
    return calculate(keys)
    
def main():
    '''
    Objective       : For Calling the function 
    Input Parameter : None
    Return value    : None
    
    '''
    dict1 = {'january':[5,[8]],'febrary':[6,1],'march':[7]}
    print('Sum of elements of the list: ',compute(dict1))

if(__name__ == '__main__'):
    main()

def combine(dict1,dict2):
    '''
    Objective: To combine two dictionaries by adding values of common keys
    Input Parameter:
          dict1: First dictionary
          dict2: second dictionary
    Return Value: Combined Dictionary
    '''
    #Approach: Get all the keys of both dictionaries
             # if common keys
             # add the values otherwise add default value which is 0
    total_keys = set(list(dict1.keys())+list(dict2.keys()))
    dict3 = {}
    for key in total_keys:
        dict3[key] = dict1.get(key,0) + dict2.get(key,0)
    return dict3

def main():
    
    '''
    Objective: Call a function To combine two dictionaries
    Input Parameter: None
    Return Value: None
    '''
    dict1 = {'a':100,'b':100,'c':300}
    dict2 = {'a':100,'b':100,'d':300}
    dict3 = {}
    dict3 = combine(dict1,dict2)
    print('Combine dictionary: ',dict3)

if (__name__=='__main__'):
    main()

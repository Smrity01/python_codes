import timeit
start = timeit.default_timer()

def minimum(mylist):
    '''
    Objective       : Return the index of minimum element
    Input parameter :
                 mylist : list of fruits with their quantity
    Return value    : Return the index of minimum quantity 
         
    '''
    quantity = []
    for i in range(len(mylist)):
        quantity.append(mylist[i][1])
    
    index = min_index(quantity,0,len(quantity)-1)  # calling a function min_index
    return index

def min_index(mylist,min_el_index,last_index,position=0):
    '''
    Objective       : Find the index of minimum element
    Input parameter :
                 mylist : The list in which minimum element is to be found
               position : To Traverse the list
           min_el_index :  Assumed as index of minimum element of the list
             last_index : last index of the list is stored 
    Return value    : Index of minimum element of the list
    '''
    #Approach: First element is assumed as minimum of the list and then compare with rest of the elements
    #if any of the element is smaller then minimum element then it becomes new minimum element
    
    
    if (position < last_index):
        if (mylist[min_el_index] > mylist[position+1]):
            min_el_index = position+1
            return min_index(mylist,min_el_index,last_index,position+1)
        
        else:return min_index(mylist,min_el_index,last_index,position+1)
        
    elif (mylist[min_el_index] > mylist[last_index]):
        min_el_index = last_index
        return min_el_index    
    else: return min_el_index

def main():
    '''
    Objective       : Call the minimum function
    Input parameter : None
    Output value    : Print the fruit with least quantity
         
    '''  
    mylist =[['Orange',59],['Apple',55],['Mango',78],['Kiwi',65],['Peach',90]]
    index = minimum(mylist)
    for  i in range(len(mylist)):
        if mylist[i][1]== mylist[index][1]:
            print(mylist[i][0],'has minimum quantity: ',mylist[i][1])

if (__name__ == '__main__'):
    main()


stop = timeit.default_timer()
print(stop - start) 

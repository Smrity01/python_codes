def min_index(mylist,min_el_index,last_index,position=0):
    '''
    Objective: Find the index of minimum element
    Input parameter:
           mylist: The list in which minimum element is to be found
           position: To Traverse the list
           min_el_index:  Assumed as index of minimum element of the list
           last_index: last index of the list is stored 
           
    
    Return value: Index of minimum element of the list
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
        
    
mylist=[27,16,-5,29,11,5]
min_el_index = 0
last_index = len(mylist)-1

#print the index of minimum element
print('Index of minimum element')
print(min_index(mylist,min_el_index,last_index))

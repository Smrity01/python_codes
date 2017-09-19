def min_index(mylist,min_el,last_index,position=0):
    '''
    Objective: Find the index of minimum element
    Input parameter:
           mylist: The list in which minimum element is to be found
           position: To Traverse the list
           min_el:  Assumed as minimum element of the list
           last_index: last index of the list is stored 
           
    
    Return value:  minimum element of the list
    '''
    #Approach: First element is assumed as minimum of the list and then compare with rest of the elements
    #if any of the element is smaller then minimum element then it becomes new minimum element
    
    
    if (position < last_index):
        if (mylist[min_el] > mylist[position+1]):
            min_el = position+1
        return min_index(mylist,min_el,last_index,position+1)
        
    else: return min_el
        
    
mylist = [27,16,13,29,11,5]
start = int(input('Enter the starting index: '))
last = int(input('enter the last index: '))
min_el = start
last_index = last

#print the index of minimum element
print(min_index(mylist,min_el,last_index))

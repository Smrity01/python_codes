def sorting(mylist,track=0):
    '''
    Objective: To sort the given list
    Input parameter:
           mylist: The list in which is to be sorted
           Track: To Traverse the list
                    
    
    Output: Print the sorted list
    '''
    #Approach: Find the minimium element of the list using min_index Function
    #Swap the minimum element with first element of the list
    #Repeat the process with rest of the list

    
    min_el_index = track
    last_index = len(mylist)-1
    position = track
    
    if (track < last_index):
        index = min_index(mylist,min_el_index,last_index,position)
        min_el = mylist[index]
        mylist[index]=mylist[track]
        mylist[track] = min_el
        sorting(mylist,track+1)
        
    else: return
        



def min_index(mylist,min_el_index,last_index,position):
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
        
   
    else: return min_el_index
        
     
mylist=[15,31,11,48,-2]
print('unsorted_list:',mylist)
sorting(mylist)
print('Sortedlist: ',mylist)

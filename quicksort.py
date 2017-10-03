# ******FUNCTION QUICKSORT USING RECURSION*******
# ******FUNCTION PARTITION USING RECURSION*******

def quicksort(mylist,low,high):
    '''
    Objective: To sort the given unsorted list
    Input Parameters:
            mylist: The list which is to be sorted
            low: The lower index of the list
            high: The higher index of the list
    Return value: It will return the Sorted list
    '''

    #Approach: DIVIDE AND CONQUER TECHNIQUE
    #The list is partitioned into two parts using pivot element
            # The index of pivot element is returned by partition function:
            # The sorting is done on first part of the list
            # Then the second part is considered
            # it repeats until the end
            
    
    if(low < high):
        pivot = partition(mylist,high,low,low)
        quicksort(mylist,low,pivot-1)
        return quicksort(mylist,pivot,high)
    
    else: return mylist



    
def partition(mylist,pivot,first,second):
    '''
    Objective: To partition the given unsorted list
    Input Parameters:
            mylist: The list which is to be sorted
            first: The index  to track the position of smaller elements to pivot element in the list
            second: The index  to track the position of greater elements to pivot element in the list
            pivot: The index of last element which is considered as pivot element

    Return value: It will return the right index of pivot element
    '''
    
#Approach: Two tracing variables are used:
    #First trace the lower elements to pivot element
    #second trace the greater elements to pivot element
    #Then the pivot element placed at its right position
    
    if second < pivot:
        if mylist[second] < mylist[pivot]:
            temp = mylist[first]
            mylist[first] = mylist[second]
            mylist[second] = temp
            return partition(mylist,pivot,first+1,second+1)

        # ***** In the case of duplicate elements ****
        '''
        elif mylist[second]==mylist[pivot]:
            temp = mylist[first]
            mylist[first] = mylist[second]
            mylist[second] = temp
            return partition(mylist,pivot,first+1,second+1)
            '''
        
        else:return partition(mylist,pivot,first,second+1)

    else:
        temp = mylist[first]
        mylist[first] = mylist[pivot]
        mylist[pivot] = temp
        pivot = first
        return pivot
            
   

    
print(quicksort([10,11,1,60,55,71,7,75],0,6))

'''
#test case
print(quicksort([10,1,1,60,55,7,7,75],0,6))
'''

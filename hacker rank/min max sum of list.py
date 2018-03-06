def insertion_sort(mylist):
     '''
    Objective: to append a value in sorted list
    Input parameter:
          mylist: list which is need to sorted
          
    '''
     #Approach: The list is divide into two parts:
                                         #right side of 'index': unsorted part
                                         #left side of 'index': sorted part
     #An element is picked from the right part and inserted in the left part at its sorted position

     for index in range(1,len(mylist)):
        element = mylist.pop(index)
        move_left(mylist,index,element)

        
        
def move_left(mylist,index,number,position=0):
    '''
    Objective: to append a value in sorted list
    Input parameter:
          mylist: list which is need to sorted
          number: number to be stored at right place in the list
          position: to traverse the list
          index: list is sorted on the left side of this index and unsorted on the right side
    '''
    #Approach: right position of the number is found recursively
    #Finally,element is inserted at right position

    if position < index:
        if (number < mylist[position]):
            mylist.insert(position,number)
            
        else:move_left(mylist,index,number,position+1)
    else:
        mylist.insert(index,number)
   
def find(mylist):
    sort_list = insertion_sort(mylist)
    length = len(mylist)-1
    min_sum = mylist[0] + mylist[1] + mylist[2] + mylist[3]
    max_sum = mylist[length] + mylist[length-1] + mylist[length-2] + mylist[length-3]
    print(min_sum,max_sum)
    
find([1,3,4,5,2])
    

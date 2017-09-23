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
   




mylist=[4,6,3,8,2,1,45,20]
print('Unsorted list: ',mylist)
insertion_sort(mylist)
print('Sorted List:',mylist)

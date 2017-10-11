def bubblesort(mylist):
     '''
    Objective: To place the highest element at its right position
    Input parameters: 
            mylist: The original list entered by user
            
    Return value: modified list is returned
    '''
     #Approach: The largest element is bubbled at highest position in the list
               #Then the second largest element is placed
               #And the process goes on till first element
     
     limit=len(mylist)-1
     while limit>0:
         swap_place(mylist,limit)
         limit=limit-1
         
     return mylist



     
def swap_place(mylist,index,position=0):
     '''
    Objective: To place the highest element at its right position
    Input parameters: 
            mylist: The original list entered by user
            index: The index where highest element is placed
            position: To track the list given by user
            
    Return value: modified list is returned
    '''
     #Approach: The largest element of the the list is placed at given index
               #By swapping the elements
     
     if position < index:
         if mylist[position]>mylist[position+1]:
            temp=mylist[position]
            mylist[position]=mylist[position+1]
            mylist[position+1]=temp
            return swap_place(mylist,index,position+1)

         else: return swap_place(mylist,index,position+1)
     else: return mylist

mylist=[10,30,45,40,19,30,28,90,76]
print(bubblesort(mylist))

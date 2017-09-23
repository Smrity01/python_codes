def binary_search(mylist,element):
    '''
    Objective: To search a number in the list using binary search algorithm
    Input parameter:
            mylist: The list in which number is to be search
            element: A number which is to be search in the list
            
    '''

    #Approach: Divide and conquer technique is used


    upper=len(mylist)
    lower=-1
    
    find(mylist,element,lower,upper)
  

    
def find(mylist,element,lower,upper):
    '''
    Objective: To search a number in the list sequentially
    Input parameter:
            mylist: The list in which number is to be search
            element: A number which is to be search in the list
            upper: upper limit of the list
            lower: lower limit of the list
    Ouput: Print whether the number is found or not.
            If number is found then its index is also printed
    '''

    #Approach: The list is divided into 2 parts:
                        #The middle element is compared with the searched element
                        #If middle element is greater than the searched element:- left half of the list is searched
                        #Else the right half of the list is searched
    
    if upper > lower+1:
       mid = (lower+upper) // 2
       if mylist[mid] == element:
           return print('Element found at: Index',mid)
       if mylist[mid] > element:
           return find(mylist,element,lower,mid)
        
       else:return find(mylist,element,mid,upper)

    else:print('Oops.......Element not found')
    
    


mylist=[2,17,29,45,51,64,67,72,89,100]
print('Your list is: ',mylist)
element=int(input('Enter the element you want to search: '))
binary_search(mylist,element) 

    
    

def deep_copy(mylist,newlist,position=0):
    '''
    Objective: To deep copy a nested list
    Input parameters: 
            mylist: The original nested list entered by user
            newlist: The new created list
            position: To track the list given by user
            
    Return value: new copied list is returned

    '''
    #Approach: The type of elements of the list is compared
            #If it is list type then deep_copy function is called on that nested list
            #If it is int type the element copied in newlist
            #It repeats until the end of the list
    #Recursion is used

    
    if(position < len(mylist)):
    
        if(type(mylist[position]) == int):
            element = mylist[position]
            newlist.insert(position,element)
            return deep_copy(mylist,newlist,position+1)
        
        elif (type(mylist[position]) == list):
            length = len(mylist[position])
            testlist=[]
            deep_copy(mylist[position],testlist,0)
            newlist.insert(position,testlist)
            return deep_copy(mylist,newlist,position+1)
             
    else:return newlist



mylist=[10,30,[20],45,[40,[19],[30,28],90],76]
newlist=[]
print('******Copied list*****')
print(deep_copy(mylist,newlist))

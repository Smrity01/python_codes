def flatter(mylist,newlist,position=0,index=0):
    '''
    Objective: To flatter a nested list
    Input parameters: 
            mylist: The original nested list entered by user
            newlist: The flattered list
            position: To track the list given by user
            index: to track the new list
    Return value: new flattered list is returned

    '''
    #Approach: The type of elements of the list is compared
            #If it is list type then flatter function is called on that nested list
            #If it is int type the element copied in newlist
            #It repeats until the end of the list
    #Recursion is used

    
    if(position < len(mylist)):
    
        if(type(mylist[position]) == int):
            element = mylist[position]
            newlist.insert(index,element)
            return flatter(mylist,newlist,position+1,index+1)
        
        elif (type(mylist[position]) == list):
            length = len(mylist[position])
            flatter(mylist[position],newlist,0,index)
            return flatter(mylist,newlist,position+1,index + length)
             
    else:return newlist



mylist=[10,30,[20],45,[40,[19],[30,28],90],76]
newlist=[]
print(flatter(mylist,newlist))

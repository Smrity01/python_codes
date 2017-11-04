def movezero(mylist,limit,pos = 0):
    '''
     Objective: The Move all the zeroes at the end of the list
    Input parameter:
          mylist: user entered list
          limit: index of last element in the list
          position: to traverse the list
    '''
    #approach: recursive call of the function move zero
    
    len_mylist = len(mylist)
    if (pos < limit):
        if mylist[pos] == 0:
            element = mylist.pop(pos)
            mylist.insert(len_mylist,element)
            return movezero(mylist,limit-1,pos)
        else: return movezero(mylist,limit,pos+1)
    else: return mylist
def main():
    '''
    Objective: To take input from the user
    Input:
         size: Take input size of the list
          mylist: A list which store the user entered elements
          element: A number to be stored in the list
    Output:  Modified list
    '''
    mylist=[]
    size = int(input('Enter the size of the list: '))
    for i in range(0,size):
        element = int(input('Enter the element: '))
        mylist.insert(i,element)
    movezero(mylist,size-1)
    print('Modified list After moving all zeroes at the end: ',mylist)
if __name__ == '__main__':
    main()
    


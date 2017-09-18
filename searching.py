def searching(mylist,number,position=0):
    '''
    Objective: To search a number in the list sequentially
    Input parameter:
            mylist: The list in which number is to be search
            number: A number which is to be search in the list
            position: To traverse the list
    Ouput: Print whether the number is found or not.
            If number is found then its index is also printed
    '''

    #Approach: Recursively search the list

    if position < len(mylist):
        if number == mylist[position]:
            print('***Number is found*** at the following index: ',position)
        else:searching(mylist,number,position+1)
    elif number == mylist[len(mylist)-1]:
         print('***Number is found*** at the following index: ',position)
    else: print('*****Number is not found in the list******')


mylist = [65,89,5,57,25,11,3]
print('This is list in which number is to be searched:',mylist)
number = int(input('Enter the number you want to search: '))
searching(mylist,number)

'''
   ##Oversized pancake flipper##
   Given the current state of the pancakes, calculate the minimum number of uses of the oversized
   pancake flipper needed to leave all pancakes happy side up('1': Happy side, '0': Sad side),
   or state that there is no way to do it.
   
   written by : Smrity Chaudhary
        Dated : 10/03/2018 
'''
def flip_list(mylist,window):
    '''
    Objective        : Flip the given list of window size
    Input Parameter  : List of string and window size
    Return Value     : Flipped list
    '''
    if(len(mylist) < window):
        return mylist
    for index in range(len(mylist)):
        if mylist[index] == "1":
            mylist[index] = "0"
        else:
            mylist[index] = "1"
    return mylist

def solve(mylist,window):
    '''
    Objective        : Count the flips and the logic to divide the main list into given window size
    Input Parameter  : List of string and window size
    Return value     : Flip count and flipped list
    '''
    flips_count = 0
    for index in range(len(mylist)):
        if mylist[index] == "0":
            mylist[index:index+window] = flip_list(mylist[index:index+window],window)
            flips_count = flips_count+1
    return flips_count

def check(mylist,window):
    '''
    Objective        : Check whether the list is totally flipped or not
    Input Parameter  : List of string and window size
    Output value     : Flip count and flipped list if solution exist
    '''
    flips_count = solve(mylist,window)

    for index in range(0,len(mylist)):
        if mylist[index] == "0":
            flag = 1
        else:
            flag = 0     
    if flag == 0:
        print(flag)
        print("it has solution",mylist," Count of flips: ",flips_count)
    else:
        print("it doesn't have solution")

def main():
    '''
    Objective        : Take the user input
    Input Parameter  : None
    Output value     : None
    '''
    case = int(input("how many Cases: "))
    case_list = []
    mylist = []
    for index in range(case):
        mylist = list(input("Enter list: ").split(','))
        window = int(input("Enter window size: "))
        case_list.append(mylist)
        case_list.append(window)
    for index in range (0,case*2,2):
        check(case_list[index],case_list[index+1])
        
main()

    

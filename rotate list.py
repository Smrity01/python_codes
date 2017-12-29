def rotate(mylist):
    '''
    Objective       : To left Rotate the list
    Input Parameter :
            mylist  : The list which need to be rotate
    Return Value    : none
    '''
    mylist = mylist[1:] + mylist[:1]
    '''
    using inbuilt functions: mylist.append(mylist.pop(0))
    '''
def main():
    '''
    Objective       : To call the Rotate function
    Input Parameter : None
    Return Value    : none
    '''
    mylist = [3,4,5,6,2,7,8,6]
    print('List before rotation: ',mylist)
    rotate(mylist)
    print('List after rotation',mylist)

if (__name__ == '__main__'):
    main()

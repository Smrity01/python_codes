
def merge(mylist,mylist2,finallist):
    '''
    objective: to merge 2 unsorted list
    input parameter:
          mylist: first unsorted list
          mylist2: Second unsorted list
          finallist: The new merged list
    return value: final merged list
    '''
    #Approach: 
    pos = 0
    
    if mylist != [] and mylist2 != []:
        if mylist[pos] < mylist2[pos]:
            el = mylist.pop(pos)
            appendlist(el,finallist)
            return merge(mylist,mylist2,finallist)
        elif mylist[pos]>mylist2[pos]:
            el = mylist2.pop(pos)
            appendlist(el,finallist)
            return merge(mylist,mylist2,finallist)
        else:
            el = mylist2.pop(pos)
            appendlist(el,finallist)
            el = mylist.pop(pos)
            appendlist(el,finallist)
            return merge(mylist,mylist2,finallist)
    elif mylist != []:
         el = mylist.pop(pos)
         appendlist(el,finallist)
         return merge(mylist,mylist2,finallist)
    elif mylist2 != []:
         el = mylist2.pop(pos)
         appendlist(el,finallist)
         return merge(mylist,mylist2,finallist)
    else: return finallist


def appendlist(number,lst,position=0):
    '''
    objective: to append a value in sorted list
    input parameter:
          lst: original sorted list
          number: the number which is inserted in the list
          position: to traverse the list
    return value:  modified list
    '''
    #approach: recursive call of the function
    if (finallist != []):
        if(number< lst[len(lst)-1]):
            if(number < lst[position]):
                lst.insert(position,number)
                return lst
            else: 
                return appendlist(number,lst,position+1)
        else:
            lst.insert(len(lst),number)
    else: lst.insert(0,number)

mylist=[6,8,9,12,23,65,43,16]
mylist2=[6,7,5,4]
finallist=[]
merge(mylist,mylist2,finallist)
print('The final merge list: ',finallist)

def mergesort(mylist,userlist):
    finallist=[]
    i=0

    merge(mylist,userlist,finallist,i)
    print('The final merge list: ',finallist)

def merge(mylist,userlist,finallist,i):
    p=0
    
    if mylist!=[] and userlist!=[]:
        if mylist[p]<userlist[p]:
            el=mylist.pop(p)
            finallist.insert(i,el)
            return merge(mylist,userlist,finallist,i+1)
        elif mylist[p]>userlist[p]:
            el=userlist.pop(p)
            finallist.insert(i,el)
            return merge(mylist,userlist,finallist,i+1)
    elif mylist!=[]:
         el=mylist.pop(p)
         finallist.insert(i,el)
         return merge(mylist,userlist,finallist,i+1)
    elif userlist!=[]:
         el=userlist.pop(p)
         finallist.insert(i,el)
         return merge(mylist,userlist,finallist,i+1)
    else: return





mylist=[6,8,9,12,23,65,78]
print('****Merge your list with my list****')
print('Here is my list',mylist)
print('****Now enter yours***')
number_of_element=int(input('How many elements you want to enter in the list: '))
userlist=[]
for i in range(number_of_element):
    element = int(input('Enter elements in the list: '))
    userlist.insert(i,element)
mergesort(mylist,userlist)

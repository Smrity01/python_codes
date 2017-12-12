def calculate(mylist):
    sum = 0
    for pos in range(0,len(mylist)):
        if (type(mylist[pos]) == list):
            sum = sum + calculate(mylist[pos])
        else:
            sum = sum + mylist[pos]
    return sum
def main():
    mylist = [2,1,[5,6],3,[[1]]]
    sum = calculate(mylist)
    print('Sum of elements of the list: ',sum)
if(__name__ == '__main__'):
    main()

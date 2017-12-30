def rotate(mylist):
    element = mylist[:1]
    print(element)
    mylist = mylist[1:] + mylist[:1]
def main():
    mylist = [3,4,5,6,2,7,8,6]
    print('List before rotation: ',mylist)
    rotate(mylist)
    print('List after rotation',mylist)

if (__name__ == '__main__'):
    main()

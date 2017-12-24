def main():
    f=open("shopinglist.txt",'w')
    answer = True
    while(answer != 'exit' ):
        answer=input("Enter the item to add in the shopping list(otherwise exit): ")
        if (answer != 'exit' ):
            f.write(answer)
            f.write("\n")
    f.close()

if (__name__=='__main__'):
    main()
    

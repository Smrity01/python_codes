def number(num):
    dict1 = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'fourty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninty'}
    dict2 = {3:'hundred',4:'thousand',6:'lac',8:'crore'}
    if(dict1.get(num,'\0') == '\0' ):
        count = count_digits(num)
        if count>7:
            number(num//(10**7))
            print('crore',end=' ')
            number(num%(10**7))
        elif (count == 3):
            digit = num//(10**2)
            double_digits(digit,dict1,dict2,3)
            number(num%(10**2))
        elif (count == 4 or count == 5):
            digit = num//(10**3)
            double_digits(digit,dict1,dict2,4)
            number(num%(10**3))
        elif (count == 6 or count == 7):
            digit = num//(10**5)
            double_digits(digit,dict1,dict2,6)
            number(num%(10**5))
        else:
            double_digits(num,dict1,dict2,0)
           
    else:print(dict1.get(num),end=' ')
def double_digits(num,dict1,dict2,count):
    if(dict1.get(num,'\0') != '\0' ):
        print(dict1.get(num,'\0'),dict2.get(count,'\0'),end=' ')
    else:
        print(dict1.get((num//10)*10,'\0'),dict1.get((num%10),'\0'),dict2.get(count,'\0'),end=' ')
          
def count_digits(num):
    count = 0 
    while(num != 0):
        count = count+1        
        num = num//10
    return count

#number(60)
#print(count_digits(100001))

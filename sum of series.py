def compute(number,count):
    '''
    Objective: To compute the sum of series n+nn+nnn....
    Input Parameter: 
            number: The number whose series need to find
            count: number of elements in the series
    Return value: sum of the series
    '''
    sum = 0
    result = 0
    for i in range(0,count):
        sum = number * pow(10,i)+sum
        result = result + sum
        
    return result

def main():
    '''
    Objective: Call a function to compute the sum of series n+nn+nnn....
    Input Parameter: None
    Return value: None
    '''
    number = int(input("Enter the number: "))
    count = int(input("Enter the count: "))
    x = compute(number,count)
    print('Sum of the series: ',x)

if (__name__ == '__main__'):
    main()
    

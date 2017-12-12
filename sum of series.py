def compute(number,count):
    sum = 0
    result = 0
    for i in range(0,count):
        sum = number*pow(10,i)+sum
        result = result + sum
        
    return result
def main():
    number = int(input("Enter the number: "))
    count = int(input("Enter the count: "))
    x = compute(number,count)
    print('Sum of the series: ',x)

if (__name__ == '__main__'):
    main()
    

def birthdayCakeCandles(n, ar):
    '''
    '''
    tallest = max(ar)
    count = 0
    for i in range(n):
        if(tallest == ar[i]):
            count = count + 1

    return count
#n = int(input().strip())
#ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(4, [3,2,1,3])
print(result)

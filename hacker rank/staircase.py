def stair_case(num):
    temp = 1
    spaces = num-1
    while(spaces >= 0):
        print(' '*(spaces),'#'*temp,sep='')
        temp = temp+1
        spaces = spaces-1
        
stair_case(5)

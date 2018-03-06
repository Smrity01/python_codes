def timeConversion(s):
    length = len(s)
    mm = s[3:5]
    ss = s[6:8]
    if(s[length-2:] == 'PM' and s[0:2] != '12'):
        hh = str(int(s[0:2]) + 12)
    elif(s[length-2:] == 'AM' and s[0:2] == '12'):
        hh = '0' + str(int(s[0:2]) - 12)
    else:
        hh = s[0:2]
    return hh+':'+mm+':'+ss
   

#s = input().strip()
result = timeConversion('12:00:00AM')
print(result)

def sentence(list1,list2,list3):
    combination = []
    for i in range(0,len(list1)):
        for j in range(0,len(list2)):
            for k in range(0,len(list3)):
                combination.append(list1[i]+' '+list2[j]+' '+list3[k])
                
    return combination
def main():
    list1 = ['I','You','Archita']
    list2 = ['love','like']
    list3 = ['football','kdrama','coding']
    finallist = []
    finallist = sentence(list1,list2,list3)
    print(*finallist,sep='\n')

if(__name__ == '__main__'):
    main()

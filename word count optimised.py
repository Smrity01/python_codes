def more_frequent(words,finallist):
    '''
    Objective       : To traverse the list for all unique words in the sentence
    Input parameter :
             words  : List of words in the sentence
         finallist  : Final list of words with there counts
    Return value    : None
         
    '''
    for word in words:
        if words.count(word)>1:
            if word not in finallist:
                finallist.append(word)
                finallist.append(words.count(word))
def main():
    '''
    Objective       : Take input from user
    Input parameter : None
    Output value    : Print the occurrences of each unique
         
    '''  
    string = input('enter your sentence: ')
    words = string.split() # Split the string into list of words
    final_list =[]
    more_frequent(words,final_list)
    print('\n Following words have more the one occurences in the sentence:\n')
    print('\n ***Word*** : ***Count***\n')
    for i in range(0,len(final_list),2):
        print(final_list[i],':',final_list[i+1],'\n')
    
if (__name__ == '__main__'):
    main()

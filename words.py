def more_frequent(words,finallist):
    '''
    Objective       : To traverse the list for all unique words in the sentence
    Input parameter :
             words  : List of words in the sentence
         finallist  : Final list of words with there count
    Return value    : Final list of words with there count
         
    '''
    if(len(words) > 0):
        my_word = words[0]            # Variable for storing unique word
        count = 0                     # Variable for storing count of word
        count = count_word(words,my_word,count) # call 'count_word' to calculate the count of unique word 'my_word'
        if (count > 1):               # Only append the words having more than one occurrences 
            finallist.append(my_word) # Store the unique word in finallist
            finallist.append(count)   # Store the count of unique word in finallist
        return more_frequent(words,finallist)
    else:
        return finallist

def count_word(words,my_word,count,pos=0):
    '''
    Objective       : To traverse the list for count the occurrences of unique word
    Input parameter :
             words  : List of words in the sentence
           my_word  : Occurrences of this word will be calculated
             count  : Calculated count will be stored here
               pos  : To traverse the list of words
    Return value    : Count of unique word in the list
         
    '''     
    if (pos < len(words)):
        if my_word == words[pos]:   # Comparing word with all other words in list
            words.pop(pos)          # Delete the occurrences of that word
            count = count+1         # Counting the occurrences
            return count_word(words,my_word,count,pos)
        else:return count_word(words,my_word,count,pos+1)
    else: return count

         
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

def main():
    '''
    Objective: Read the text file and print the first longest word with its length
    Input Parameter: None
    Return value: None
    '''
    f = open("poem.txt","r")                      #Open the text file
    count_list = []
    word_list = []
    for line in f:
        for word in line.split():
            count_list.append(len(word))          #Count of each word
            word_list.append(word)                #Respective words

    max_index = count_list.index(max(count_list)) #Index of maximum length
    max_word = word_list[max_index]               #Longest Word 
    print('longest word: ',max_word)
    print('length of longest word: ',max_count)
    f.close()

if (__name__=='__main__'):
    main()


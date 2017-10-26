from random import shuffle
def createdeck():
    '''
    Objective: To create a deck of cards
    Input parameters: none
    Return value: A deck of cards
    '''
    #Approach: Create a nested list of 52 cards
              #with the rank & Suit of a card
    deck = [['ace','sphade'],[2,'sphade'],[3,'sphade'],[4,'sphade'],[5,'sphade'],[6,'sphade'],[7,'sphade'],[8,'sphade'],
          [9,'sphade'],[10,'sphade'],['jack','sphade'],['queen','sphade'],['king','sphade'],
          ['ace','diamond'],[2,'diamond'],[3,'diamond'],[4,'diamond'],[5,'diamond'],[6,'diamond'],[7,'diamond'],[8,'diamond'],
          [9,'diamond'],[10,'diamond'],['jack','diamond'],['queen','diamond'],['king','diamond'],
          ['ace','heart'],[2,'heart'],[3,'heart'],[4,'heart'],[5,'heart'],[6,'heart'],[7,'heart'],[8,'heart'],
          [9,'heart'],[10,'heart'],['jack','heart'],['queen','heart'],['king','heart'],
          ['ace','club'],[2,'club'],[3,'club'],[4,'club'],[5,'club'],[6,'club'],[7,'club'],[8,'club'],
          [9,'club'],[10,'club'],['jack','club'],['queen','club'],['king','club']]
    
    return deck

def shuffle_deck(deck):
    '''
    Objective: To shuffle the given deck of cards
    Input parameters:
                deck: The given deck of cards
    Return value: Shuffled deck of cards
    '''
    #Approach: Use inbuilt function shuffle of a library random
    shuffle(deck)
    return deck

def deal(top,shuffled):
    '''
    Objective: To return the top most card of the shuffled deck
    Input parameters:
                 top: The index of the top most card without replacement
            shuffled: The shuffled deck of cards
    Return value: The topmost card
    '''  
    topcard = []
    topcard = shuffled[top]
    return topcard


def calculate_score(topcard,score):
    '''
    Objective: To calculate the score of user and computer
    Input parameters:
                topcard: the topcard which is used to caculate the score
                score: previous score of the user or computer
    Return value: current score of user or computer
    '''
    #Approach: According to rules:
         #rank of topcard card is added in the previous score
    
    if(topcard[0] == 'ace'):
        if (score+11 < 21):
            score = score+11
        else: score = score+1
    elif (topcard[0] == 'jack' or topcard[0] == 'queen' or topcard[0] == 'king'):
        score = score+10
    else:
        score=score+topcard[0]
    return score


def twentyone():
    '''
    Objective: This function Keep track of the whole game 21
    Input parameters: none
    Return value: none
    '''
    #Approach: If the user scores more than 21,he will lose
         #if user score is less than computer's score, he will lose
         #The user win if and only if he scores less than 21 or more than computer's score 
    
    answer='HIT'
    deck = createdeck()
    shuffled = shuffle_deck(deck)
    top = 0
    topcard = []
    user_score = 0

    while(answer == 'HIT' or answer == 'hit'):
        topcard = deal(top,shuffled)
        top = top+1
        user_score = calculate_score(topcard,user_score)
        print('Your card is: ',topcard[0],'of',topcard[1])
        print('Your score is: ',user_score)
        if user_score > 21:
            print('\n \n *****OOPSS...YOU LOSE*****')
            break
        if user_score == 21:
            print('\n \n *******YOU WIN******')
            break

        answer=input('\n \nYOU WANT TO "HIT OR STAY: " ')
        
    if user_score<21 :
        print('\n \n *******COMPUTERS TURN********')
        comp_score=0
        while comp_score < 17:
            comp_card = deal(top,shuffled)
            top = top+1
            comp_score=calculate_score(comp_card,comp_score)
        print("computer's score is: ",comp_score)
        if(comp_score > user_score and comp_score < 21 or comp_score == 21):
            print('\n *******COMPUTER WINS********* \n \n*********OOPSS...YOU LOSE************')
        elif (comp_score == user_score):
            print("*******OOPSS.... IT's a TIE******")
        else: print('\n \n *******YOU WIN********')
    

    

def main():
    '''
    Objective: call the twentyone function and let the user to play the game
    Input parameters: none
    Return value: none
    '''
    
    print("*************let's play TWENTY ONE*****************\n \n \n")
    twentyone()
    
if __name__ == '__main__':
    main()
    

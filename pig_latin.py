def encrypt(data):
    '''
    Objective: To encrypt the string
    Input parameter:
            data: The user enter string
    output: print the encrpyt string
    '''
    #Approach: Piglatin encrpytion
    
    element = data[0]
    data = data[1:] + element
        
    data = data + 'ay'
        
    print('Encrypted Data: ',data)
    return data

def decrypt(data):
    '''
    Objective: To decrypt the encrypted string
    Input parameter:
            data: The encrypted string
    output: print the decrpyted string
    '''
    #Approach: Piglatin Decryption
    
    limit = len(data)-2
    
    data = data[:limit]
    element = data[limit-1:]
    data = element + data[0:limit-1]

    print('Decrypted Data: ',data)

data=input('Enter the String you want to encrypt: ')

data1 = encrypt(data)
decrypt(data1)

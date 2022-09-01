
##🐛Bug alert: What happens if you try to encode the word 'civilization' to 'hnanqnefynts' shift = 5?🐛
## Hello World! with Shfit =5  --> qnuux fxaum!


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
shifted_alphabets = list(alphabet)
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
text = 'Hello World!'.lower()
shift = 9


def encrypt(message, shift_number):
    
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    cipher_text = ''

    for _ in range(shift):
        shifted_alphabets.append(shifted_alphabets.pop(0))  # remove element from the front and add it to the back

        ############# decrypt ############
        # shifted_alphabets.insert(0,(shifted_alphabets.pop())) # remove last element and add it to the front / for decryption

    # print(shifted_alphabets) #for debugging
    # message_index = [] 

    for char in message:
        if char in alphabet:
            position = alphabet.index(char) # .index() give the first occurance
            cipher_text += shifted_alphabets[position]
            # message_index.append(alphabet.index(char)) #for debugging
        else:
            cipher_text += char

    # print(message_index)  # for debugging 


    
    print(cipher_text)
    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list


#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(text,shift)
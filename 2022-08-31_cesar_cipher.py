
##🐛Bug alert: What happens if you try to encode the word 'civilization' to 'hnanqnefynts' shift = 5?🐛
## Hello World! with Shfit =5  --> qnuux fxaum!


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_txt,shift_amount,cipher_direction):
    shifted_alphabets = list(alphabet)
    cipher_text = ''
    
    if cipher_direction == 'encode':
        for _ in range(shift_amount):
            shifted_alphabets.append(shifted_alphabets.pop(0))  # remove element from the front and add it to the back
    elif cipher_direction == 'decode': 
        for _ in range(shift_amount):
            shifted_alphabets.insert(0,(shifted_alphabets.pop())) # remove last element and add it to the front / for decryption
    
    # print(shifted_alphabets) #for debugging
    # message_index = [] 


    for char in start_txt:
        if char in alphabet:
            position = alphabet.index(char) # .index() give the first occurance
            cipher_text += shifted_alphabets[position]
            # message_index.append(alphabet.index(char)) #for debugging
        else:
            cipher_text += char

    print(cipher_text)


############ for debugging ##### auto input  ########
direction ='encode'
text = 'Hello World!'.lower()
shift = 9
caesar(text, shift, direction)

direction ='decode'
text = 'qnuux fxaum!'.lower()
shift = 9

caesar(text, shift, direction)

#####################################################
continue_game = True
while continue_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    user_input = (input("Type 'yes' if you want to go again, Otherwise type 'no': \n")).lower()
    if user_input == 'no':
        continue_game = False
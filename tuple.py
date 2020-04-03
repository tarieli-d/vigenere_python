from src import *


def encrypt(start_text, keyword):
    end_text = ()
    for e, let in enumerate(start_text):
        if let.isalpha():
            len_sum = char_position(let) + char_position(keyword[e])
            end_text = end_text+(pos_to_char(len_sum % 26, let),)
        else:
            end_text = end_text + (let,)
    return end_text


def decrypt(end_text, keyword):
    start_text = ()
    for e, let in enumerate(end_text):
        if let.isalpha():
            start_text = start_text + (pos_to_char((char_position(let) + 26 - char_position(keyword[e])) % 26, let),)
        else:
            start_text = start_text + (let,)
    return start_text


# convert text to tuple
textTuple = tuple(text)
keyTuple = tuple(key)

# We need this two below,in while
keywordTuple = ()
i = 1

# Get Keyword from key,it's the same length as plain text,it's need while encryption and decryption
while len_text != 0:
    keywordTuple = keywordTuple+(keyTuple[i-1],)
    if len_key == i:
        i = 1
    else:
        i += 1
    len_text -= 1


# invoke functions
encrypted_tuple = encrypt(textTuple, keywordTuple)
decrypted_tuple = decrypt(encrypted_tuple, keywordTuple)

print('Encrypted tuple: ', encrypted_tuple)
print('Decrypted tuple: ', decrypted_tuple)

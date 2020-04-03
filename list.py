from src import *

def encrypt(start_text, keyword):
    end_text = []
    for e, let in enumerate(start_text):
        if let.isalpha():
            len_sum = char_position(let) + char_position(keyword[e])
            end_text.append(pos_to_char(len_sum % 26, let))
        else:
            end_text.append(let)
    return end_text


def decrypt(end_text, keyword):
    start_text = []
    for e, let in enumerate(end_text):
        if let.isalpha():
            start_text.append(pos_to_char((char_position(let) + 26 - char_position(keyword[e])) % 26,let))
        else:
            start_text.append(let)
    return start_text


# lists for plaintext,key and keyword.keyword we will get from from key
ListText = list(text)
ListKey = list(key)
ListKeyword = []
i = 1

# here we get ListKeyword from key,it's the same length as plain text,it's need while encryption and decryption
while len_text != 0:
    ListKeyword.append(ListKey[i-1])
    if len_key == i:
        i = 1
    else:
        i += 1
    len_text -= 1


# invoke functions
endText = encrypt(ListText, ListKeyword)
startText = decrypt(endText, ListKeyword)

print("encrypted list:", endText)
print("decrypted list:", startText)



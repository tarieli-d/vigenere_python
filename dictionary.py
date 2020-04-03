from src import *

alphabet_pos = {'A': 0, 'a': 0, 'B': 1, 'b': 1, 'C': 2, 'c': 2, 'D': 3, 'd': 3,
                'E': 4, 'e': 4, 'F': 5, 'f': 5, 'G': 6, 'g': 6, 'H': 7, 'h': 7, 'I': 8, 'i': 8,
                'J': 9, 'j': 9, 'K': 10, 'k': 10, 'L': 11, 'l': 11, 'M': 12, 'm': 12, 'N': 13,
                'n': 13, 'O': 14, 'o': 14, 'P': 15, 'p': 15, 'Q': 16, 'q': 16, 'R': 17, 'r': 17,
                'S': 18, 's': 18, 'T': 19, 't': 19, 'U': 20, 'u': 20, 'V': 21, 'v': 21, 'W': 22,
                'w': 22, 'X': 23, 'x': 23, 'Y': 24, 'y': 24, 'Z': 25, 'z': 25}


def encrypt(start_text, keyword):
    end_text = {}
    for e, let in enumerate(start_text):
        if let.isalpha():
            len_sum = (alphabet_pos[let] + alphabet_pos[keyword[e]]) % 26
            end_text[e] = pos_to_char(len_sum, let)
        else:
            end_text[e] = let
    return end_text


def decrypt(end_text, keyword):
    start_text = {}
    for e, let in enumerate(end_text):
        if end_text[let].isalpha():
            len_sum = (alphabet_pos[end_text[e]] + 26 - alphabet_pos[keyword[e]]) % 26
            start_text[e] = pos_to_char(len_sum, end_text[e])
        else:
            start_text[e] = end_text[e]
    return start_text


# Keyword and 2 variables needed below in while loop.keyword we will get from key below
dict_Keyword = {}
d = 0
i = 1

# Get Keyword from key,it's the same length as plain text,we need it while encryption and decryption
while len_text != 0:
    dict_Keyword[d] = key[i - 1]
    if len_key == i:
        i = 1
    else:
        i += 1
    len_text -= 1
    d += 1

# invoke functions
endText = encrypt(text, dict_Keyword)
startText = decrypt(endText, dict_Keyword)

print("encrypted dictionary:", endText)
print("decrypted dictionary:", startText)

# user input
text = input("input text:")
key = input("input key:")

# variables needed in working files
len_text = len(text)
len_key = len(key)
i = 1


# find out char position
def char_position(letter):
    if letter.isupper():
        return ord(letter) - 65
    return ord(letter) - 97


# get character according to position
def pos_to_char(pos, let):
    if let.isupper():
        return chr(pos + 65)
    return chr(pos + 97)

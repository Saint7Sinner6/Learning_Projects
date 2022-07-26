
def caesar_cipher_decryption(text, offset):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decryption = ""
    
    #This function will intake a coded cypher and output a decrypted cypher.
    text = text.upper()
    for i in range(len(text)):
        char = text[i]
        if char not in alphabet:
            decryption += char
        else:
            index = alphabet.find(char)
            mod_index = (index + offset) % 26
            decryption += alphabet[int(mod_index)]
    return decryption

#Testing string
"""
text = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
print(caesar_cipher_decryption(text, 10))
"""


def caesar_cipher_encryption(text, offset):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encryption = ""
    
    #This function will intake a message and output an encrypted cypher.
    text = text.upper()
    for i in range(len(text)):
        char = text[i]
        if char not in alphabet:
            encryption += char
        else:
            index = alphabet.find(char)
            mod_index = (index - offset) % 26
            encryption += alphabet[int(mod_index)]
    return encryption

"""
text = "Test message!"
print(caesar_cipher_encryption(text, 10))
"""


def brute_decoder(message):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    possibilities = []
    
    #This function will intake a coded cypher and output a decrypted cypher.
    text = message.upper()
    for z in range(26):
        decryption = ""
        for i in range(len(message)):
            char = text[i]
            if char not in alphabet:
                decryption += char
            else:
                index = alphabet.find(char)
                mod_index = (index + int(z)) % 26
                decryption += alphabet[int(mod_index)]
        possibilities.append(decryption)
        
    return '\n'.join(possibilities)

message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
print(brute_decoder(message))



def vigenere_cypher(message, keyword):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key_phrase = ''
    decryption = ''

    for i in range(len(message)):
        if message[i] == " ":
            key_phrase += " "
            decryption += " "
        else:
            key_phrase += keyword[i % len(keyword)]
            decryption += alphabet[(message[i].find(alphabet) - key_phrase[-1].find(alphabet)) % 26]
    
    return key_phrase, decryption


    

"""
Tasks:
1. Get message length
2. Continue to add letters of keyword indefinitly until keyword length == message length.
3. Once we have key_phrase, for index of messaage, compare index of key_phrase against index of alphabet.
4. Append matching character of alphabet for index of key_phrase to return value.
"""

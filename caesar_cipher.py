def caesar_cipher(text, offset):
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
print(caesar_cipher(text, 10))
"""
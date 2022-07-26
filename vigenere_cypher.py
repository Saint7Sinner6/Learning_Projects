def vigenere_cypher_decryption(message, keyword):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_phrase = ''
    decryption = ''
    counter = 0

    for i in range(0, len(message)):
        if message[i] not in alphabet:
            key_phrase += " "
            decryption += message[i]
        else:
            key_phrase += keyword[counter % len(keyword)]
            if key_phrase[i] not in alphabet:
                decryption += message[i]
            else:
                decryption += alphabet[(alphabet.find(message[i]) - alphabet.find(key_phrase[-1])) % 26]
            counter = (counter + 1) % len(keyword)
    
    return decryption, key_phrase, counter

message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
keyword = "friends"
print(vigenere_cypher_decryption(message, keyword))


def vigenere_cypher_encrypt(message, keyword):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_phrase = ''
    encryption = ''
    counter = 0

    for i in range(0, len(message)):
        if message[i] not in alphabet:
            key_phrase += " "
            encryption += message[i]
        else:
            key_phrase += keyword[counter % len(keyword)]
            if key_phrase[i] not in alphabet:
                encryption += message[i]
            else:
                encryption += alphabet[(alphabet.find(message[i]) + alphabet.find(key_phrase[-1])) % 26]
            counter = (counter + 1) % len(keyword)
    
    return encryption
    

message = "test encryption behavior."
keyword = "alpha"
print(vigenere_cypher_encrypt(message, keyword))
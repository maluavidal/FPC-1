alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

encrypted_seq = [char for char in input()]
encrypted_msg = [char for char in input()]

decrypted_msg = ''

for letter in encrypted_msg: # para cada letra na mensagem criptografada,
    for l in encrypted_seq:  # ao percorrer as letras da sequência recebida,
        if letter == l:      # se as letras encontradas nos laços forem iguais,
            decrypted_msg += alphabet[encrypted_seq.index(l)] # o index da letra encontrada é procurado na lista do alfabeto original, concatenando seu valor à variável descriptografada 
            break

print(decrypted_msg)

import numpy as np

def create_tableau(keyword: str, text: str):
    #Створює таблицю для табличного шифру
    keyword = "".join(sorted(set(keyword), key=keyword.index))  # Унікальні символи в порядку появи
    columns = len(keyword)
    text = text.replace(" ", "").upper()
    
    while len(text) % columns != 0:
        text += "X"
    
    rows = len(text) // columns
    matrix = np.array(list(text)).reshape(rows, columns)
    
    sorted_indices = sorted(range(len(keyword)), key=lambda x: keyword[x])
    
    ciphertext = "".join("".join(matrix[:, i]) for i in sorted_indices)
    
    return ciphertext, matrix, sorted_indices

def decrypt_tableau(keyword: str, ciphertext: str):
    #Розшифровує табличний шифр
    keyword = "".join(sorted(set(keyword), key=keyword.index))
    columns = len(keyword)
    rows = len(ciphertext) // columns
    
    sorted_indices = sorted(range(len(keyword)), key=lambda x: keyword[x])
    reversed_indices = sorted(range(len(keyword)), key=sorted_indices.__getitem__)
    
    matrix = np.zeros((rows, columns), dtype=str)
    col_index = 0
    for i in sorted_indices:
        matrix[:, i] = list(ciphertext[col_index * rows:(col_index + 1) * rows])
        col_index += 1
    
    plaintext = "".join(matrix.flatten()).rstrip("X")  #Видаляємо додані 'X'
    return plaintext

def vigenere_encrypt(text: str, key: str):
    #Шифрування шифром Віженера
    text = text.replace(" ", "").upper()
    key = key.upper()
    key_repeat = (key * (len(text) // len(key) + 1))[:len(text)]
    
    ciphertext = ""
    for t, k in zip(text, key_repeat):
        if t.isalpha():
            new_char = chr(((ord(t) - ord('A') + (ord(k) - ord('A'))) % 26) + ord('A'))
            ciphertext += new_char
        else:
            ciphertext += t
    return ciphertext

def vigenere_decrypt(ciphertext: str, key: str):
    #Розшифрування шифром Віженера
    key = key.upper()
    key_repeat = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
    
    plaintext = ""
    for c, k in zip(ciphertext, key_repeat):
        if c.isalpha():
            new_char = chr(((ord(c) - ord('A') - (ord(k) - ord('A'))) % 26) + ord('A'))
            plaintext += new_char
        else:
            plaintext += c
    return plaintext

def restore_spaces(reference: str, text: str):
    #Відновлює пробіли у тексті відповідно до оригінального
    text_list = list(text)
    for i, char in enumerate(reference):
        if char == ' ':
            text_list.insert(i, ' ')
    return "".join(text_list)

# Тестування алгоритмів
plaintext = "The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. The critic is he who can translate into another manner or a new material his impression of beautiful things. The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can express everything. Thought and language are to the artist instruments of an art. Vice and virtue are to the artist materials for an art. From the point of view of form, the type of all the arts is the art of the musician. From the point of view of feeling, the actor's craft is the type. All art is at once surface and symbol. Those who go beneath the surface do so at their peril. Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. Diversity of opinion about a work of art shows that the work is new, complex, vital. When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless thing is that one admires it intensely. All art is quite useless."

# Рівень 1: Табличний шифр
ciphertext_1, _, _ = create_tableau("MATRIX", plaintext)
decrypted_text_1 = restore_spaces(plaintext, decrypt_tableau("MATRIX", ciphertext_1))

# Рівень 2: Шифр Віженера + Табличний шифр
vigenere_ciphertext = vigenere_encrypt(plaintext, "CRYPTO")
ciphertext_2, _, _ = create_tableau("CRYPTO", vigenere_ciphertext)
decrypted_tableau_2 = decrypt_tableau("CRYPTO", ciphertext_2)
decrypted_vigenere_2 = vigenere_decrypt(decrypted_tableau_2, "CRYPTO")
decrypted_vigenere_2 = restore_spaces(plaintext, decrypted_vigenere_2)

# Вивід результатів
print("Рівень 1 - Табличний шифр:")
print("Зашифрований текст:", ciphertext_1)
print("Розшифрований текст:", decrypted_text_1)

print("\nРівень 2 - Віженер + Табличний шифр:")
print("Шифр Віженера:", vigenere_ciphertext)
print("Після Табличного шифру:", ciphertext_2)
print("Розшифрований текст:", decrypted_vigenere_2)

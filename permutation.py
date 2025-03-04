import numpy as np

def text_to_matrix(text, key):
    # Перетворення тексту на матрицю за довжиною ключа
    key_length = len(key)
    positions = [i for i, char in enumerate(text) if char.isspace() or char in ".,'"]
    clean_text = [char for char in text if not char.isspace() and char not in ".,'"]
    rows = -(-len(clean_text) // key_length)  # округлення вгору
    matrix = np.full((rows, key_length), fill_value=" ", dtype=str)
    
    for i, char in enumerate(clean_text):
        matrix[i // key_length, i % key_length] = char
    
    return matrix, positions

def get_permutation_order(key):
    # Отримання порядку перестановки з урахуванням алфавітного порядку ключа
    return sorted(range(len(key)), key=lambda k: key[k])

def encrypt(text, key):
    # Шифрування тексту за шифром перестановки
    matrix, positions = text_to_matrix(text, key)
    order = get_permutation_order(key)
    
    encrypted_text = "".join("".join(matrix[:, col]) for col in order)
    
    return encrypted_text, positions

def decrypt(encrypted_text, key, positions, original_length):
    # Розшифрування тексту за шифром перестановки
    key_length = len(key)
    order = get_permutation_order(key)
    rows = -(-len(encrypted_text) // key_length)  # округлення вгору
    
    matrix = np.full((rows, key_length), fill_value=" ", dtype=str)
    index = 0
    
    for col in order:
        for row in range(rows):
            if index < len(encrypted_text):
                matrix[row, col] = encrypted_text[index]
                index += 1
    
    decrypted_text = "".join(matrix.flatten()).strip()
    
    # Відновлення пробілів та розділових знаків
    text_with_spaces = list(decrypted_text)
    for pos in positions:
        if pos < len(text_with_spaces):
            text_with_spaces.insert(pos, " ")
    
    return "".join(text_with_spaces)[:original_length]

# Вхідні дані
text = "The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. The critic is he who can translate into another manner or a new material his impression of beautiful things. The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can express everything. Thought and language are to the artist instruments of an art. Vice and virtue are to the artist materials for an art. From the point of view of form, the type of all the arts is the art of the musician. From the point of view of feeling, the actor's craft is the type. All art is at once surface and symbol. Those who go beneath the surface do so at their peril. Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. Diversity of opinion about a work of art shows that the work is new, complex, vital. When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless thing is that one admires it intensely. All art is quite useless."
key = "SECRET"

# Шифрування
encrypted_text, positions = encrypt(text, key)
print("Зашифрований текст:", encrypted_text)

# Дешифрування
decrypted_text = decrypt(encrypted_text, key, positions, len(text))
print("Розшифрований текст:", decrypted_text)
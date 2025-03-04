import numpy as np

def generate_permutation_key(key):
    return sorted(range(len(key)), key=lambda k: key[k])

def transpose(text, key, encrypt=True):
    columns = len(key)
    rows = -(-len(text) // columns)
    matrix = [[' ' for _ in range(columns)] for _ in range(rows)]
    
    for i, char in enumerate(text):
        matrix[i // columns][i % columns] = char
    
    permuted_matrix = []
    permutation = generate_permutation_key(key)
    
    if encrypt:
        for row in matrix:
            permuted_matrix.append([row[i] for i in permutation])
    else:
        for row in matrix:
            new_row = [''] * columns
            for idx, i in enumerate(permutation):
                new_row[i] = row[idx]
            permuted_matrix.append(new_row)
    
    return ''.join([''.join(row) for row in permuted_matrix])

def double_transposition_encrypt(text, key1, key2):
    first_pass = transpose(text, key1, encrypt=True)
    second_pass = transpose(first_pass, key2, encrypt=True)
    return second_pass

def double_transposition_decrypt(text, key1, key2):
    first_pass = transpose(text, key2, encrypt=False)
    second_pass = transpose(first_pass, key1, encrypt=False)
    return second_pass

# Вхідні дані
key1 = "SECRET"
key2 = "CRYPTO"
plaintext = "The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. The critic is he who can translate into another manner or a new material his impression of beautiful things. The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can express everything. Thought and language are to the artist instruments of an art. Vice and virtue are to the artist materials for an art. From the point of view of form, the type of all the arts is the art of the musician. From the point of view of feeling, the actor's craft is the type. All art is at once surface and symbol. Those who go beneath the surface do so at their peril. Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. Diversity of opinion about a work of art shows that the work is new, complex, vital. When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless thing is that one admires it intensely. All art is quite useless."

# Шифрування
ciphertext = double_transposition_encrypt(plaintext, key1, key2)
print("Зашифрований текст:", ciphertext)

# Дешифрування
decrypted_text = double_transposition_decrypt(ciphertext, key1, key2)
print("Розшифрований текст:", decrypted_text)

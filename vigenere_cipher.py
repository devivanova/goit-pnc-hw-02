import re
from collections import Counter

def vigenere_cipher(text, key, encrypt=True):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key.upper()
    text = text.upper()
    result = []
    key_index = 0
    
    for char in text:
        if char in alphabet:
            shift = alphabet.index(key[key_index])
            if not encrypt:
                shift = -shift
            new_index = (alphabet.index(char) + shift) % 26
            result.append(alphabet[new_index])
            key_index = (key_index + 1) % len(key)
        else:
            result.append(char)
    
    return ''.join(result)

def kasiski_examination(ciphertext):
    min_len = 3  # Мінімальна довжина повторюваної послідовності
    sequences = {}
    
    for i in range(len(ciphertext) - min_len + 1):
        seq = ciphertext[i:i+min_len]
        if seq in sequences:
            sequences[seq].append(i)
        else:
            sequences[seq] = [i]
    
    distances = []
    for seq, indexes in sequences.items():
        if len(indexes) > 1:
            for j in range(1, len(indexes)):
                distances.append(indexes[j] - indexes[j - 1])
    
    gcd_counter = Counter()
    for d in distances:
        for i in range(2, d + 1):
            if d % i == 0:
                gcd_counter[i] += 1
    
    most_common = gcd_counter.most_common()
    return most_common

# Вхідні дані
txt = "The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. The critic is he who can translate into another manner or a new material his impression of beautiful things. The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can express everything. Thought and language are to the artist instruments of an art. Vice and virtue are to the artist materials for an art. From the point of view of form, the type of all the arts is the art of the musician. From the point of view of feeling, the actor's craft is the type. All art is at once surface and symbol. Those who go beneath the surface do so at their peril. Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. Diversity of opinion about a work of art shows that the work is new, complex, vital. When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless thing is that one admires it intensely. All art is quite useless."

# Видалення пробілів та знаків пунктуації для аналізу
txt_cleaned = re.sub(r'[^A-Z]', '', txt.upper())

# Шифрування
key = "CRYPTOGRAPHY"
cipher_text = vigenere_cipher(txt, key, encrypt=True)
print("Зашифрований текст:")
print(cipher_text)

# Розшифрування
decrypted_text = vigenere_cipher(cipher_text, key, encrypt=False)
print("\nРозшифрований текст:")
print(decrypted_text)

# Аналіз методом Касіскі
print("\nМетод Касіскі для визначення довжини ключа:")
kasiski_results = kasiski_examination(txt_cleaned)
print(kasiski_results)

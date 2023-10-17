def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)
def crack_caesar_with_known_word(ciphertext, known_word):
    for shift in range(26):
        decrypted_text = caesar_decipher(ciphertext, shift)
        if known_word in decrypted_text:
            return decrypted_text, shift
    return None, None

def affine_cipher(text, a, b, m=26):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((a * (ord(char) - base) + b) % m + base)
        else:
            result += char
    return result

def affine_decipher(text, a, b, m=26):
    result = ""
    inverse_a = next((x for x in range(1, m) if (a * x) % m == 1), None)
    if inverse_a is None:
        raise ValueError(f"'a'={a} has no modular inverse modulo {m}")
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr(inverse_a * (ord(char) - base - b) % m + base)
        else:
            result += char
    return result

def substitution_cipher(text):
    words = text.split()
    word_map = {word: str(index) for index, word in enumerate(words)}
    encrypted = ' '.join([word_map.get(word, word) for word in words])
    return encrypted, word_map

def substitution_decipher(text, word_map):
    words = text.split()
    reverse_map = {v: k for k, v in word_map.items()}
    decrypted = ' '.join([reverse_map.get(word, word) for word in words])
    return decrypted

def main():
    print("Text Encryption and Decryption")

    action = input("Choose action - Encrypt (E) / Decrypt (D): ").lower()
    if action not in ['e', 'd']:
        print("Invalid action choice.")
        return

    print("Select algorithm:")
    print("1. Caesar Cipher\n2. Affine Cipher\n3. Substitution Cipher")
    choice = input("Enter choice (1/2/3): ")

    text = input("Enter text: ")

    if choice == '1':
        if action == 'e':
            shift = int(input("Shift value: "))
            print("Encrypted:", caesar_cipher(text, shift))
        else:
            known_word = input("Enter a known word from the original text (or press Enter to skip): ")
            if known_word:
                decrypted, found_shift = crack_caesar_with_known_word(text, known_word)
                if decrypted:
                    print("Decrypted with shift", found_shift, ":", decrypted)
                else:
                    print("Couldn't decrypt using the provided known word.")
            else:
                shift = int(input("Shift value: "))
                print("Decrypted:", caesar_decipher(text, shift))
    elif choice == '2':
        a, b = int(input("Value of a: ")), int(input("Value of b: "))
        if action == 'e':
            print("Encrypted:", affine_cipher(text, a, b))
        else:
            print("Decrypted:", affine_decipher(text, a, b))
    elif choice == '3':
        if action == 'e':
            encrypted, mapping = substitution_cipher(text)
            print("Encrypted:", encrypted)
            print("Word Map:", mapping)
        else:
            word_map = eval(input("Provide word map as dictionary: "))
            print("Decrypted:", substitution_decipher(text, word_map))
    else:
        print("Invalid algorithm choice.")

if __name__ == "__main__":
    main()


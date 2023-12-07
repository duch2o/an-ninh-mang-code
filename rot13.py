def rot13(text):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr(((ord(char) - 65 + 13) % 26) + 65)
        elif 'a' <= char <= 'z':
            result += chr(((ord(char) - 97 + 13) % 26) + 97)
        else:
            result += char
    
    return result

original_text = input("Enter a text to ROT13 encode: ")
encoded_text = rot13(original_text)

print("\n--------------------------------\n")
print("Original Text: ", original_text)
print("\n--------------------------------\n")
print("ROT13 Encoded: ", encoded_text)
print("\n--------------------------------\n")


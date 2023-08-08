ans = ""

def caesar_encrypt(text, key):
    global ans
    for i in range(len(text)):
        ch = text[i]

        if ch == " ":
            ans += " "
        elif ch.isupper():
            ans += chr((ord(ch) + key - 65) % 26 + 65)
        else:
            ans += chr((ord(ch) + key - 97) % 26 + 97)
    return ans

input_text = input("Enter the string to be encrypted: ")
key = int(input("Enter the key to be shifted by: "))

print("Plain Text is: " + input_text)
print("Shift pattern is: " + str(key))
print("Cipher Text is: " + caesar_encrypt(input_text, key))

# A B C D ......... Z
# key=2
# C D E F ......... B
# aaron = A A R O N
# AARON = C C T Q P
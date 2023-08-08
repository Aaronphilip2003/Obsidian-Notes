
# **Classical cryptography**

## 1) **Caesar Cipher**

```
The Caesar cipher is one of the simplest and oldest encryption techniques used to secure messages. It is a substitution cipher where each letter in the plaintext is shifted a fixed number of positions down the alphabet. The fixed shift value is known as the "key" or "shift." For example, with a shift of 3, 'A' would become 'D', 'B' would become 'E', and so on.

Here's a brief summary of how the Caesar cipher works:

1. Choose a shift value (key) - This is typically a positive integer representing the number of positions each letter will be shifted.
    
2. Encrypting a message - For each letter in the plaintext, find its position in the alphabet, apply the shift, and replace it with the corresponding letter in the new position. Non-alphabetic characters (such as spaces or punctuation) are left unchanged.
    
3. Decrypting a message - To decrypt a message encoded using the Caesar cipher, simply apply the reverse shift (by subtracting the key instead of adding) to each letter in the ciphertext.
    

The Caesar cipher is relatively easy to understand and implement but is not considered secure by modern standards due to its vulnerability to brute-force attacks, where an attacker can try all possible shift values until the original message is revealed. As a result, it's mostly used for educational purposes and not for practical encryption in real-world scenarios.
```

```python
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
```


## 2) **Hill Cipher**

```
Hill cipher is a symmetric encryption algorithm used for converting plaintext into ciphertext and vice versa. It was proposed by Lester S. Hill in 1929 and is a polygraphic substitution cipher, meaning it encrypts multiple letters at once. Unlike many traditional ciphers that operate on a single letter at a time, Hill cipher processes blocks of letters simultaneously.

The algorithm works with matrices and modular arithmetic. It requires a key matrix that is used for encryption and decryption. The size of the key matrix depends on the block size of plaintext; for example, if the block size is 2, the key matrix will be a 2x2 matrix.

The encryption process involves breaking the plaintext into blocks, each represented as a vector of numerical values (usually mapped from letters). The key matrix multiplies with each block, resulting in a new vector, which is then converted back to ciphertext. Decryption follows a similar process but uses the inverse of the key matrix to retrieve the original plaintext.

Hill cipher offers some level of security due to its polygraphic nature and the use of matrices, but it is vulnerable to attacks if the key matrix is not chosen properly, especially if it has a low determinant or is poorly distributed. Additionally, it is not suitable for encrypting large amounts of data because the key matrix size grows proportionally with the block size, making it less efficient compared to modern encryption algorithms like AES (Advanced Encryption Standard).
```

```python
def split(a):  # splitting the string into its arbitrary characters
    return [char for char in a]

def arbitraryNumbers(lst):  # returning the arbitrary value of the alphabets
    lst_arb = []
    for i in lst:
        lst_arb.append(ord(i) - 65)  # Considering 'A' as 0, 'B' as 1, and so on...
    return lst_arb
  
def getKeyMatrix(key):
    keyMatrix = [[0] * 3 for _ in range(3)]  # Initialize the keyMatrix as a 3x3 matrix
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = key[k] % 65  # Convert key characters to 0-25 range
            k += 1
    return keyMatrix

def matrix_multiplication(keyMatrix, messageVector):
    result = [0] * 3
    for i in range(3):
        for j in range(3):
            result[i] += (keyMatrix[i][j] * messageVector[j])
        result[i] = result[i] % 26
    return result


def HillCipher(message, key):
    # Generate key matrix from the key string
    keyMatrix = getKeyMatrix(key)
    # Generate vector for the message
    messageVector = arbitraryNumbers(message)
    cipherVector = matrix_multiplication(keyMatrix, messageVector)
    cipherText = [chr(c + 65) for c in cipherVector]
    print("Ciphertext:", "".join(cipherText))
def main():
    # Get the message to be encrypted
    message = "ACT"
    # Get the key
    key = [ord(c) for c in "GYBNQKURP"]
    HillCipher(message, key)
if __name__ == "__main__":

    main()
```


def split(a):  # splitting the string into its arbitrary characters
    return [char for char in a]

def arbitraryNumbers(lst):  # returning the arbitrary value of the alphabets
    lst_arb = []
    for i in lst:
        lst_arb.append(ord(i) - 65)  # Considering 'A' as 0, 'B' as 1, and so on...
    return lst_arb

def getKeyMatrix(key):
    keyMatrix = [[0] * 3 for _ in range(3)]  # Initialize the keyMatrix as a 3x3 matrix
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = key[k] % 65  # Convert key characters to 0-25 range
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

    # Encrypt the message
    cipherVector = matrix_multiplication(keyMatrix, messageVector)

    # Generate the encrypted text
    cipherText = [chr(c + 65) for c in cipherVector]

    # Finally, print the ciphertext
    print("Ciphertext:", "".join(cipherText))

# Driver Code
def main():
    # Get the message to be encrypted
    message = "ACT"

    # Get the key
    key = [ord(c) for c in "GYBNQKURP"]

    HillCipher(message, key)

if __name__ == "__main__":
    main()

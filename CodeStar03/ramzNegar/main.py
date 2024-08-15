import re


def clean_txt(text):
    text = text.upper()
    text = re.sub('[\W_]+', ' ', text)
    text = re.sub(' +', ' ', text).strip()
    return text


def decodeInput(text):
    inputList = text.split(" ")
    cipher = inputList[0]
    plaintext = clean_txt(re.search(r'-text\s+"([^"]*)"', text).group(1))
    k = int(inputList[inputList.index("-key") + 1]) if "-key" in inputList else None
    a = int(inputList[inputList.index("-a") + 1]) if "-a" in inputList else None
    b = int(inputList[inputList.index("-b") + 1]) if "-b" in inputList else None
    mapping = clean_txt(inputList[inputList.index("-mapping") + 1]) if "-mapping" in inputList else None
    return cipher, plaintext, k, a, b, mapping


def decoderSystem(mapping="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    letter_to_num = {' ': -1}
    num_to_letter = {-1: ' '}
    for idx, letter in enumerate(list(mapping)):
        letter_to_num[letter] = idx
        num_to_letter[idx] = letter
    return letter_to_num, num_to_letter


def main(cipher, plaintext, k=None, a=None, b=None, mapping=None):
    letter_to_num, num_to_letter = decoderSystem()

    def additiveCipher():
        encryptedText = list(plaintext)
        decryptedText = []
        for lett in encryptedText:
            value = ((letter_to_num[lett] + k) % 26) if lett != ' ' else -1
            decryptedText.append(num_to_letter[value])

        return ''.join(decryptedText)

    def multiplicativeCipher():
        encryptedText = list(plaintext)
        decryptedText = []
        for lett in encryptedText:
            value = ((letter_to_num[lett] * k) % 26) if lett != ' ' else -1
            decryptedText.append(num_to_letter[value])

        return ''.join(decryptedText)

    def affineCipher():
        encryptedText = list(plaintext)
        decryptedText = []
        for lett in encryptedText:
            value = (((letter_to_num[lett] * a + b) % 26) % 26) if lett != ' ' else -1
            decryptedText.append(num_to_letter[value])

        return ''.join(decryptedText)

    def mappingCipher():
        new_letter_to_num, new_num_to_letter = decoderSystem(mapping=mapping)
        encryptedText = list(plaintext)
        decryptedText = []
        for lett in encryptedText:
            value = letter_to_num[lett]
            decryptedText.append(new_num_to_letter[value])

        return ''.join(decryptedText)

    if cipher == 'additive-cipher':
        return additiveCipher()
    elif cipher == 'multiplicative-cipher':
        return multiplicativeCipher()
    elif cipher == 'affine-cipher':
        return affineCipher()
    elif cipher == 'mapping-cipher':
        return mappingCipher()


if __name__ == "__main__":
    num_queries = int(input())
    queries = [input() for _ in range(num_queries)]
    for query in queries:
        cipher, plaintext, k, a, b, mapping = decodeInput(query)
        decryptedText = main(cipher=cipher, plaintext=plaintext, k=k, a=a, b=b, mapping=mapping)
        print(decryptedText)

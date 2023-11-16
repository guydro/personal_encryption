import random
import pyperclip

def encrypt(txt):
    og_txt = txt
    words = txt.split(" ")
    while "" in words:
        words.remove("")

    for i, word in enumerate(words):
        j = len(word)
        k = random.randint(0, j-1)
        words[i] = [word[:k], word[k:], j-k]

    j = len(words)
    k = random.randint(0, j-2)
    words[0][0], words[k][0] = words[k][0], words[0][0] + "~"

    encrypted = ""
    for word in words:
        rnd = int(0.5+random.random())
        encrypted += word[0] + "-"*rnd + "@"*(1-rnd)
        if len(encrypted) >= 2 and encrypted[-2] == "~":
            encrypted = encrypted[:-1]

    encrypted = encrypted[:-1] + "@"

    for word in words:
        rnd = int(0.5+random.random())
        encrypted += word[1] + "-"*rnd

    if "~" not in encrypted:
        encrypt(og_txt)
        return

    questions = ""
    for word in words:
        questions += input("Please enter a question that results in " + str(word[2]) + ": ") + "\n"

    pyperclip.copy(encrypted)
    print("encrypted text (copied to clipboard):")
    print(encrypted, end="\n\n")

    print("questions:")
    print(questions)


def decrypt(txt, questions):
    questions = questions.split(" ")
    while "" in questions:
        questions.remove("")

    words = []
    for question in questions:
        words += [["", int(question)]]

    txt = txt.split("@")
    first_chunk = "-".join(txt[:-1]) + "-"
    second_chunk = txt[-1]

    reminder = ""
    i = 0
    for chr in first_chunk:
        if chr in "~-@":
            if chr == "~":
                k = i

            words[i][0] = reminder
            i += 1
            reminder = ""

        else:
            reminder += chr

    words[0][0], words[k][0] = words[k][0], words[0][0]

    j = 0
    for word in words:
        for _ in range(word[1]):
            while second_chunk[j] == "-":
                j += 1
            word[0] += second_chunk[j]
            j += 1

    decrypted_text = ""
    for word in words:
        decrypted_text += word[0] + " "


    print("decrypted text:")
    print(decrypted_text, end="\n\n")




if __name__ == '__main__':
    encrypt(input("Enter text to encrypt:\n"))
    decrypt(input("Enter encrypted text:\n"), input("Enter answer to questions seperated by spaces:\n"))

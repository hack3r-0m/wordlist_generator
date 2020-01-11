print("WORLDLIST GENERATOR")
n_words = int(input("Enter how many words you want to combine :"))

list_user_words = []

for _ in range(0, n_words) :
    list_user_words.append(input())

choice_leet = input("Do you want to enable LEET mode ? [Y/N]").lower()

def leet(text) :
    getchar = lambda c: chars[c] if c in chars else c
    chars = {"a":"4","e":"3","l":"1","o":"0","s":"5"}
    return ''.join(getchar(c) for c in text)

if choice_leet == "y" :
    for i in range(0, n_words) :
        list_user_words.append(leet(list_user_words[i]))
else :
    list_user_words = list_user_words

additive_strings = [

    "123",
    "@123",
    "1",
    "#",
    "@",
    "007",
    "2",
    "$",
    "*",
    "0",
    "&",
    '12345',
    '111',
    'iloveyou',
    '666',
    'abc123',
    '123123',
    '!@#$%^&* ',
    'aa1234',
    'donald'

]

output_file = open("wordlist_gen.txt", "a+", encoding="utf-8")

def string_combiner() :

    global count
    count = 0

    for word in list_user_words :
        for string in additive_strings:

            print(word + string)
            count += 1
            output_file.writelines(word + string + "\n")

            print((word + string).capitalize())
            count += 1
            output_file.writelines((word + string).capitalize() + "\n")

            print(word.upper() + string.upper())
            count += 1
            output_file.writelines(word.upper() + string.upper() + "\n")

            print(word + string.upper())
            count += 1
            output_file.writelines(word + string.upper() + "\n")

            print(string + word.upper())
            count += 1
            output_file.writelines(string + word.upper() + "\n")

            print(string + word)
            count += 1
            output_file.writelines(string + word + "\n")

            print((string + word).capitalize())
            count += 1
            output_file.writelines((string + word).capitalize() + "\n")

    for word1 in list_user_words :
        for word2 in list_user_words:

            print(word1 + word2)
            count += 1
            output_file.writelines(word1 + word2 + "\n")

            print(word2 + word1)
            count += 1
            output_file.writelines(word2 + word1 + "\n")

            print((word1 + word2).capitalize())
            count += 1
            output_file.writelines((word1 + word2).capitalize() + "\n")

            print(word1.upper() + word2.upper())
            count += 1
            output_file.writelines(word1.upper() + word2.upper() + "\n")

            print(word1.upper() + word2)
            count += 1
            output_file.writelines(word1.upper() + word2 + "\n")

            print(word1 + word2.upper())
            count += 1
            output_file.writelines(word1.upper() + word2.upper() + "\n")

string_combiner()
print("{} words generated!".format(count))

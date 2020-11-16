import re


def read_content_from_file(filename):
    stream = open(filename, 'r', encoding='utf-8')
    try:
        content = stream.read()
    # print(100/0)
    finally:
        stream.close()
    return content


def get_longest_sentence(text):
    sentences = text.split(sep=".")
    print("\nYour longest sentence is:\n", max(sentences, key=len))


def get_number_of_occurrences_of_each_word(text):
    words = re.findall(r'\w+', text.lower())
    word_counter = {}
    for word in words:
        if word in word_counter:
            occurrences = word_counter[word]
            word_counter[word] = occurrences + 1
        else:
            word_counter[word] = 1
    sorted_dict = dict(sorted(word_counter.items(),
                              key=lambda item: item[1],
                              reverse=True))
    print("Let me see how many occurrences of each word we have in your text: ")
    for key, value in sorted_dict.items():
        print(key, value)


if __name__ == '__main__':
    x = read_content_from_file("../whatever.txt")
    get_number_of_occurrences_of_each_word(x)
    get_longest_sentence(x)
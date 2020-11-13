def read_content_from_file(filename):
    stream = open(filename, 'r', encoding='utf-8')
    try:
        content = stream.read()
    # print(100/0)
    finally:
        stream.close()
    return content

def getSentencesOrWords(text, sentencesOrWords):
    if sentencesOrWords:
        sentences = text.split(sep=".")
        return sentences
    else:
        words = text.lower().replace("?", "").replace(":", "").replace(";", "").replace("-", "").replace("!",
                                                                                                         "").replace(
            ".", "").replace(",", "").split(sep=" ")
        return words

def number_of_occurrences_of_each_word(words):
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
    return sorted_dict

if __name__ == '__main__':
    x = read_content_from_file("../whatever.txt")
    words = getSentencesOrWords(x, False)
    word_counterr = number_of_occurrences_of_each_word(words)
    print("Let me see how many occurrences of each word we have in your text: ")
    for key, value in word_counterr.items():
        print(key, value)
    sentences = getSentencesOrWords(x, True)
    print("\nYour longest sentence is:\n",max(sentences, key=len))
import statistics
import plotly.graph_objects as go


# distinguishes abbreviations and initials ending in periods from ends of sentences
# treats the . as a space for processing without modifying original file
def remove_dot_exceptions(text):
    exceptions = ("Mrs.", "Mr.", "Ms.", "Dr.", "Sr.", "Jr.", "St.", "A.", "B.", "C.", "D.", "E.", "F.", "G.", "H.", "I.", "J.", "K.", "L.", "M.", "O.", "P.", "Q.", "R.", "S.", "T.", "U.", "V.", "W.", "X.", "Y.", "Z.")
    edited_text = text
    for abbreviation in exceptions:
        edited_text = edited_text.replace(abbreviation, abbreviation[:-1])
    return edited_text


#removes em dashes and section break asterisks that might be counted as extra words in the sentence length
#note: removing hyphens and en dashes doesn't affect the sentence length because they will remain single words
#UNHANDLED EXCEPTION: time ranges formatted like 1900-2001 will get counted as 1 word when it should be 2.
def remove_special_chars(text):
    special_chars = ("-", "*", "_")
    edited_text = text
    for string in special_chars:
        edited_text = edited_text.replace(string, "")
    return edited_text


#splits sentences by various delimiters
def split_sentences(text):
    sentences = []
    start = 0
    i = 0
    #prev_char = ' '

    for char in text:
        # handles ignoring titles, chapter headings, page numbers
        # handles the case of how some txt formats have no space between new lines
        if char == '\n':
            start = i + 1
        if char == '\\n': # plain text formatting gets super weird sometimes
            start = i + 2

        # splits sentences by end punctiation (. or ? or !)
        if char == '.': #UNHANDLED EXCEPTIONS: leading and trailing ellipses and ex: "He said (not!)." is a single complicated sentence
            sentences.append(text[start:i + 1])
            start = i + 1

        if char == '?':
            sentences.append(text[start:i + 1])
            start = i + 2
        if char == '!':
            sentences.append(text[start:i + 1])
            start = i + 2
        i += 1
        #prev_char = char

        #print(str(i) + " and " + str(char))

    return sentences


#Counts words in a sentence by counting the number of spaces + 1
def count_words(sentence):
    word_count = 1

    for char in sentence:
        if char == ' ':
            word_count += 1

    # print("Word count is " + str(word_count))
    return word_count


#Shows basic stats including word count, sentence count, shortest and longest sentences and their lengths, mean, and standard deviation.
#Shows a line graph for sentence length over a text and histogram of sentence lengths.
def show_stats_and_graphs(all_sentences, file_name):
    min = 10000
    max = 0
    word_count = 0
    i = 0
    word_counts = []

    num_sentences = len(all_sentences)
    print(str(num_sentences) + " sentences")

    for sentence in all_sentences:
        num_words = count_words(sentence)
        word_counts.append(num_words)
        if num_words < min:
            min = all_sentences[sentence]
        if num_words > max:
            max = all_sentences[sentence]
        word_count += num_words

    print(str(word_count) + " words")

    print("\nShortest sentence(s): " + str(min) + " words")
    for sentence in all_sentences:
        if all_sentences[sentence] == min:
            print(sentence)

    print("\nLongest sentence(s): " + str(max) + " words")
    for sentence in all_sentences:
        if all_sentences[sentence] == max:
            print(sentence)

    mean = word_count / num_sentences
    print("\nAverage " + str( round(mean, 2)) + " words per sentence.")

    print("Standard deviation " + str( round(( statistics.stdev(word_counts) ), 3) ) )

    #displays bar graph of sentence lengths
    fig1 = go.Figure(
        data=[go.Scatter(y=word_counts, mode='lines', name='sentence lengths')],
        layout_title_text="Sentence lengths of " + str(file_name)
    )
    fig1.show()

    #displays histogram of sentence lengths
    fig2 = go.Figure(data=[go.Histogram(x=word_counts)])
    fig2.show()



def main():
    file = input("Enter file name: ")
    fd = open(file).read()

    # Remove punctuation that can throw off the delineators
    text = remove_dot_exceptions(fd)
    text = remove_special_chars(text)

    #Return dictionary of sentences and their word counts.
    all_sentences = split_sentences(text)
    sentence_lengths = {}
    for sentence in all_sentences:
        #print(sentence)
        sentence = sentence.lstrip() #remove leading whitespace
        sentence_lengths[sentence] = count_words(sentence)
    print(sentence_lengths)

    show_stats_and_graphs(sentence_lengths, file)




# Run program
if __name__ == '__main__':
    main()

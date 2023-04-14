from lexical_diversity import lex_div as ld
import cophi as cophi
import cophi_toolbox as cophi_toolbox
import csvreader as csvreader
import tsvtools as tsvtools
import stanfordnlp as stanfordnlp
import pycorenlp as pycorenlp
import csv
from collections import Counter
import array
import nltk
nltk.download('grammar')
import re
ttr_results = []
mtld_results = []


def read_tsv_column(filename, col):
    #this just extracts the content of every line in a specific given column of a tsv
    # #in mine the tweets are the third column of the file
    #so i call this as read_tsv_column(filename, 2)
    #then it makes them into an array of ur tweets or wtvr
    with open(filename, 'r', encoding='utf-8') as tsvfile:
        data = []
        for line in tsvfile:
            fields = line.strip().split('\t')
            if len(fields) > col:
                data.append(str(fields[col]))
    return data

def categorize_lines(filename):
    #this was to split the dail corpus into lines which were speeches and lines which were questions
    #but the function for extracting csv does it al now so im not using this one
    speeches_lines = []
    questions_lines = []

    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            if len(row) > 4 and 'speeches' in row[4]:
                speeches_lines.append(row)
            elif len(row) > 4 and 'questions' in row[4]:
                questions_lines.append(row)

    return (speeches_lines, questions_lines)

def average_sentence_length(text):
    #this takes like a single tweet or speech gets the avg sentence length
    sentences = nltk.sent_tokenize(text)
    total_words = sum(len(nltk.word_tokenize(sentence)) for sentence in sentences)
    total_sentences = len(sentences)
    avg_sentence_length = total_words / total_sentences

    return avg_sentence_length

def average_sentence_length_texts(texts):
    #yesss excellent naming going on here but like you can pass all the speeches or all the tweets or smth into this
    #and it will give you the average sentence length in all the tweets or all the speeches or wtvr
    lengths = []
    for text in texts:
       length = average_sentence_length(text)
       lengths.append(length)
    average_sentence_length_overall = (sum(lengths))/(len(lengths))
    return average_sentence_length_overall

def extract_csv_content(filename):
    #this is like made for the format my dail csv is in so u might need to change the column numberss based on urs
    #also my td only had speeches and questions but if urs has something else like answers or something
    #u might need to alter it for that idk
    speeches = []
    questions = []
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            if len(row) > 4 and 'speeches' in row[4]:
                speeches.append(row[9])
            elif len(row) > 4 and 'questions' in row[4]:
                questions.append(row[9])

    return (speeches, questions)

def calculate_average_ttr(array_of_texts):
    # takes an array of tweets or speehces or smth idk
    for elem in array_of_texts:

       # print(elem)
        pattern = r'\b(?:https?://|www\.|#|@)\S+\b'
        elem = re.sub(pattern, '', elem)
        ttr_result = ld.ttr(elem)
        ttr_results.append(ttr_result)
       # print("ttr:")
        #print(ttr_result)

    average_ttr = (sum((ttr_results)) / (len(ttr_results)))
    return average_ttr
  #  print("average of the ttr calculation for all elements:")
  #  print(average_ttr)

def calculate_average_mtld(array_of_texts):
    #takes an array of tweets or speehces or smth idk
    for elem in array_of_texts:
       # print(elem)
        pattern = r'\b(?:https?://|www\.|#|@)\S+\b'
        elem = re.sub(pattern, '', elem)
        mtld_result = ld.mtld(elem)
        mtld_results.append(mtld_result)
       # print("mtld:")
       # print(mtld_result)

    average_mtld = (sum((mtld_results)) / (len(mtld_results)))
    return average_mtld
   # print("average of the mtld calculation for all elements:")
   # print(average_mtld)

def yule(text):
    tokens = re.findall(r'\b\w+\b', text.lower())
    freqs = Counter(tokens)
    freq_of_freqs = Counter(freqs.values())
    n = len(tokens)
    sum_squared_fof = sum([i*i*f for i, f in freq_of_freqs.items()])
    k = 10000 * (sum_squared_fof - n) / (n*n)
    return k

def average_yulesk_of_texts(array_of_texts):
    yulesk_values =[]
    for text in array_of_texts:
        yulesk = yule(text)
        yulesk_values.append(yulesk)

    average = ((sum(yulesk_values)) / (len(yulesk_values)))
    return average



def calculate_wfi(text):
    #i think this might be a totally fucked up way of doing this but wtvr
    # most common words
    common_words = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "I",
                    "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
                    "this", "but", "his", "by", "from", "they", "we", "say", "her",
                    "she", "or", "an", "will", "my", "one", "all", "would", "there",
                    "their", "what", "so", "up", "out", "if", "about", "who", "get",
                    "which", "go", "me"]

    # text as list of words
    words = text.split()
    total_words = len(words)

    # frequency of each word in the text
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # sum of the frequencies of the 50 most common words
    common_word_freq = 0
    for word in common_words:
        if word in word_counts:
            common_word_freq += word_counts[word]

    # calculate the WFI
    wfi = common_word_freq / total_words
    return wfi

def average_wfi_of_texts(array_of_texts):
    wfi_values =[]
    for text in array_of_texts:
        wfi = calculate_wfi(text)
        wfi_values.append(wfi)

    average = ((sum(wfi_values)) / (len(wfi_values)))
    return average

def get_syntax_tree_height(sentence):
    # Tokenize the sentence into a list of words
    words = nltk.word_tokenize(sentence)

    # Use the NLTK parser to generate a syntax tree
    grammar = nltk.parse.load_parser('grammar:english')
    trees = list(grammar.parse(words))

    # Find the height of the tallest tree
    max_height = 0
    for tree in trees:
        height = tree.height()
        if height > max_height:
            max_height = height

    return max_height

def get_avg_syntax_tree_height(text):
    sentences = nltk.sent_tokenize(text)
    averages = []

    for sentence in sentences:
        height = get_syntax_tree_height(sentence)
        averages.append(height)

    average = ((sum(averages))/(len(averages)))
    return average

def average_syntax_tree_height_texts(array_of_texts):
    results = []
    for text in array_of_texts:
        result = get_avg_syntax_tree_height(text)
        results.append(result)

    average = ((sum(results)) / (len(results)))
    return average
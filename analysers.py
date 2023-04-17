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
from nltk.tree import Tree
import stanza
import spacy
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
    #this is broken rn but idk why
    def get_syntax_tree_height(sentence):
        nlp = stanza.Pipeline('en', processors='tokenize,mwt,pos,lemma,depparse')
        doc = nlp(sentence)

        if not doc.sentences:
            # No parse trees were returned for this sentence
            return None

        # Get the string representation of the syntax tree
        tree_str = doc.sentences[0].syntax

        if not tree_str:
            # The sentence had a parse tree, but it was empty
            return None

        # Parse the string representation into a Tree object
        try:
            tree = Tree.fromstring(tree_str)
        except ValueError:
            # The string representation was not a valid tree
            return None

        # Find the height of the tree
        height = tree.height()

        return height

def get_avg_syntax_tree_height(text):
    sentences = nltk.sent_tokenize(text)
    heights = []

    for sentence in sentences:
        height = get_syntax_tree_height(sentence)
        if height is not None:
            heights.append(height)

    if len(heights) == 0:
        return None

    average = sum(heights) / len(heights)
    return average

def average_syntax_tree_height_texts(array_of_texts):
    results = []
    for text in array_of_texts:
        result = get_avg_syntax_tree_height(text)
        if result is not None:
            results.append(result)

    if len(results) == 0:
        return None

    average = ((sum(results)) / (len(results)))
    return average


def calculate_mlcu(text):

    sentences = nltk.sent_tokenize(text)
    words = [nltk.word_tokenize(sentence) for sentence in sentences]

    num_communication_units = sum([len(nltk.sent_tokenize(sentence)) for sentence in sentences])

    num_words = sum([len(sentence) for sentence in words])

    mlcu = num_words / num_communication_units

    return mlcu

def average_mlcu_texts(array_of_texts):
    results = []
    for text in array_of_texts:
        result = calculate_mlcu(text)
        if result is not None:
            results.append(result)

    if len(results) == 0:
        return None

    average = ((sum(results)) / (len(results)))
    return average



def calculate_avg_embedded_clauses(text):
    #you might have to run python -m spacy download en_core_web_sm
    #in your terminal before this will work
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    total_embedded_clauses = 0
    total_sentences = 0
    for sentence in doc.sents:
        num_embedded_clauses = sum(1 for token in sentence if token.dep_ == "acl" or token.dep_ == "advcl")
        total_embedded_clauses += num_embedded_clauses
        total_sentences += 1
    avg_embedded_clauses = total_embedded_clauses / total_sentences

    return avg_embedded_clauses

def calculate_avg_embedded(array_of_texts):
    #this takes a whiiile im sorry
    results = []
    for text in array_of_texts:
        result = calculate_avg_embedded_clauses(text)
        if result is not None:
            results.append(result)

    if len(results) == 0:
        return None

    average = ((sum(results)) / (len(results)))
    return average

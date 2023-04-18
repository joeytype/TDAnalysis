from lexical_diversity import lex_div as ld
import csv
from collections import Counter
import numpy as np
import nltk
from nltk.tree import Tree
nltk.download('averaged_perceptron_tagger')
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

def results_sentence_length_texts(texts):
    #yesss excellent naming going on here but like you can pass all the speeches or all the tweets or smth into this
    #and it will give you the average sentence length in all the tweets or all the speeches or wtvr
    lengths = []
    for text in texts:
       length = average_sentence_length(text)
       lengths.append(length)
    return lengths


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

import nltk

def ttr_of_text(text):
    # Define regex pattern to match words starting with "@" or "http" or "#"
    pattern = r"(^|\s)[@#]?http\S+|[@#]\S+"

    # Remove words starting with "@" or "http" or "#" symbols from text
    filtered_text = re.sub(pattern, "", text)

    # Tokenize filtered text into words and calculate TTR
    words = nltk.word_tokenize(filtered_text)
    unique_words = set(words)
    ttr = len(unique_words) / len(words) if len(words) > 0 else 0
    return ttr


def results_ttr(array_of_texts):
    # takes an array of tweets or speehces or smth idk
    ttrs = []
    for text in array_of_texts:
         ttrs.append(ttr_of_text(text))
    return ttrs


def calculate_mtld(text):

    words = nltk.word_tokenize(text)
    words = [word for word in words if not (word.startswith("http") or word.startswith("@") or word.startswith("#"))]
    mtld_value = ld.mtld(words)
    return mtld_value
    print(mtld_value)

def results_mtld(array_of_texts):
    #takes an array of tweets or speehces or smth idk
    for elem in array_of_texts:
       # print(elem)
        mtld_result = calculate_mtld(elem)
        mtld_results.append(mtld_result)

    return mtld_results



def yule(text):
    tokens = re.findall(r'\b\w+\b', text.lower())
    freqs = Counter(tokens)
    freq_of_freqs = Counter(freqs.values())
    n = len(tokens)
    sum_squared_fof = sum([i*i*f for i, f in freq_of_freqs.items()])
    k = 10000 * (sum_squared_fof - n) / (n*n)
    return k

def results_yulesk_of_texts(array_of_texts):
    yulesk_values =[]
    for text in array_of_texts:
        yulesk = yule(text)
        yulesk_values.append(yulesk)

    return yulesk_values



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

def results_wfi_of_texts(array_of_texts):
    wfi_values =[]
    for text in array_of_texts:
        wfi = calculate_wfi(text)
        wfi_values.append(wfi)

    return wfi_values

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

def results_syntax_tree_height_texts(array_of_texts):
    results = []
    for text in array_of_texts:
        result = get_avg_syntax_tree_height(text)
        if result is not None:
            results.append(result)

    if len(results) == 0:
        return None

    return results


def calculate_mlcu(text):
    # Tokenize text into sentences
    sentences = nltk.sent_tokenize(text)

    # Iterate over sentences and tokenize into clause units
    clause_units = []
    for sentence in sentences:
        # Tokenize sentence into words
        words = nltk.word_tokenize(sentence)

        # Iterate over words and group into clause units
        clause_unit = []
        for i, word in enumerate(words):
            if i == 0:
                clause_unit.append(word)
            elif nltk.pos_tag([word])[0][1] in [',', ':', 'CC', 'IN']:
                # Add punctuation and conjunctions to previous clause unit
                clause_unit.append(word)
            else:
                # Start a new clause unit
                clause_units.append(clause_unit)
                clause_unit = [word]

        # Add the last clause unit in the sentence
        clause_units.append(clause_unit)

    # Calculate the total number of clause units and the total number of words
    num_clause_units = len(clause_units)
    num_words = sum(len(clause_unit) for clause_unit in clause_units)

    # Calculate the mean length of clause unit
    mlcu = num_words / num_clause_units

    return mlcu

def results_mlcu_texts(array_of_texts):
    results = []
    for text in array_of_texts:
        result = calculate_mlcu(text)
        if result is not None:
            results.append(result)

    if len(results) == 0:
        return None

    return results


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

def get_results_embedded(array_of_texts):
    #this takes a whiiile im sorry
    results = []
    for text in array_of_texts:
        result = calculate_avg_embedded_clauses(text)
        if result is not None:
            results.append(result)

    if len(results) == 0:
        return None

    return results


def stats_of_results_array(arr):
    minimum = np.min(arr)
    maximum = np.max(arr)
    mean = np.mean(arr)
    median = np.median(arr)
    std_dev = np.std(arr)

    print("Minimum: ", minimum)
    print("Maximum: ", maximum)
    print("Mean: ", mean)
    print("Median: ", median)
    print("Standard deviation: ", std_dev)
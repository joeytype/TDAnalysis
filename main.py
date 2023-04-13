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
import re
ttr_results = []
mtld_results = []


def read_tsv_column(filename, col):
    with open(filename, 'r', encoding='utf-8') as tsvfile:
        data = []
        for line in tsvfile:
            fields = line.strip().split('\t')
            if len(fields) > col:
                data.append(str(fields[col]))
    return data

def categorize_lines(filename):
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
    sentences = nltk.sent_tokenize(text)
    total_words = sum(len(nltk.word_tokenize(sentence)) for sentence in sentences)
    total_sentences = len(sentences)
    avg_sentence_length = total_words / total_sentences

    return avg_sentence_length

def extract_csv_content(filename):
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

def calculate_ttr(array_of_content):
    for elem in array_of_content:
        print(elem)
        pattern = r'http\S+'
        elem = re.sub(pattern, '', elem)
        ttr_result = ld.ttr(elem)
        ttr_results.append(ttr_result)
        print("ttr:")
        print(ttr_result)

    average_ttr = (sum((ttr_results)) / (len(ttr_results)))
    print("average of the ttr calculation for all elements:")
    print(average_ttr)

def calculate_mtld(array_of_content):
    for elem in array_of_content:
        print(elem)
        pattern = r'http\S+'
        elem = re.sub(pattern, '', elem)
        mtld_result = ld.mtld(elem)
        mtld_results.append(mtld_result)
        print("mtld:")
        print(mtld_result)

    average_mtld = (sum((mtld_results)) / (len(mtld_results)))
    print("average of the mtld calculation for all elements:")
    print(average_mtld)

def yule(text):
    # split text into tokens
    tokens = re.findall(r'\b\w+\b', text.lower())
    # count frequencies of each word
    freqs = Counter(tokens)
    # count frequencies of frequencies
    freq_of_freqs = Counter(freqs.values())
    # calculate yule's k
    n = len(tokens)
    sum_squared_fof = sum([i*i*f for i, f in freq_of_freqs.items()])
    k = 10000 * (sum_squared_fof - n) / (n*n)
    return k

(speeches, questions) = extract_csv_content("speechesBALDMAN.csv")
sm_array = read_tsv_column("TD_Darren O'Rourke_SocialMediaCorpus.tsv", 2)










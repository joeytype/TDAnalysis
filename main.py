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
import analysers as a

#this literally just prints all the results lol sorry if its messy
#also again my dail corpus only has speeches and questions so if urs has more u need to allow for that

(speeches, questions) = a.extract_csv_content("speechesBALDMAN.csv")
tweets = a.read_tsv_column("TD_Darren O'Rourke_SocialMediaCorpus.tsv", 2)

#ttr
print("average ttr of tweets corpus:")
print(a.calculate_average_ttr(tweets))

print("average ttr of speeches corpus:")
print(a.calculate_average_ttr(speeches))

print("average ttr of questions corpus:")
print(a.calculate_average_ttr(questions))

#mtld
print("average mtld of tweets corpus:")
print(a.calculate_average_mtld(tweets))

print("average mtld of speeches corpus:")
print(a.calculate_average_mtld(speeches))

print("average mtld of questions corpus:")
print(a.calculate_average_mtld(questions))

#sentence length
print("average sentence length of tweets corpus:")
print(a.average_sentence_length_texts(tweets))

print("average sentence length of speeches corpus:")
print(a.average_sentence_length_texts(speeches))

print("average sentence length of questions corpus:")
print(a.average_sentence_length_texts(questions))

#yules k
print("average yules k of tweets corpus:")
print(a.average_yulesk_of_texts(tweets))

print("average yules k of speeches corpus:")
print(a.average_yulesk_of_texts(speeches))

print("average yules k of questions corpus:")
print(a.average_yulesk_of_texts(questions))

#wfi
print("average wfi of tweets corpus:")
print(a.average_wfi_of_texts(tweets))

print("average wfi of speeches corpus:")
print(a.average_wfi_of_texts(speeches))

print("average wfi of questions corpus:")
print(a.average_wfi_of_texts(questions))

#syntax tree height BROKEN RN LOL SORRY IT ALWAYS RETURNS NONE OOPSIES
print("average syntax tree height of tweets corpus:")
print(a.average_syntax_tree_height_texts(tweets))

print("average syntax tree height of speeches corpus:")
print(a.average_syntax_tree_height_texts(speeches))

print("average syntax tree height of questions corpus:")
print(a.average_syntax_tree_height_texts(questions))
###











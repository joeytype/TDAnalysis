import analysers as a
import stats as s

#this literally just prints all the results lol sorry if its messy
#also again my dail corpus only has speeches and questions so if urs has more u need to allow for that
#
(speeches, questions) = a.extract_csv_content("speechesBALDMAN.csv")
dail_utterances = speeches + questions
tweets = a.read_tsv_column("TD_Darren O'Rourke_SocialMediaCorpus.tsv", 2)

choice = input("Input 1 to get your measure results, 2 to get your stat test results")

if choice == 1:
    print(
        "These are calculated using the average for each entry in each corpus. For example the maximum sentence \n length is the maximum AVERAGE sentence length of an entry in that corpus")
    ###lexical complexity
    print("**MEASURES OF LEXICAL COMPLEXITY/DIVERSITY**")
    # ttr

    print("\n")
    print("TTR tweets corpus:")
    print(a.stats_of_results_array(a.results_ttr(tweets)))
    print("\n")
    print("TTR speeches corpus:")
    print(a.stats_of_results_array(a.results_ttr(speeches)))
    print("\n")
    print("TTR questions corpus:")
    print(a.stats_of_results_array(a.results_ttr(questions)))
    print("\n")
    print("TTR dail as a whole:")
    print(a.stats_of_results_array(a.results_ttr(dail_utterances)))
    print("\n")
    # mtld

    print("MTLD tweets corpus:")
    print(a.stats_of_results_array(a.results_mtld(tweets)))
    print("\n")
    print("MTLD speeches corpus:")
    print(a.stats_of_results_array(a.results_mtld(speeches)))
    print("\n")
    print("MTLD questions corpus:")
    print(a.stats_of_results_array(a.results_mtld(questions)))
    print("\n")
    print("MTLD dail as a whole:")
    print(a.stats_of_results_array(a.results_mtld(dail_utterances)))
    print("\n")

    # yules k
    print("Yules K tweets corpus:")
    print(a.stats_of_results_array(a.results_yulesk_of_texts(tweets)))
    print("\n")
    print("Yules K speeches corpus:")
    print(a.stats_of_results_array(a.results_yulesk_of_texts(speeches)))
    print("\n")
    print("Yules K questions corpus:")
    print(a.stats_of_results_array(a.results_yulesk_of_texts(questions)))
    print("\n")
    print("Yules K dail as a whole:")
    print(a.stats_of_results_array(a.results_yulesk_of_texts(dail_utterances)))
    print("\n")

    # wfi
    print("WFI tweets corpus:")
    print(a.stats_of_results_array(a.results_wfi_of_texts(tweets)))
    print("\n")
    print("WFI speeches corpus:")
    print(a.stats_of_results_array(a.results_wfi_of_texts(speeches)))
    print("\n")
    print("WFI of questions corpus:")
    print(a.stats_of_results_array(a.results_wfi_of_texts(questions)))
    print("\n")
    print("WFI dail as a whole:")
    print(a.stats_of_results_array(a.results_wfi_of_texts(dail_utterances)))
    print("\n")
    ##structural complexity
    print("***MEASURES OF STRUCTURAL COMPLEXITY***")
    print("\n")
    # sentence length
    print("sentence length tweets corpus:")
    print(a.stats_of_results_array(a.results_sentence_length_texts(tweets)))
    print("\n")
    print("sentence length speeches corpus:")
    print(a.stats_of_results_array(a.results_sentence_length_texts(speeches)))
    print("\n")
    print("sentence length questions corpus:")
    print(a.stats_of_results_array(a.results_sentence_length_texts(questions)))
    print("\n")
    print("sentence length dail as a whole:")
    print(a.stats_of_results_array(a.results_sentence_length_texts(dail_utterances)))
    print("\n")

    # mlcu
    print("MLCU tweets corpus:")
    print(a.stats_of_results_array(a.results_mlcu_texts(tweets)))
    print("\n")
    print("MLCU speeches corpus:")
    print(a.stats_of_results_array(a.results_mlcu_texts(speeches)))
    print("\n")
    print("MLCU questions corpus:")
    print(a.stats_of_results_array(a.results_mlcu_texts(questions)))
    print("\n")
    print("MLCU dail as a whole:")
    print(a.stats_of_results_array(a.results_mlcu_texts(dail_utterances)))
    print("\n")

    # average number of embedded clauses
    print("embedded clauses tweets corpus:")
    print(a.stats_of_results_array(a.get_results_embedded(tweets)))
    print("\n")
    print("embedded clauses speeches corpus:")
    print(a.stats_of_results_array(a.get_results_embedded(speeches)))
    print("\n")
    print("embedded clauses questions corpus:")
    print(a.stats_of_results_array(a.get_results_embedded(questions)))
    print("\n")
    print("embedded clauses dail as a whole:")
    print(a.stats_of_results_array(a.get_results_embedded(dail_utterances)))
    print("\n")

    # syntax tree height BROKEN RN LOL SORRY IT ALWAYS RETURNS NONE OOPSIES
    print("syntax tree height tweets corpus:")
    print(a.stats_of_results_array(a.results_syntax_tree_height_texts(tweets)))
    print("\n")
    print("syntax tree height speeches corpus:")
    print(a.stats_of_results_array(a.results_syntax_tree_height_texts(speeches)))
    print("\n")
    print("syntax tree height questions corpus:")
    print(a.stats_of_results_array(a.results_syntax_tree_height_texts(questions)))
    print("\n")
    print("syntax tree height dail as a whole:")
    print(a.stats_of_results_array(a.results_syntax_tree_height_texts(dail_utterances)))
    print("\n")
    ###

else:
    print("time for some statistics!")
    dail_ttrs = a.results_ttr(dail_utterances)
    twitter_ttrs = a.results_ttr(tweets)

    dail_mtlds = a.results_mtld(dail_utterances)
    twitter_mtlds = a.results_mtld(tweets)

    dail_yulesks = a.results_yulesk_of_texts(dail_utterances)
    twitter_yulesks = a.results_yulesk_of_texts(tweets)

    dail_wfis = a.results_wfi_of_texts(dail_utterances)
    twitter_wfis = a.results_wfi_of_texts(tweets)

    dail_sentencelengths = a.results_sentence_length_texts(dail_utterances)
    twitter_sentencelengths = a.results_sentence_length_texts(tweets)

    dail_mlcus = a.results_mlcu_texts(dail_utterances)
    twitter_mlcus = a.results_mlcu_texts(tweets)

    dail_embeddeds = a.get_results_embedded(dail_utterances)
    twitter_embeddeds = a.get_results_embedded(tweets)


    print("KRUSKAL WALLACE TEST COMPARING DAIL AND TWEETS")
    print("TTR")
    s.kruskal_wallis_test(dail_ttrs, twitter_ttrs)

    print("\n MTLD")
    s.kruskal_wallis_test(dail_mtlds, twitter_mtlds)

    print("\n Yule's K")
    s.kruskal_wallis_test(dail_yulesks, twitter_yulesks)

    print("\n WFI")
    s.kruskal_wallis_test(dail_wfis, twitter_wfis)

    print("\n Sentence Lengths")
    s.kruskal_wallis_test(dail_sentencelengths, twitter_sentencelengths)

    print("\n MLCU")
    s.kruskal_wallis_test(dail_mlcus, twitter_mlcus)

    print("\n Embedded Clauses")
    s.kruskal_wallis_test(dail_embeddeds, twitter_embeddeds)

    "\n MANN WHITNEY U TEST COMPARING DAIL AND TWEETS"
    print("TTR")
    s.mann_whitney_u(dail_ttrs, twitter_ttrs)

    print("\n MTLD")
    s.mann_whitney_u(dail_mtlds, twitter_mtlds)

    print("\n Yule's K")
    s.mann_whitney_u(dail_yulesks, twitter_yulesks)

    print("\n WFI")
    s.mann_whitney_u(dail_wfis, twitter_wfis)

    print("\n Sentence Lengths")
    s.mann_whitney_u(dail_sentencelengths, twitter_sentencelengths)

    print("\n MLCU")
    s.mann_whitney_u(dail_mlcus, twitter_mlcus)

    print("\n Embedded Clauses")
    s.mann_whitney_u(dail_embeddeds, twitter_embeddeds)

    print("\n AND T TEST FOR THE MEAN OF EACH MEASURE IN EACH SAMPLE!")

    print("TTR")
    s.t_test(dail_ttrs, twitter_ttrs)

    print("\n MTLD")
    s.t_test(dail_mtlds, twitter_mtlds)

    print("\n Yule's K")
    s.t_test(dail_yulesks, twitter_yulesks)

    print("\n WFI")
    s.t_test(dail_wfis, twitter_wfis)

    print("\n Sentence Lengths")
    s.t_test(dail_sentencelengths, twitter_sentencelengths)

    print("\n MLCU")
    s.t_test(dail_mlcus, twitter_mlcus)

    print("\n Embedded Clauses")
    s.t_test(dail_embeddeds, twitter_embeddeds)














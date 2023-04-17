import scipy.stats as stats


def kruskal_wallis_test(corpus1, corpus2):
    """
    Conducts Kruskal-Wallis test on two arrays of values and returns the test statistic and p-value.
    """
    h_statistic, p_value = stats.kruskal(corpus1, corpus2)

    # Print the results
    print("Kruskal-Wallis test results:")
    print(f"H-statistic: {h_statistic:.4f}")
    print(f"p-value: {p_value:.4f}")

    if p_value < 0.05:
        print("There is a statistically significant difference between the two samples at the 0.05 level.")
    else:
        print("There is not a statistically significant difference between the two samples at the 0.05 level.")

    return h_statistic, p_value



def mann_whitney_u(corpus1, corpus2):
    # Calculate the Mann-Whitney U test, pass it a list of values for ur corpora
    u_statistic, p_value = stats.mannwhitneyu(corpus1, corpus2, alternative='two-sided')

    # Print the test results
    print("Mann-Whitney U test results:")
    print(f"U statistic: {u_statistic}")
    print(f"p-value: {p_value}")
    if p_value < 0.05:
        print("There is a significant difference between the two samples.")
    else:
        print("There is no significant difference between the two samples.")



def t_test(values1, values2):
    #this now takes arrays like the other ones hehe
    # Calculate the sample means
    mean1 = sum(values1) / len(values1)
    mean2 = sum(values2) / len(values2)

    # Define the sample sizes
    n1 = len(values1)
    n2 = len(values2)

    # Calculate the sample standard deviations
    sd1 = stats.tstd(values1)
    sd2 = stats.tstd(values2)

    # Calculate the t-statistic and p-value
    t_statistic, p_value = stats.ttest_ind_from_stats(mean1, sd1, n1, mean2, sd2, n2)

    # Print the results
    print("T-test results:")
    print(f"t-statistic: {t_statistic}")
    print(f"p-value: {p_value}")
    if p_value < 0.05:
        print("The difference in means is statistically significant.")
    else:
        print("The difference in means is not statistically significant.")

import scipy.stats as stats

def kruskal_wallis_test(corpus1, corpus2):
    """
    Conducts Kruskal-Wallis test on two arrays of values and returns the test statistic and p-value.
    """
    h_statistic, p_value = stats.kruskal(corpus1, corpus2)
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



def seqAlignment(seq1, seq2, scoring_matrix):
    # Lengths of the sequences
    m, n = len(seq1), len(seq2)

    # Initialize the DP matrix
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Initialize the first row and column with gap penalties
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] + scoring_matrix[seq1[i - 1]]['-']
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] + scoring_matrix['-'][seq2[j - 1]]

    # Fill the DP matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = dp[i - 1][j - 1] + scoring_matrix[seq1[i - 1]][seq2[j - 1]]
            delete = dp[i - 1][j] + scoring_matrix[seq1[i - 1]]['-']
            insert = dp[i][j - 1] + scoring_matrix['-'][seq2[j - 1]]
            dp[i][j] = max(match, delete, insert)

    # Traceback to find the optimal alignment
    align1, align2 = "", ""
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + scoring_matrix[seq1[i - 1]][seq2[j - 1]]:
            align1 = seq1[i - 1] + align1
            align2 = seq2[j - 1] + align2
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + scoring_matrix[seq1[i - 1]]['-']:
            align1 = seq1[i - 1] + align1
            align2 = "-" + align2
            i -= 1
        else:
            align1 = "-" + align1
            align2 = seq2[j - 1] + align2
            j -= 1

    return align1, align2

# Updated scoring matrix and sequences
scoring_matrix = {
    'A': {'A': 1, 'G': -0.8, 'T': -0.2, 'C': -2.3, '-': -0.6},
    'G': {'A': -0.8, 'G': 1, 'T': -1.1, 'C': -0.7, '-': -1.5},
    'T': {'A': -0.2, 'G': -1.1, 'T': 1, 'C': -0.5, '-': -0.9},
    'C': {'A': -2.3, 'G': -0.7, 'T': -0.5, 'C': 1, '-': -1},
    '-': {'A': -0.6, 'G': -1.5, 'T': -0.9, 'C': -1, '-': 0}
}
seq1 = "ATGCC"
seq2 = "TACGCA"


print(seqAlignment(seq1, seq2, scoring_matrix))
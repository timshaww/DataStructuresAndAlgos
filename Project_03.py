def longest_common_subsequence(seq1, seq2):
    m, n = len(seq1), len(seq2)
    table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

            print(f"Table after updating cell [{i}][{j}]:")
            print_table(table)
            print("\n")

    lcs = construct_lcs(seq1, seq2, table)
    return lcs

def print_table(table):
    for row in table:
        print(row)

def construct_lcs(seq1, seq2, table):
    i, j = len(seq1), len(seq2)
    lcs = []

    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            lcs.append(seq1[i - 1])
            i -= 1
            j -= 1
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))

seq1 = "AGGTAB"
seq2 = "GGTATA"

lcs_length = longest_common_subsequence(seq1, seq2)
print("Longest Common Subsequence: " + lcs_length)
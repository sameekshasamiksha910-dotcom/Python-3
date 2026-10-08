def lcs(a, b):
    m, n = len(a), len(b)

    # DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct LCS
    i, j = m, n
    result = []

    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            result.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], ''.join(reversed(result))


# Main program
if __name__ == "__main__":
    a = input("Enter first sequence: ")
    b = input("Enter second sequence: ")

    length, sequence = lcs(a, b)

    print("LCS Length:", length)
    print("LCS:", sequence)
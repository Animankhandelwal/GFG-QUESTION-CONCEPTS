public class longestCommonSub {
    public int longestCommonSubstr(String s1, String s2) {
        // Find length of both strings.
        int m = s1.length();
        int n = s2.length();
        // Variable to store length of longest
        // common substring.
        int result = 0;
        // Matrix to store result of two
        // consecutive rows at a time.
        int[][] dp = new int[2][n + 1];
        // Variable to represent which row of
        // matrix is current row.
        int currRow = 0;
        // For a particular value of i and j,
        // dp[currRow][j] stores length of longest
        // common substring in string X[0..i] and Y[0..j].
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == 0 || j == 0) {
                    dp[currRow][j] = 0;
                } else if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    dp[currRow][j] = dp[1 - currRow][j - 1] + 1;
                    result = Math.max(result, dp[currRow][j]);
                } else {
                    dp[currRow][j] = 0;
                }
            }
            // Make current row as previous row and previous
            // row as new current row.
            currRow = 1 - currRow;
        }
        return result;
    }
}

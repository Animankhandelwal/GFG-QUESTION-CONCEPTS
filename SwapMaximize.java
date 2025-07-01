import java.util.*;
public class SwapMaximize {
    public long maxSum(Long[] arr) {
        // code here
        long sum = 0;
        int n=arr.length;
        // Sorting the array.
        Arrays.sort(arr);
        for (int i = 0; i < n/2; i++)
        {
            sum -= (2 * arr[i]);
            sum += (2 * arr[n - i - 1]);
        }
        return sum;
    }
}

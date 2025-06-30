import java.util.*;
public class SubsetSum {
        int minSubset(int[] arr) {
        // code here
        int halfSum = 0;
        int n=arr.length;
        for (int i = 0; i < n; i++)
            halfSum = halfSum + arr[i];
        halfSum = halfSum / 2;
        Arrays.sort(arr);

        int res = 0, curr_sum = 0;
        for (int i = n - 1; i >= 0; i--) {

            curr_sum += arr[i];
            res++;
            if (curr_sum > halfSum)
                return res;
        }
        return res;
    }
}

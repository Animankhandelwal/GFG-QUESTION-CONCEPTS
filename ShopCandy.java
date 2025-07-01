import java.util.ArrayList;
import java.util.Arrays;
public class ShopCandy {
    static ArrayList<Integer> candyStore(int candies[], int N, int K) {
        // code here
        ArrayList<Integer> lst = new ArrayList<>();
        Arrays.sort(candies);

        int min = 0, max = 0;
        int i = 0, j = N - 1;

        // Calculate minimum candies
        int n = N; // Copy of original N
        while (i < n) {
            min += candies[i];
            i++;
            n -= K;
        }

        // Reset i and j for maximum calculation
        i = 0;
        j = N - 1;

        // Calculate maximum candies
        int m = N;
        while (j >= i) {
            max += candies[j];
            j--;
            i += K;
        }

        lst.add(min);
        lst.add(max);
        return lst;
    }
}

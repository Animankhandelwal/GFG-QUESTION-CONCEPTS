import java.util.PriorityQueue;
public class Activity {
    public int activitySelection(int[] start, int[] finish) {
        // code here
        int n = start.length;
        int ans = 0;

        PriorityQueue<int[]> p = new PriorityQueue<>(
            (a, b) -> Integer.compare(a[0], b[0]));

        for (int i = 0; i < n; i++) {
            p.add(new int[] { finish[i], start[i] });
        }
        int finishtime = -1;

        while (!p.isEmpty()) {
            int[] activity
                = p.poll(); // Extract the activity with the
                            // smallest finish time
            if (activity[1] > finishtime) {
                finishtime = activity[0];
                ans++;
            }
        }
        return ans;
    }
}

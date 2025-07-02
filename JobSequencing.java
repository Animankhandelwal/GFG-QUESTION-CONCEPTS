import java.util.*;
public class JobSequencing {

    public ArrayList<Integer> jobSequencing(int[] deadline, int[] profit) {
        // Find the length of the deadline
        int n=deadline.length;
        ArrayList<Integer> ans = new ArrayList<>(Arrays.asList(0, 0));
        // Now creating a pair for the deadline profit which will be sorted based on deadline
        List<int[]> jobs=new ArrayList<>();
        for(int i=0;i<n;i++){
            jobs.add(new int[]{deadline[i],profit[i]});
        }
        // Now sorting the list based on deadline
        jobs.sort(Comparator.comparingInt(a->a[0]));
        PriorityQueue<Integer> pq=new PriorityQueue<>();
        for(int[] job:jobs){
            if(job[0]>pq.size()){
                pq.add(job[1]);
            }
            // replace the job with the lowest profit 
            else if(!pq.isEmpty() && pq.peek()<job[1]){
                pq.poll();
                pq.add(job[1]);
            }
        }
        while (!pq.isEmpty()) {
            ans.set(1, ans.get(1) + pq.poll());
            ans.set(0, ans.get(0) + 1);
        }
        return ans;
    }
}

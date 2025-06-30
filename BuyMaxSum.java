import java.util.*;
class BuyMaxSum {
    public static int buyMaximumProducts(int n, int k, int[] price) {
        // code here
        Pair[] arr=new Pair[n];
        // arranging the pair according to the (stock price,day)
        for(int i=0;i<n;i++){
            arr[i]=new Pair(price[i],i+1);
        }
        
        Arrays.sort(arr,new SortPair());
        int ans=0;
        for(int i=0;i<n;i++){
            ans+=Math.min(arr[i].second,k/arr[i].first);
            k-=arr[i].first*Math.min(arr[i].second,k/arr[i].first);
        }
        return ans;
    }
}
class Pair {
    int first, second;
    Pair(int first, int second)
    {
        this.first = first;
        this.second = second;
    }
}

class SortPair implements Comparator<Pair> {
    public int compare(Pair a, Pair b)
    {
        return a.first - b.first;
    }
}
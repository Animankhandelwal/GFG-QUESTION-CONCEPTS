# CONCEPTS FOR CODING PRACTICE

## SMALLEST SUBSET SUM
### Concept:
The idea to solve this problem is based on the greedy approach that we pick the largest elements to form the subset having sum greater than all others. We first sort the array in reverse order. Then we traverse the sorted array from the left (largest element) and compute sum of elements. If sum of current elements become more than the remaining sum, we return count of current elements as result.

### Time Complexity:
O(nlogn)

## BUY MAX SUM:
### Concept:
The idea is to use greedy approach, where we should start buying product from the day when the stock price is least and so on. 
So, we will sort the pair of two values i.e { stock price, day } according to the stock price, and if stock prices are same, then we sort according to the day. 
Now, we will traverse along the sorted list of pairs, and start buying as follows: 
Let say, we have R rs remaining till now, and the cost of product on this day be C, and we can buy atmost L products on this day then, 
total purchase on this day (P) = min(L, R/C) 
Now, add this value to the answer 
total_purchase = total_purchase + P, where P =min(L, R/C) 
Now, subtract the cost of buying P items from remaining money, R = R - P*C. 
Total number of products that we can buy is equal to total_purchase.

### Time Complexity:
O(nlogn)

### New Concepts Learnt:
Making the new class as Pair which is using the constructors to declare the first and second element
Then making another class called the SortPair which is a comparator for the first elements of the two pairs being compared to get the optimal answer

## SWAP MAXIMIZE:
### Concept:
We need to arrange the elements of the array in such a way that the difference of the consecutive elements has to be maximum.

So first we sort the array, then subtract the numbers as follow the following pattern:
(a1-an), (a2,an-1) and so on.
We will notice that the sum of the elements becomes twice.

### Time Complexity:
O(nlogn)

## Shop in Candy Store:
### Time Compplexity:
O(nlogn)

## Minimum Fibonacci
### the numbers can be expressed as the sum of their fibonacci series and ths is called Zeckendorf's Theorem.
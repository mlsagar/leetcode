Solution Article
We need to find out the maximum difference (which will be the maximum profit) between two numbers in the given array. Also, the second number (selling price) must be larger than the first one (buying price).

In formal terms, we need to find max(prices[j]−prices[i]), for every i and j such that j>i.

Approach 1: Brute Force

Complexity Analysis
Time complexity: O(n 
2
 ). Loop runs  
2
n(n−1)
​
  times.

Space complexity: O(1). Only two variables - maxprofit and profit are used.

Approach 2: One Pass
Algorithm
Say the given array is:

[7, 1, 5, 3, 6, 4]
If we plot the numbers of the given array on a graph, we get:

Profit Graph

The points of interest are the peaks and valleys in the given graph. We need to find the largest price following each valley, which difference could be the max profit.
We can maintain two variables - minprice and maxprofit corresponding to the smallest valley and maximum profit (maximum difference between selling price and minprice) obtained so far respectively.


Complexity Analysis
Time complexity: O(n). Only a single pass is needed.

Space complexity: O(1). Only two variables are used.

Problem Set 1 review

1) Set Matrix to 0s
```
STEPS
1) Make two functions markRow and markCol
2) If the element is not 0 then mark it a distinct number in the two functions
3) Traverse through the matrix and if 0 is encountered invoke the two functions
4) Now travserse through the entire matrix, if you see the distinct number change it to 0
5) Print the matrix
```

2) Pascal's Triangle
```
STEPS
1) 
```

3) Next Permutation
```
STEPS
1) Find the breaking point index (A[i]<A[i+1])
2) If there is no breaking point just reverse the array
3) Start from the last index and traverse backwards till the index
4) if (A[i] > A[i+1]) swap A[i] and A[index]
5) reverse(A.begin()+ind+1,A.end()) // reverse from the next of index till end
```

4) Maximum Subarray
```
1) Make a variable and declare it to INT_MIN (maxi)
2) run i loop from 0 to size
3) run j loop from 0 to size
4) run k loop from i to j
5) inside k loop add the numbers
6) outside k loop maxi=max(maxi,sum)
```

5) Sort Colors
```
1) Buble Sort (Brute force)
2) only 0s 1s and 2s so count them and then in the array add them accordingly
3) Dutch National Flag Algorithm
```

6) Best time to Buy and Sell Stock
```
1) Make a minPrice and set it as INT_MAX
2) Make a profit variable
3) Iterate through the entire list once
4) minPrice=min(prices[i],minPrice)
5) profit=max(profit,prices[i]-minPrice)
6) return profit
```

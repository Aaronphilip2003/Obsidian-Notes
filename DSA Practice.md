STL Functions [[STL Functions]]
Go to [[DSA Notes]] for main points

1. 
![[Pasted image 20230822215707.png]]

Solution:

```cpp
class Solution {
public:
    void markRow(int i, vector<vector<int>>& matrix) {
        int col = matrix[0].size();
	        for (int j = 0; j < col; j++) {
            if (matrix[i][j] != 0) {
                matrix[i][j] = -999;  // Use a distinct value to mark
            }
        }
    }
    void markCol(int j, vector<vector<int>>& matrix) {
        int rows = matrix.size();
        for (int i = 0; i < rows; i++) {
            if (matrix[i][j] != 0) {
                matrix[i][j] = -999;  // Use a distinct value to mark
            }
        }
    }

    void setZeroes(vector<vector<int>>& matrix) {
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[i].size(); j++) {
                if (matrix[i][j] == 0) {
                    markRow(i, matrix);
                    markCol(j, matrix);
                }
            }
        }
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[i].size(); j++) {
                if (matrix[i][j] == -999) {  // Replace distinct value with 0
                    matrix[i][j] = 0;
                }
            }
        }
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[i].size(); j++) {
                cout << matrix[i][j] << " ";
            }
            cout << endl;
        }
    }
};
```

The idea is wherever you see a 0, mark all the non zero elements of that row and column with a distinct number
then in the final print wherever you see that distinct number make it 0

2. 
![[Pasted image 20231024192140.png]]

1) Given the row number and column number, print the element 
	- Formula = <sup>(R-1)</sup> C <sub>(C-1)</sub>

Shortcut to find Combinations
![[Pasted image 20231024192553.png]]
![[Pasted image 20231024192700.png]]

2)  Print any nth row of pascals triangle
	- nth row will ALWAYS have n elements
![[Pasted image 20231024192910.png]]
![[Pasted image 20231024193628.png]]


3) Given N print the entire pascal's triangle
![[Pasted image 20231024194802.png]]
3. 
![[Pasted image 20231025215424.png]]

![[Pasted image 20231025215448.png]]

Steps to find next permutation : 
1) find the breaking point in the array ( arr[i] < arr[i+1])
2) start from the last element and find the smallest one
3) place the remaining elements in sorted order

```cpp
class Solution {
public:
    vector<int> nextPermutation(vector<int>& A) {
        int ind=-1;
        int n=A.size();
        for(int i=n-2;i>=0;i--)
        {
            if(A[i] < A[i+1])
            {
                ind=i;
                break;
            }
        }
        if(ind==-1)
        {
            reverse(A.begin(),A.end());
            return A;
        }
        for(int i=n-1;i>ind;i--)
        {
            if(A[i]>A[ind])
            {
                swap(A[i],A[ind]);
                break;
            }
        }
        reverse(A.begin()+ind+1,A.end());
        return A;
    }
};
```

4. 
![[Pasted image 20231026085505.png]]

1) Brute force Approach
```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxi=INT_MIN;
        for(int i=0;i<nums.size();i++)
        {
            for(int j=i;j<nums.size();j++)
            {
                int sum=0;
                for(int k=i;k<=j;k++)
                {
                    sum+=nums[k];
                }
                maxi=max(maxi,sum);
            }
        }
        return maxi;
    }
};
```

5. ![[Pasted image 20231027090700.png]]
Method 1:
Brute force, I used Bubble sort

```cpp
class Solution {
public:
    void sortColors(vector<int>& nums) {
        for(int i=0;i<nums.size();i++)
        {
            int temp=0;
            for(int j=0;j<nums.size()-i-1;j++)
            {
                if(nums[j]>nums[j+1])
                {
                    temp=nums[j];
                    nums[j]=nums[j+1];
                    nums[j+1]=temp;
                }
            }
        }
    }
};
```
![[Pasted image 20231027144715.png]]

Method 2:
We know that we have only 0s 1s and 2s 
So we can just count the number of 0s 1s and 2s and just print it in order

```cpp
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int count0=0;
        int count1=0;
        int count2=0;
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]==0)
                count0++;
            else if(nums[i]==1)
                count1++;
            else if(nums[i]==2)
                count2++;
        }
        for(int i=0;i<count0;i++)
        {
            nums[i]=0;
        }
        for(int i=count0;i<count0+count1;i++)
        {
            nums[i]=1;
        }
        for(int i=count0+count1;i<count0+count1+count2;i++)
        {
            nums[i]=2;
        }
    }
};
```
![[Pasted image 20231027184706.png]]

Method 3: Dutch National Flag Algorithm
![[Pasted image 20231027185500.png]]
![[Pasted image 20231027190026.png]]
```cpp
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int low=0,mid=0,high=nums.size()-1;
        while(mid<=high)
        {
            if(nums[mid]==0)
            {
                swap(nums[low],nums[mid]);
                low++;
                mid++;
            }
            else if(nums[mid]==1)
            {
                mid++;
            }
            else
            {
                swap(nums[mid],nums[high]);
                high--;
            }
        }
    }
};
```
![[Pasted image 20231027191211.png]]

6. ![[Pasted image 20231028132345.png]]

Method 1: Brute Force (Exceeds time limit)
```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_=INT_MIN;
        for(int i=0;i<prices.size();i++)
        {
            for(int j=i+1;j<prices.size();j++)
            {
                int temp_max=0;
                if(prices[j]-prices[i]>0)
                {
                    temp_max=prices[j]-prices[i];
                }
            if(temp_max>max_)
            {
                max_=temp_max;
            }
            }
        }
        if (max_==INT_MIN)
        {
            return 0;
        }
        return max_;
    }
};
```

Method 2: One pass solution

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit=0;
        int minPrice=INT_MAX;
        for(int i=0;i<prices.size();i++)
        {
            minPrice=min(minPrice,prices[i]);
            profit=max(profit,prices[i]-minPrice);
        }
        return profit;
    }
};
```
f
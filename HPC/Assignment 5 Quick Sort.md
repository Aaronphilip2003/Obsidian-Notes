## CODE

```c
#include <iostream>
#include <vector>
#include <omp.h>
using namespace std;
void quicksort(vector<int>& arr, int low, int high);
int main() {
    vector<int> arr = {12, 5, 23, 1, 6, 9, 15, 2, 10};
    int size = arr.size();
    cout << "Original array:" << endl;
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    #pragma omp parallel
    {
        #pragma omp single nowait
        {
            quicksort(arr, 0, size - 1);
        }
    }

    cout << "Sorted array:" << endl;
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}

void quicksort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr[i], arr[j]);
            }
        }
        swap(arr[i + 1], arr[high]);
        int pi = i + 1;

        #pragma omp task shared(arr)
        {
            quicksort(arr, low, pi - 1);
        }
        #pragma omp task shared(arr)
        {
            quicksort(arr, pi + 1, high);
        }
    }
}


```


## Time taken to sort

| Sr No. | Data Points | Time taken for Serial Bubble Sort | Time taken for Parallel Bubble Sort |
| ------ | ----------- | --------------------------------- | ----------------------------------- |
| 1      | 500         | 0.0025 seconds                    | 0.0010 seconds                      |
| 2      | 1000        | 0.0052 seconds                    | 0.0030 seconds                      |
| 3      | 10000       | 0.0528 seconds                    | 0.0143 seconds                      |
| 4      | 30000       | 0.1584 seconds                    | 0.0400 seconds                      |
| 5      | 50000       | 0.2661 seconds                    | 0.0602 seconds                      |
| 6      | 70000       | 0.3789 seconds                    | 0.0793 seconds                      |
| 7      | 100000      | 0.5423 seconds                    | 0.1097 seconds                      |

![[Pasted image 20240423172657.png]]


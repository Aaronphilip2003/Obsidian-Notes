
## CODE
```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>
#include <string.h>

void displayMenu(void);
void init_array(int[], int);
void display_array(int[], int);
void merge(int[], int, int, int);
void mergeSort_serial(int[], int, int);
void mergeSort_parallel(int[], int, int);
void initializeBest(int[], int);
void initializeWorst(int[], int);
#define max 100000 // Maximum array size
int main(void) {
    int Array[max];
    int choice = -9;
    int alreadyInitialized = 0;
    int size;
    int OriginalArray[max]; // Array to store the original unsorted values
    while (1) {
        displayMenu();
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                printf("\nEnter the size of the array: ");
                scanf("%d", &size);
                if (size <= 0 || size > max) {
                    printf("\nInvalid size. Size should be between 1 and %d.\n", max);
                    continue;
                }
                init_array(Array, size);
                memcpy(OriginalArray, Array, size * sizeof(int)); // Make a copy of the original array

                alreadyInitialized = 1;
                printf("\n|  The array is initialized to:");
                display_array(Array, size);
                break;
            case 2:
                if (alreadyInitialized == 0) {
                    printf("\nArray not initialized. Please initialize the array first.\n");
                    break;
                }
                printf("\n|  The array contents are:");
                display_array(Array, size);
                break;
            case 3:
                if (alreadyInitialized == 0) {
                    printf("\nArray not initialized. Please initialize the array first.\n");
                    break;
                }
                {
                    double start_time = omp_get_wtime();
                    mergeSort_serial(OriginalArray, 0, size - 1); // Sort the original unsorted array
                    double end_time = omp_get_wtime();
                    printf("\nSerial Sorting Time: %f seconds\n", end_time - start_time);
                }
                break;
            case 4:
                if (alreadyInitialized == 0) {
                    printf("\nArray not initialized. Please initialize the array first.\n");
                    break;
                }
                {
                    double start_time = omp_get_wtime();
                    mergeSort_parallel(OriginalArray, 0, size - 1);
                    double end_time = omp_get_wtime();
                    printf("\nParallel Sorting Time: %f seconds\n", end_time - start_time);
                }
                break;
            case 5:
                printf("\nEnter the size of the array: ");
                scanf("%d", &size);
                if (size <= 0 || size > max) {
                    printf("\nInvalid size. Size should be between 1 and %d.\n", max);
                    continue;
                }
                initializeBest(Array, size);
                memcpy(OriginalArray, Array, size * sizeof(int)); // Make a copy of the original array
                alreadyInitialized = 1;
                printf("\n|  The array is initialized to:");
                display_array(Array, size);
                break;
            case 6:
                printf("\nEnter the size of the array: ");
                scanf("%d", &size);
                if (size <= 0 || size > max) {
                    printf("\nInvalid size. Size should be between 1 and %d.\n", max);
                    continue;
                }
                initializeWorst(Array, size);
               memcpy(OriginalArray, Array, size * sizeof(int)); // Make a copy of the original array
                alreadyInitialized = 1;
                printf("\n|  The array is initialized to:");
                display_array(Array, size);
                break;
            case 7:
                return 0;
                break;
            default:
                printf("\nEnter a valid option!\n");
                break;
        }
    }
    return 0;
} 
void displayMenu(void) {
    printf("\n_-_-_-_-_-_-_-_ Merge Sort Assignment -_-_-_-_-_-_-_-_");
    printf("\n1. Initialize Array with Random Values");
    printf("\n2. Display Array");
    printf("\n3. Serial Merge Sort");
    printf("\n4. Parallel Merge Sort");
    printf("\n5. Initialize Array with Best Case (ascending order)");
    printf("\n6. Initialize Array with Worst Case (descending order)");
    printf("\n7. Exit");
    printf("\n");
}
void merge(int arr[], int l, int m, int r) {
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;
    int L[n1], R[n2];
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];
    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}
void mergeSort_serial(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort_serial(arr, l, m);
        mergeSort_serial(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}
void mergeSort_parallel(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        #pragma omp parallel sections
        {
            #pragma omp section
            mergeSort_parallel(arr, l, m);
            #pragma omp section
            mergeSort_parallel(arr, m + 1, r);
        }
        merge(arr, l, m, r);
    }
}
void init_array(int *a, int size) {
    srand(time(NULL)); // Seed the random number generator with current time
    for (int i = 0; i < size; i++) {
        a[i] = rand(); // Generate random values between 0 and 99
    }
}
void initializeBest(int *a, int size) {
    for (int i = 0; i < size; i++) {
        a[i] = i;
    }
}
void initializeWorst(int *a, int size) {
    for (int i = 0; i < size; i++) {
        a[i] = size - i;
    }
}
void display_array(int *a, int size) {
    printf("\n Array = [");
    for (int i = 0; i < size; i++) {
        printf(" %d ,", a[i]);
    }
    printf("\b]");
}
```


## OUTPUT
![[Pasted image 20240221110915.png]]
![[Pasted image 20240221110953.png]]
![[Pasted image 20240221111020.png]]



## Average Case

| Sr No. | Data Points | Time taken for Serial Merge Sort | Time taken for Parallel Merge Sort |
| ---- | ---- | ---- | ---- |
| 1 | 500 | 0.000079 seconds | 0.003184 seconds |
| 2 | 1000 | 0.000281 seconds | 0.002820 seconds |
| 3 | 10000 | 0.003644 seconds | 0.007401 seconds |
| 4 | 30000 | 0.007306 seconds | 0.030752 seconds |
| 5 | 50000 | 0.012934 seconds | 0.023811 seconds |
| 6 | 70000 | 0.023823 seconds | 0.040514 seconds |
| 7 | 100000 | 0.029230 seconds | 0.077001 seconds |
|  |  |  |  |

![[Pasted image 20240213212559.png]]

## Best Case

| Sr No. | Data Points | Time taken for Serial Merge Sort | Time taken for Parallel Merge Sort |
| ---- | ---- | ---- | ---- |
| 1 | 500 | 0.000093 seconds | 0.010976 seconds |
| 2 | 1000 | 0.000193 seconds | 0.000571 seconds |
| 3 | 10000 | 0.002254 seconds | 0.009559 seconds |
| 4 | 30000 | 0.007733 seconds | 0.015638 seconds |
| 5 | 50000 | 0.013309 seconds | 0.027015 seconds |
| 6 | 70000 | 0.014245 seconds | 0.041354 seconds |
| 7 | 100000 | 0.023296 seconds | 0.058829 seconds |

![[Pasted image 20240213212637.png]]

## Worst Case

| Sr No. | Data Points | Time taken for Serial Merge Sort | Time taken for Parallel Merge Sort |
| ------ | ----------- | -------------------------------- | ---------------------------------- |
| 1      | 500         | 0.000124 seconds                                 | 0.000329 seconds                                   | 
| 2      | 1000        | 0.000108 seconds                 | 0.000395 seconds                   |
| 3      | 10000       | 0.001273 seconds                 | 0.009225 seconds                   |
| 4      | 30000       | 0.004712 seconds                 | 0.016675 seconds                   |
| 5      | 50000       | 0.013072 seconds                 | 0.031783 seconds                   |
| 6      | 70000       | 0.017343 seconds                 | 0.039345 seconds                   |
| 7      | 100000      | 0.022693 seconds                 | 0.067181 seconds                   |

![[Pasted image 20240213212654.png]]
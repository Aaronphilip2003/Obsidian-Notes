## CODE

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <unistd.h>
#include <string.h>
#include <omp.h>
void displayMenu(void);
void reset();
void red();
void init_array(int[], int);
void display_array(int[], int);
void bubbleSort_Serial(int[], int);
void bubbleSort_parallel(int[], int);
void bubbleSort_parallel_with_explanation(int[], int);
void display_array_colored(int[], int[], int, int);
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
                if (alreadyInitialized)
                    printf("\n|  The array is re-initialized to:");
                else {
                    printf("\n|  The array is initialized to:");
                    alreadyInitialized = 1;
                }
  
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
                bubbleSort_Serial(OriginalArray, size); // Sort the original unsorted array
                break;
            case 4:
                if (alreadyInitialized == 0) {
                    printf("\nArray not initialized. Please initialize the array first.\n");
                    break;
                }
                bubbleSort_parallel(Array, size);
                break;
            case 5:
                if (alreadyInitialized == 0) {
                    printf("\nArray not initialized. Please initialize the array first.\n");
                    break;
                }
                bubbleSort_parallel_with_explanation(Array, size);
                break;
            case 6:
                printf("\nEnter the size of the array: ");
                scanf("%d", &size);
                if (size <= 0 || size > max) {
                    printf("\nInvalid size. Size should be between 1 and %d.\n", max);
                    continue;
                }
                initializeBest(Array, size);
                memcpy(OriginalArray, Array, size * sizeof(int)); // Make a copy of the original array
                if (alreadyInitialized)
                    printf("\n|  The array is re-initialized to:");
                else {
                    printf("\n|  The array is initialized to:");
                    alreadyInitialized = 1;
                }
                display_array(Array, size);
                break;
            case 7:
                printf("\nEnter the size of the array: ");
                scanf("%d", &size);
                if (size <= 0 || size > max) {
                    printf("\nInvalid size. Size should be between 1 and %d.\n", max);
                    continue;
                }
                initializeWorst(Array, size);
                memcpy(OriginalArray, Array, size * sizeof(int)); // Make a copy of the original array
                if (alreadyInitialized)
                    printf("\n|  The array is re-initialized to:");
                else {
                    printf("\n|  The array is initialized to:");
                    alreadyInitialized = 1;
                }
  
                display_array(Array, size);
                break;
            case 8:
                // Print the code for parallel bubble sort
                break;
            case 9:
                return 0;
                break;
            default:
                printf("\n enter valid option !!");
                break;
        }  // end_switch
  
   }  // end_while 
    return 0;
}  // end_main
  
void displayMenu(void) {
    printf("\n_-_-_-_-_-_-_-_ Bubble Sort Assignment 2 of High Performance Computing_-_-_-_-_-_-_-_");
    printf("\n1. Initialize Array with Random Values");
    printf("\n2. Display Array");
    printf("\n3. Serial Bubble Sort");
    printf("\n4. Parallel Bubble Sort");
    printf("\n5. Parallel Bubble sort with explanation");
    printf("\n6. Initialize Array with Best Case (ascending order)");
    printf("\n7. Initialize Array with Worst Case (descending order)");
    printf("\n8. Print the parallel bubble sort code");
    printf("\n9. Exit");
    printf("\n");
}  // end_display_Menu
void bubbleSort_parallel(int *a, int size) {
    double start_time, end_time;
    int z, i, j, k;
    start_time = omp_get_wtime();
    for (z = 0; z < ceil(size / 2.0); z++) {
        #pragma omp parallel for private(j)
        for (j = 0; j < size; j += 2) {
            int temp1;
            if (j + 1 < size && a[j + 1] < a[j]) {
                temp1 = a[j + 1];
                a[j + 1] = a[j];
                a[j] = temp1;
            }
        }
        #pragma omp parallel for private(k)
        for (k = 1; k < size - 1; k += 2) {
            int temp2;
            if (k + 1 < size && a[k + 1] < a[k]) {
                temp2 = a[k + 1];
                a[k + 1] = a[k];
                a[k] = temp2;
            }
        }
    }
    end_time = omp_get_wtime();
    printf("\nParallel Sorting Time: %f seconds\n", end_time - start_time);
}
void bubbleSort_parallel_with_explanation(int *a, int size) {
    double start_time, end_time;
    int z, i, j, k;
    start_time = omp_get_wtime();
    int even_counter = 0;
    int odd_counter = 0;
    display_array(a, size);
  
    printf("\n To sort the given array we are going to use even phase and odd phases.");
    printf("\n Each of these phases compares element pairs which do not have any common element.");
  
    for (z = 0; z < ceil(size / 2.0); z++) {
        sleep(1);
        printf("\n\n Even phase %d 'th iteration. All the below comparisons are executed in parallel manner .. ", even_counter++);
        for (j = 0; j < size - 1; j += 2) {
            int temp1;
            if (j + 1 < size && a[j + 1] < a[j]) {
                temp1 = a[j + 1];
                a[j + 1] = a[j];
                a[j] = temp1;
            }
            display_array_colored(a, NULL, j, j + 1);
            sleep(1);
        }
        sleep(1);
        printf("\n\n Odd phase %d 'th iteration. All the below comparisons are executed in parallel manner .. ", odd_counter++);
        for (k = 1; k < size - 1; k += 2) {
            int temp2;
            if (k + 1 < size && a[k + 1] < a[k]) {
                temp2 = a[k + 1];
                a[k + 1] = a[k];
                a[k] = temp2;
            }
            display_array_colored(a, NULL, k, k + 1);
            sleep(1);
        }
    }
    end_time = omp_get_wtime();
    printf("\nParallel Sorting Time: %f seconds\n", end_time - start_time);
}
  
void bubbleSort_Serial(int *a, int size) {
    double start_time, end_time;
    start_time = omp_get_wtime();
    int i, j = 0;
    for (i = 0; i < size; i++) {
        for (j = 0; j < size - i - 1; j++) {
            int temp;
            if (a[j + 1] < a[j]) {
                temp = a[j + 1];
                a[j + 1] = a[j];
                a[j] = temp;
            }
        }
    }
    end_time = omp_get_wtime();
    printf("\nSerial Sorting Time: %f seconds\n", end_time - start_time);
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
  
void display_array_colored(int *a, int indices[], int x, int y) {
    printf("\n Array = [");
    for (int i = 0; i < max; i++) {
        if (i == x || i == y) {
            red();
            printf(" %d ,", a[i]);
            reset();
        } else
            printf(" %d ,", a[i]);
    }
    printf("\b]");
}
void red() {
    printf("\033[1;31m");
} 
void reset() {
    printf("\033[0m");
}

```

## OUTPUT
![[Pasted image 20240221111842.png]]
![[Pasted image 20240221111902.png]]
![[Pasted image 20240221111929.png]]

## Average Case
| Sr No. | Data Points | Time taken for Serial Bubble Sort | Time taken for Parallel Bubble Sort |
| ------ | ----------- | --------------------------------- | ----------------------------------- |
| 1      | 500         | 0.000392 seconds                  | 0.000954 seconds                    |
| 2      | 1000        | 0.001384 seconds                  | 0.001930 seconds                    |
| 3      | 10000       | 0.216226 seconds                  | 0.091191 seconds                    |
| 4      | 30000       | 2.587706 seconds                  | 0.639906 seconds                    |
| 5      | 50000       | 7.760478 seconds                  | 1.769465 seconds                    |
| 6      | 70000       | 15.542236 seconds                 | 4.837191 seconds                    |
| 7      | 100000      | 32.543785 seconds                 | 9.737296 seconds                    |

![[Pasted image 20240207120232.png]]

## Best Case
| Sr No. | Data Points | Time taken for Serial Bubble Sort | Time taken for Parallel Bubble Sort |
| ---- | ---- | ---- | ---- |
| 1 | 500 | 0.000258 seconds | 0.004320 seconds |
| 2 | 1000 | 0.001044 seconds | 0.001556 seconds |
| 3 | 10000 | 0.094924 seconds | 0.037163 seconds |
| 4 | 30000 | 0.913149 seconds | 0.299356 seconds |
| 5 | 50000 | 2.401252 seconds | 0.943703 seconds |
| 6 | 70000 | 4.758987 seconds | 1.287811 seconds |
| 7 | 100000 | 9.540666 seconds | 3.555021 seconds |

![[Pasted image 20240207122511.png]]

## Worst Case
| Sr No. | Data Points | Time taken for Serial Bubble Sort | Time taken for Parallel Bubble Sort |
| ---- | ---- | ---- | ---- |
| 1 | 500 | 0.000460 seconds | 0.001164 seconds |
| 2 | 1000 | 0.001576 seconds | 0.001780 seconds |
| 3 | 10000 | 0.285830 seconds | 0.088001 seconds |
| 4 | 30000 | 2.987241 seconds | 0.724143 seconds |
| 5 | 50000 | 8.482234 seconds | 2.101510 seconds |
| 6 | 70000 | 15.065458 secondsq | 3.992550 seconds |
| 7 | 100000 | 33.788145 seconds | 9.204779 seconds |


![[Pasted image 20240207122533.png]]
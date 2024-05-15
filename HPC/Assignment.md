
Write a C program and convert it into parallel using its openMP directive

compilation command
`gcc -fopenmp first.c -o first`

By default 8 cores are chosen as I have 8 cores
if I specify 9 cores, it will do a wrap around

local variables increase parallelism
global variables decrease parallelism

```c
#pragma omp parallel sections
{
#pragma omp section
{
*/ Executes in thread 1 */
}
#pragma omp section
{
*/ Executes in thread 2 */
}
#pragma omp section
{
*/ Executes in thread 3 */
}
}
```

A section is a piece of code that has the capability to run in parallel with another piece of code

```c
start=omp_get_wtime();
{
routine
}
end=omp_get_wtime();
Time_spent=end-start;
```



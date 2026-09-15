const char* dgemm_desc = "Basic implementation, three-loop dgemm.";
#include <stdio.h>
/*
 * This routine performs a dgemm operation
 *  C := C + A * B
 * where A, B, and C are n-by-n matrices stored in row-major format.
 * On exit, A and B maintain their input values.
 */

 //C= C + A*B == index = (i * N) + j
 //https://youtu.be/EmzdmqUWq3o?si=2SRX0HV93Y6wb0OZ&t=279
void square_dgemm(int n, double* A, double* B, double* C) 
{
   for (int i = 0; i < n; i++) {
       for (int j = 0; j < n; j++) {
           for (int k = 0; k < n; k++) {
              C[n * i + j] += A[n * i + k] * B[n * k + j];
           }
       }
   }
}

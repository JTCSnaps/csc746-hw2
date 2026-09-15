#include <algorithm>
#include <vector>

const char *dgemm_desc = "Blocked dgemm.";

/* This routine performs a dgemm operation
 *  C := C + A * B
 * where A, B, and C are n-by-n matrices stored in row-major format.
 * On exit, A and B maintain their input values. */
void square_dgemm_blocked(int n, int block_size, double *A, double *B, double *C)
{
   std::vector<double> A_cache(block_size * block_size);
   std::vector<double> B_cache(block_size * block_size);
   std::vector<double> C_cache(block_size * block_size);

   int num_blocks = n / block_size;
   
   for (int i = 0; i < num_blocks; i++) {
       for (int j = 0; j < num_blocks; j++) {
             
            // Load C block into cache
             for (int block_i = 0; block_i < block_size; block_i++) {
                for (int block_j = 0; block_j < block_size; block_j++) {
                      C_cache[block_i * block_size + block_j] = C[(i * block_size + block_i) * n + (j * block_size + block_j)];
                }
             }
   
             for (int k = 0; k < num_blocks; k++) {
                
               // Load A into cache
                for (int block_i = 0; block_i < block_size; block_i++) {
                      for (int block_k = 0; block_k < block_size; block_k++) {
                         A_cache[block_i * block_size + block_k] = A[(i * block_size + block_i) * n + (k * block_size + block_k)];
                      }
                }

                // Load B into cache
                for (int block_k = 0; block_k < block_size; block_k++) {
                      for (int block_j = 0; block_j < block_size; block_j++) {
                         B_cache[block_k * block_size + block_j] = B[(k * block_size + block_k) * n + (j * block_size + block_j)];
                      }
                }
   
                // Perform the multiplication of the blocks
                for (int block_i = 0; block_i < block_size; block_i++) {
                      for (int block_j = 0; block_j < block_size; block_j++) {
                         for (int block_k = 0; block_k < block_size; block_k++) {
                            C_cache[block_i * block_size + block_j] += A_cache[block_i * block_size + block_k] * B_cache[block_k * block_size + block_j];
                         }
                      }
                }
             }
   
             // Store the updated C block back to the original matrix
             for (int block_i = 0; block_i < block_size; block_i++) {
                for (int block_j = 0; block_j < block_size; block_j++) {
                      C[(i * block_size + block_i) * n + (j * block_size + block_j)] = C_cache[block_i * block_size + block_j];
                }
             }
          }

   }
}

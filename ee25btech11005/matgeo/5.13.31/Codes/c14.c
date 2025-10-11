#include <stdbool.h>

#define SIZE 3

void matmul(const double *A, const double *B, double *C) {
    for (int i=0; i<SIZE; i++)
        for (int j=0; j<SIZE; j++) {
            C[i*SIZE + j] = 0.0;
            for (int k=0; k<SIZE; k++)
                C[i*SIZE + j] += A[i*SIZE + k] * B[k*SIZE + j];
        }
}

void transpose(const double *A, double *B) {
    for (int i=0; i<SIZE; i++)
        for (int j=0; j<SIZE; j++)
            B[i*SIZE + j] = A[j*SIZE + i];  // swap row, column
}

bool mat_approx_equal(const double *A, const double *B, double tol) {
    for (int i=0; i<SIZE*SIZE; i++)
        if ((A[i] - B[i] > tol) || (B[i] - A[i] > tol))
            return false;
    return true;
}

int check_k(const double *A, const double *B) {
    double AB[SIZE*SIZE], AB_T[SIZE*SIZE], neg_AB[SIZE*SIZE];
    matmul(A,B,AB);
    transpose(AB,AB_T);
    for (int i=0; i<SIZE*SIZE; i++)
        neg_AB[i] = -AB[i];
    double tol = 1e-9;
    if (mat_approx_equal(AB_T, neg_AB, tol))
        return 1;
    else if (mat_approx_equal(AB_T, AB, tol))
        return 2;
    else
        return 0;
}


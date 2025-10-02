#include <stdio.h>

void row_op(double mat[2][3], int target_row, int source_row, double factor) {
    for(int j=0; j<3; j++) {
        mat[target_row][j] += factor * mat[source_row][j];
    }
}

void solve_vars(double mat[2][3], double *x, double *y) {
    double a = mat[0][0];
    double b = mat[0][1];
    double c = mat[0][2];
    *y = 0;
    *x = (c - b*(*y)) / a;
}


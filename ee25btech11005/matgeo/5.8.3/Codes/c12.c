#include <stdio.h>

void solve_lines(double *result) {
    double aug[2][3] = { {5, 7, 50}, {7, 5, 46} };
    double factor;
    factor = aug[1][0] / aug[0][0];
    for (int j = 0; j < 3; j++)
        aug[1][j] -= factor * aug[0][j];
    result[1] = aug[1][2] / aug[1][1];
    result[0] = (aug[0][2] - aug[0][1] * result[1]) / aug[0][0];
}


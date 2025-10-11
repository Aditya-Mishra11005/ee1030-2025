#include <math.h>

void find_unit_vector(double *result) {
    double a[3] = {1, -1, 0};
    double b[3] = {0, 1, -1};
    double c[3] = {-1, 0, 1};
    double aTb = a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
    double aTc = a[0]*c[0] + a[1]*c[1] + a[2]*c[2];
    double lam = -aTc / aTb;
    double d[3];
    for (int i = 0; i < 3; ++i)
        d[i] = c[i] + lam * b[i];
    double norm = sqrt(d[0]*d[0] + d[1]*d[1] + d[2]*d[2]);
    for (int i = 0; i < 3; ++i)
        result[i] = d[i] / norm;
}


#include <math.h>

void normalize(const double v[2], double out[2]) {
    double mag = sqrt(v[0]*v[0] + v[1]*v[1]);
    out[0] = v[0]/mag;
    out[1] = v[1]/mag;
}

void add_vec(const double a[2], const double b[2], double out[2]) {
    out[0] = a[0] + b[0];
    out[1] = a[1] + b[1];
}

void angle_bisector(const double A[2], const double B[2], const double C[2], double out[2]) {
    double D[2] = {A[0] - B[0], A[1] - B[1]};
    double E[2] = {C[0] - B[0], C[1] - B[1]};
    double eD[2], eE[2];
    normalize(D, eD);
    normalize(E, eE);
    add_vec(eD, eE, out);
}


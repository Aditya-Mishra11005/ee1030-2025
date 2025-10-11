#include <math.h>

// Output: d[0..2] is the unit vector
void compute_d(double* d) {
    double i[3] = {1.0, 0.0, 0.0};
    double j[3] = {0.0, 1.0, 0.0};
    double k[3] = {0.0, 0.0, 1.0};
    double a[3], b[3], c[3], x[3];
    int m;
    for (m = 0; m < 3; ++m) {
        a[m] = i[m] - j[m];
        b[m] = j[m] - k[m];
        c[m] = k[m] - i[m];
    }
    // cross product of a and b_cross_c
    double b_cross_c[3];
    b_cross_c[0] = b[1]*c[2] - b[2]*c[1];
    b_cross_c[1] = b[2]*c[0] - b[0]*c[2];
    b_cross_c[2] = b[0]*c[1] - b[1]*c[0];
    // perpendicular to both a and b_cross_c
    x[0] = a[1]*b_cross_c[2] - a[2]*b_cross_c[1];
    x[1] = a[2]*b_cross_c[0] - a[0]*b_cross_c[2];
    x[2] = a[0]*b_cross_c[1] - a[1]*b_cross_c[0];
    double norm = sqrt(x[0]*x[0] + x[1]*x[1] + x[2]*x[2]);
    d[0] = x[0]/norm;
    d[1] = x[1]/norm;
    d[2] = x[2]/norm;
}


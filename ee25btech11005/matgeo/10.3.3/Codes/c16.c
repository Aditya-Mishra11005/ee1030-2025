#include <math.h>

void find_points(double V11, double V22, double f,
                 double n1, double n2, double *out)
{
    // V = diag(V11, V22), u = 0
    double V11_inv = 1.0 / V11;
    double V22_inv = 1.0 / V22;

    double nVn = n1*n1*V11_inv + n2*n2*V22_inv;
    // Solve k^2 * n^T V^-1 n + f = 0 => k^2 = -f / nVn
    double k = sqrt(-f / nVn);

    // Two points for k and -k
    out[0] = V11_inv * k * n1; // x1
    out[1] = V22_inv * k * n2; // y1
    out[2] = V11_inv * (-k) * n1; // x2
    out[3] = V22_inv * (-k) * n2; // y2
}


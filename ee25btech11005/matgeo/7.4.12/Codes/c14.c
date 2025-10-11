#include <math.h>

// Returns the inner radius (R - r)
double inner_radius(double R, double r) {
    return R - r;
}

// Returns the outer radius (R + r)
double outer_radius(double R, double r) {
    return R + r;
}

// Generates circle points into arrays passed from Python
// (x[i] = center_x + radius*cos(theta), etc.)
void circle_points(double center_x, double center_y, double radius,
                   double *x, double *y, int n) {
    for (int i = 0; i < n; i++) {
        double theta = 2.0 * M_PI * i / n;
        x[i] = center_x + radius * cos(theta);
        y[i] = center_y + radius * sin(theta);
    }
}


#include <math.h>

void quadratic_roots(double a, double b, double c, double *x1, double *x2) {
    double disc = b*b - 4*a*c;
    *x1 = (-b + sqrt(disc)) / (2*a);
    *x2 = (-b - sqrt(disc)) / (2*a);
}

double evaluate_quadratic(double a, double b, double c, double x) {
    return a*x*x + b*x + c;
}


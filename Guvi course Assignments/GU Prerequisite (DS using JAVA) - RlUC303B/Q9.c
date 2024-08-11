#include <stdio.h>

// Define a structure for a complex number
typedef struct {
    float real;
    float imag;
} Complex;

// Function to add two complex numbers
Complex addComplex(Complex c1, Complex c2) {
    Complex result;
    result.real = c1.real + c2.real;
    result.imag = c1.imag + c2.imag;
    return result;
}

// Function to subtract two complex numbers
Complex subtractComplex(Complex c1, Complex c2) {
    Complex result;
    result.real = c1.real - c2.real;
    result.imag = c1.imag - c2.imag;
    return result;
}
// Function to print a complex number
void printComplex(Complex c, char sign) {
    printf("%.1f %c %.1fi", c.real, sign, c.imag);
}

int main() {
    Complex c1, c2, sum, difference;

    // Read two complex numbers from the user
    scanf("%f %f %f %f", &c1.real, &c1.imag, &c2.real, &c2.imag);

    // Perform addition and subtraction
    sum = addComplex(c1, c2);
    difference = subtractComplex(c1, c2);

    // Display the results
    printf("Addition: ");
    printComplex(sum, '+');
    printf("\nSubtraction: ");
    printComplex(difference, '-');

    return 0;
}

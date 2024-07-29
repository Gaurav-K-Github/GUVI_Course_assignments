// Operators and Associativity
//717580
// Problem Statement: Write a program that reads an integer n, followed by n integers, and then applies a complex expression involving multiple operators and parentheses. The expression should be evaluated in a specific order demonstrating operator precedence and associativity.

// Description: Define an expression like (((x1 + x2) - x3) * x4 / x5) % x6 and ensure the operators are applied correctly according to their precedence and associativity rules. The program should read the values and compute the result.

// Input Format:

// The first line contains an integer n, the number of elements.
// The next n lines contain one integer each.
// Output Format:

// Print the result of the complex expression.
// Sample Input:
// 6
// 5
// 10
// 3
// 8
// 2
// 7
// Sample Output:
// 6

//==============================================================================================

// -----------
// Source code:
// -----------

#include <stdio.h>

int main() {
    int n;

    scanf("%d", &n);

    if (n != 6) {
        printf("Error: The number of elements must be 6.\n");
        return 1;
    }

    int x1, x2, x3, x4, x5, x6;

    scanf("%d", &x1);
    scanf("%d", &x2);
    scanf("%d", &x3);
    scanf("%d", &x4);
    scanf("%d", &x5);
    scanf("%d", &x6);
    //717580
    int result = (((x1 + x2) - x3) * x4 / x5) % x6;

    printf("%d\n", result);

    return 0;
}

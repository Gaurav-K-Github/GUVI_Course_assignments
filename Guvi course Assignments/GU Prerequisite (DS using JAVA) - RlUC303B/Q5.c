// Unconventional Use of Goto Statement
// Problem Statement:
// Create a C program that calculates the factorial of a number using the goto statement. The twist is to implement error handling for negative inputs using the goto statement to jump to an error handling section.

// Description:

// The program should prompt the user to enter a number.
// If the number is negative, use goto to jump to an error message.
// If the number is positive, calculate the factorial using a loop and goto.717580
// Input Format:

// The user inputs a single integer.
// Output Format:

// The output is either the factorial of the number or an error message for negative inputs.

// Sample Input:
// 5
// Sample Output:
// Factorial of 5 is 120
    
//==============================================================================================

// -----------
// Source code:
// -----------

#include <stdio.h>

int main() {
    int num;
    unsigned long long factorial = 1;
    scanf("%d", &num);

    if (num < 0) {
        goto error;
    }

    int i = 1;
    loop:
    if (i <= num) {
        factorial *= i;
        i++;
        goto loop;
    }
    //717580
    printf("Factorial of %d is %llu\n", num, factorial);
    return 0;

    error:
    printf("Error: Factorial of a negative number doesn't exist.\n");
    return 1;
}

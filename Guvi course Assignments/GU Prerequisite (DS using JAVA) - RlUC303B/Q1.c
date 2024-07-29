// Data Types and Type Casting
//717580
// Problem Statement: Write a program that reads two integers and a floating-point number. Perform bitwise operations on the integers and arithmetic operations involving all three numbers. Use type casting where necessary to ensure correct results and avoid overflow/underflow.

// Description: Ensure that you correctly cast between data types to avoid any potential overflow or underflow issues during arithmetic operations. Also, explore how different data types interact with each other.

// Input Format:

// Three lines, each containing one number. The first two lines contain integers, and the third line contains a floating-point number.
// Output Format:

// Print the result of ((int1 & int2) | (int1 ^ int2)) as an integer.
// Print the result of (int1 * float_num + int2 / float_num) as a floating-point number.

// Sample Input :
// 8
// 7
// 3.3
// Sample Output :
// 15
// 28.5212

//==============================================================================================

// -----------
// Source code:
// -----------
#include <stdio.h>

int main() {
    int int1, int2;
    float float_num;

    scanf("%d", &int1);
    scanf("%d", &int2);
    scanf("%f", &float_num);

    int bitwise_result = (int1 & int2) | (int1 ^ int2);
    //717580
    float arithmetic_result = (int1 * float_num) + (int2 / float_num);

    printf("%d\n", bitwise_result);
    printf("%.4f\n", arithmetic_result);

    return 0;
}
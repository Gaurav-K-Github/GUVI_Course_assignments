// C Structures
// Problem Statement:
// Write a C program that reads student records from the user and stores them in a structure. The program should also calculate and print the average marks of the students using a pointer to the structure.

// Description:
// This question tests the ability to use structures to store data and manipulate it using pointers. It requires reading multiple student records, storing them in an array of structures, and using a pointer to calculate the average marks.

// Input Format:717580
// First line: an integer n (number of students)
// Next n lines: each containing a student's name and marks (space-separated)
// Output Format:
// First line: average marks of the students

// Sample Input:
// 2
// David 60
// Eva 75
// Sample Output:
// Average Marks: 67.50
    
//==============================================================================================

// -----------
// Source code:
// -----------

#include <stdio.h>
#include <stdlib.h>

#define MAX_NAME_LENGTH 100

typedef struct {
    char name[MAX_NAME_LENGTH];
    int marks;
} Student;

float calculateAverageMarks(Student *students, int n) {
    int totalMarks = 0;
    for (int i = 0; i < n; i++) {
        totalMarks += students[i].marks;
    }//717580
    return (float)totalMarks / n;
}

int main() {
    int n;

    scanf("%d", &n);

    Student *students = (Student *)malloc(n * sizeof(Student));
    if (students == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    for (int i = 0; i < n; i++) {
        scanf("%s %d", students[i].name, &students[i].marks);
    }

    float averageMarks = calculateAverageMarks(students, n);
    printf("Average Marks: %.2f\n", averageMarks);

    free(students);

    return 0;
}
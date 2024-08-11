#include <stdio.h>
#include <string.h>
#define MAX_NAME_LENGTH 100
typedef struct {
    char name[MAX_NAME_LENGTH];
    int age;
    float gpa;
} Student;
Student findHighestGPA(Student students[], int n) {
    Student topStudent = students[0];
    for (int i = 1; i < n; i++) {
        if (students[i].gpa > topStudent.gpa) {
            topStudent = students[i];
        }
    }
    return topStudent;
}
int main() {
    int n;
    scanf("%d", &n);

    Student students[n]; 
    for (int i = 0; i < n; i++) {
        scanf("%s %d %f", students[i].name, &students[i].age, &students[i].gpa);
    }
    printf("All Students:\n");
    for (int i = 0; i < n; i++) {
        printf("Name: %s, Age: %d, GPA: %.1f\n", students[i].name, students[i].age, students[i].gpa);
    }
    Student topStudent = findHighestGPA(students, n);
    printf("\nStudent with the highest GPA:\n");
    printf("Name: %s, Age: %d, GPA: %.1f\n", topStudent.name, topStudent.age, topStudent.gpa);
    return 0;
}

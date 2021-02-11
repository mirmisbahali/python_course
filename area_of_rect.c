#include<stdio.h>

int main(void)
{
    float length, breadth, area;
    printf("Enter length: \n");
    scanf("%f", &length);
    printf("Enter breadth: \n");
    scanf("%f", &breadth);
    
    area = length * breadth;

    printf("Area = %f\n", area);

    return 0;
}
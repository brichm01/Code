#include <stdio.h>

/* print Celsius-Fahrenheit table
    for fahr = 0, 20, ..., 300 */
main()
{
    float fahr, celsius;
    int lower, upper, step;

    lower = -20;    /* lower limit of temperature table */
    upper = 30;  /* upper limit */
    step =5;     /* step size   */

    celsius = lower;
    printf("Celsius\t\tFahrenheit\n");
    while  (celsius <= upper)  {
        fahr = ((9.0/5.0) * celsius) +32;
        printf("%6.1f\t\t%6.1f\n", celsius, fahr);
        celsius = celsius + step;
    }
}

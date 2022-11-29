#include <stdio.h>
#include <math.h>

float dplus(float num[], int n);
float dminus(float num[], int n);
float largest(float data[], int n);

int main()
{
    printf("Kolmogorov Test\n");

    int n;
    printf("Enter number of elements to compute for test: ");
    scanf("%d", &n);

    float num[n];

    for (int i = 0; i < n; i++)
    {
        scanf("%f", &num[i]);
    } 

    // sorting in ascending order

    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (num[i] > num[j])
            {
                float temp = num[i];
                num[i] = num[j];
                num[j] = temp;
            }
        }
    }

    printf("Numbers in ascending order are: \t");

    for (int i = 0; i < n; i++)
    {
        printf("%0.2f\t", num[i]);
    }

    printf("\n");

    float dp = dplus(num, n);
    float dn = dminus(num, n);
    printf("dp = %f\n", dp);
    printf("dn = %f\n", dn);

    float dvalue = dn;

    if (dp > dn)
    {
        dvalue = dp;
    }

    printf("Calculated D = %0.2f\n", dvalue);

    float dalpha = 0.565;  // for alpha = 0.05

    if (dalpha > dvalue)
    {
        printf("Since D is less than Dalpha, the data is uniformly distributed.\n");
    }
    else
    {
        printf("Since D is greater than Dalpha, the data is not uniformly distributed.\n");
    }

    return 0;
}

float dplus(float num[], int n)
{
    float data[n];

    for (int i = 0; i < n; i++)
    {
        data[i] = (i + 1) / ((float) n) - num[i];
    }

    return largest(data, n);
}

float dminus(float num[], int n)
{
    float data[n];

    for (int i = 0; i < n; i++)
    {
        data[i] = num[i] - i / ((float) n);    
    }

    return largest(data, n);
}

float largest(float data[], int n)
{
    float large = data[0];

    for (int i = 1; i < n; i++)  
    {
        if (large < data[i])
            large = data[i];
    }

    return large;
}



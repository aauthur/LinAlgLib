#include <math.h>
#include <stdio.h>
#include <stdlib.h>

double clean_number(double n, double precision) {
    if (fabs(n - round(n)) < precision) {
        return round(n);
    } else {
        return n;
    }
}

typedef struct {
    int rows;
    int cols;
    double **data;
} Matrix;

Matrix create_matrix(int rows, int cols) {
    Matrix m;
    m.rows = rows;
    m.cols = cols;
    m.data = malloc(rows * sizeof(double *));
    for (int i = 0; i < rows; i++) {
        m.data[i] = calloc(cols, sizeof(double));
    }
    return m;
}

Matrix from_2d_array(double arr[][2], int rows, int cols) {
    Matrix m = create_matrix(rows, cols);
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            m.data[i][j] = arr[i][j];
        }
    }
    return m;
}

void free_matrix(Matrix *m) {
    for (int i = 0; i < m->rows; i++) {
        free(m->data[i]);
    }
    free(m->data);
}

void print_matrix(Matrix m) {
    for (int i = 0; i < m.rows; i++) {
        for (int j = 0; j < m.cols; j++) {
            printf("%f ", m.data[i][j]);
        }
        printf("\n");
    }
}

//poopy loopy loops
int main() {
    double num = 3.000001;
    double precision = 0.00001;
    printf("Cleaned number: %f\n", clean_number(num, precision));

    double arr[][2] = {{1, 2}, {3, 4}};
    Matrix m = from_2d_array(arr, 2, 2);
    printf("Matrix:\n");
    print_matrix(m);
    free_matrix(&m);

    return 0;
}
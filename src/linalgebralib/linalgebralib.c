#include <stdio.h>
#include <stdlib.h>

struct Matrix {
    int rows;
    int columns;
    double** contents;
};
typedef struct Matrix Matrix;

Matrix* allocate_matrix(int rows, int columns) {
    //Allocates space for a matrix.
    struct Matrix* matrix = (Matrix*)malloc(sizeof(Matrix));
    matrix->rows = rows;
    matrix->columns = columns;
    double** contents = (double**)malloc(sizeof(double*) * rows);
    for (int i = 0; i < rows; i++) {
        contents[i] = (double*)calloc(columns, sizeof(double));
    }
    matrix->contents = contents;
    return matrix;
}

Matrix* create_matrix(int rows, int columns, double* contents) {
    //Initialize a matrix.
    struct Matrix *m = allocate_matrix(rows, columns);
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
            m->contents[i][j] = contents[columns*i + j];
        }
    }
    return m;
}

void print_matrix(Matrix* matrix) {
    //Exists for the purposes of debugging C file. Interaction with user will be handled through python interface.
    for (int i = 0; i < matrix->rows; i++) {
        printf("\n");
        for (int j = 0; j < matrix->columns; j++) {
            printf("%f ", matrix->contents[i][j]);
        }
    }
}

Matrix* add_matrices(Matrix* A, Matrix* B) {
    //Adds two matrices.
    if ((A->rows != B->rows) || (A->columns != B->columns)) {
        //Catches invalid dimensions. Error message exists for development purposes and must be omitted once packaged for use in Python.
        printf("Cannot add matricies of different dimensions.");
        exit(1);
    }
    else {
        double data[(A->rows)*(A->columns)];
        for (int i = 0; i < A->rows; i++){
            for (int j = 0; j < A->columns; j++) {
                data[i*A->columns+j] = A->contents[i][j] + B->contents[i][j];
            }
        }
        Matrix* result = create_matrix(A->rows, A->columns, data);
        return result;
    }
}

Matrix* subtract_matrices(Matrix* A, Matrix* B) {
    //Returns the matrix A - B
    if ((A->rows != B->rows) || (A->columns != B->columns)) {
        //Catches invalid dimensions. Error message exists for development purposes and must be omitted once packaged for use in Python.
        printf("Cannot subtract matricies of different dimensions.");
        exit(1);
    }
    else {
        double data[(A->rows)*(A->columns)];
        for (int i = 0; i < A->rows; i++){
            for (int j = 0; j < A->columns; j++) {
                data[i*A->columns+j] = A->contents[i][j] - B->contents[i][j];
            }
        }
        Matrix* result = create_matrix(A->rows, A->columns, data);
        return result;
    }
}

Matrix* scalar_multiplication(double r, Matrix* A) {
    //Function for scalar multiplication of a matrix.
    double data[(A->rows)*(A->columns)];
    for (int i = 0; i < A->rows; i++) {
        for (int j = 0; j < A->columns; j++) {
            data[(A->columns)*i+j] = r*A->contents[i][j];
        }
    }
    Matrix* result = create_matrix(A->rows, A->columns, data);
    return result;
}

int main() {
    Matrix* m1;
    Matrix* m2;
    double data1[] = {
        1, 2, 3, 4, 10,
        4, 5, 6, 9, 4.0,
        7, 8, 9, 12, 8.7
    };
    double data2[] = {
        3, 4, 5, 6, 1,
        4.8, 1, 1, 1, 2,
        7, 8, 8, 1, 1
    };
    m1 = create_matrix(3, 5, data1);
    m1 = scalar_multiplication(3.91, m1);
    m2 = create_matrix(3, 5, data2);
    m2 = scalar_multiplication(-3.8, m2);
    print_matrix(add_matrices(m1, subtract_matrices(m1, m2)));
    return 1;
}

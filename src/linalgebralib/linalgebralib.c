#include <stdio.h>
#include <stdlib.h>

__declspec( dllexport ) struct Matrix {
    int rows;
    int columns;
    double** contents;
};
typedef struct Matrix Matrix;

__declspec( dllexport ) Matrix* allocate_matrix(int rows, int columns) {
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

__declspec( dllexport ) void free_matrix(Matrix* A) {
    for (int i = 0; i < A->rows; i++) {
        free(A->contents[i]);
    }
    free(A->contents);
    free(A);
}

__declspec( dllexport ) Matrix* create_matrix(int rows, int columns, double* contents) {
    //Initialize a matrix.
    struct Matrix *m = allocate_matrix(rows, columns);
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
            m->contents[i][j] = contents[columns*i + j];
        }
    }
    return m;
}

__declspec( dllexport ) void print_matrix(Matrix* matrix) {
    //Exists for the purposes of debugging C file. Interaction with user will be handled through python interface.
    for (int i = 0; i < matrix->rows; i++) {
        printf("\n");
        for (int j = 0; j < matrix->columns; j++) {
            printf("%f ", matrix->contents[i][j]);
        }
    }
    printf("\n");
}

__declspec( dllexport ) Matrix* add_matrices(Matrix* A, Matrix* B) {
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

__declspec( dllexport ) Matrix* subtract_matrices(Matrix* A, Matrix* B) {
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

__declspec( dllexport ) Matrix* scalar_multiplication(double r, Matrix* A) {
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

__declspec( dllexport ) Matrix* matrix_multiply(Matrix* A, Matrix* B) {
    // Function for matrix multiplication.
    if (A->columns != B->rows) {
        fprintf(stderr, "Error: Dimension mismatch between matrices.\n");
        exit(1);
    }
    Matrix* result = allocate_matrix(A->rows, B->columns);
    for (int i = 0; i < A->rows; i++) {
        for (int j = 0; j < B->columns; j++) {
            result->contents[i][j] = 0;
            for (int k = 0; k < A->columns; k++) {
                result->contents[i][j] += A->contents[i][k] * B->contents[k][j];
            }
        }
    }
    return result;
}

__declspec( dllexport ) int are_matrices_equal(Matrix* A, Matrix* B) {
    // Function for checking is matrices are equal.
    if (A->rows != B->rows || A->columns != B->columns) {
        return 0;
    }
    for (int i = 0; i < A->rows; i++) {
        for (int j = 0; j < A->columns; j++) {
            if (A->contents[i][j] != B->contents[i][j]) {
                return 0;
            }
        }
    }
    return 1;
}

__declspec( dllexport ) Matrix* transpose_matrix(Matrix* A) {
    // Returns a copy of the transpose of A.
    Matrix* result = allocate_matrix(A->columns, A->rows);
    for (int i = 0; i < A->rows; i++) {
        for (int j = 0; j < A->columns; j++) {
            result->contents[j][i] = A->contents[i][j];
        }
    }
    return result;
}

__declspec( dllexport ) void row_swap(Matrix* A, int r1, int r2) {
    //Function for swapping two rows of a matrix.
    if ((r1 < 0 || r1 >= A->rows) || (r2 < 0 || r2 >= A->rows)){
        fprintf(stderr, "Error: row index out of bounds.\n");
        exit(1);
    }
    double tmp[A->columns];
    for (int j = 0; j < A->columns; j++) {
        tmp[j] = A->contents[r1][j];
    }
    for (int j = 0; j < A->columns; j++) {
        A->contents[r1][j] = A->contents[r2][j];
        A->contents[r2][j] = tmp[j];
    }
}

__declspec( dllexport ) void row_scale(Matrix* A, int r, double c) {
    // Function for scaling a row of matrix by a constant c.
    if (r < 0 || r >= A->rows){
        fprintf(stderr, "Error: row index out of bounds.\n");
        exit(1);
    }
    for (int j = 0; j < A->columns; j++) {
        A->contents[r][j] = c*(A->contents[r][j]);
    }
}

__declspec( dllexport ) void row_addition(Matrix* matrix, int r, int rc, double c){
    // Function for computing the row addition.
    if(r<0 || r>= matrix->rows || rc< 0 || rc>=matrix->rows) {
        fprintf(stderr, "Error: rows are out of bounds.\n");
    }

    if(r==rc) {
        fprintf(stderr, "Error: Cannot add row to itself.\n");
        exit(1);
    }

    for(int j = 0; j < matrix->columns; j++){
        matrix->contents[r][j] += matrix->contents[rc][j]*c;
    }
}

__declspec( dllexport ) Matrix* copy_matrix(Matrix* A) {
    Matrix* result = allocate_matrix(A->rows, A->columns);
    for (int i = 0; i < A->rows; i++) {
        for (int j = 0; j < A->columns; j++) {
            result->contents[i][j] = A->contents[i][j];
        }
    }
    return result;
}

__declspec( dllexport ) int upper_triangular(Matrix* A) {
    //Converts Matrix A to upper triangular for computing the determinant.
    int det_value = 1;
    if (A->rows == 1) {
        return det_value;
    }
    //Determine leftmost nonzero column.
    int column = -1;
    for (int j = 0;j < A->columns; j++) {
        for (int i = 0; i < A->rows; i++) {
            if (A->contents[i][j] != 0) {
                column = j;
                break;
            }
        }
        if (column != -1) {
            break;
        }
    }
    if (column == -1) {
        //Returns in case of 0 matrix.
        return det_value;
    }
    //Put nonzero entry at the top of the column.
    for (int i = 0; i < A->rows; i++) {
        if (A->contents[i][column] != 0) {
            if (i == 0) {
                break;
            } else {
                row_swap(A, 0, i);
                det_value *= -1;
                break;
            }
        }
    }
    //Eliminate nonzero entries below with row operations.
    for (int i = 1; i < A->rows; i++) {
        if (A->contents[i][column] != 0) {
            row_addition(A, i, 0, -(A->contents[i][column])/(A->contents[0][column]));
        }
    }
    //Make submatrix from remainder of the matrix and recursively call.
    Matrix* submatrix = allocate_matrix((A->rows)-1, (A->columns)-1);
    for (int i = 1; i < (A->rows); i++) {
        for (int j = 1; j < (A->columns); j++) {
            submatrix->contents[i-1][j-1] = A->contents[i][j];
        }
    }

    det_value *= upper_triangular(submatrix);
    for (int i = 0; i < (A->rows)-1; i++) {
        for (int j = 0; j < (A->columns)-1; j++) {
            A->contents[i+1][j+1] = submatrix->contents[i][j];
        }
    }
    free_matrix(submatrix);
    return det_value;
}

__declspec( dllexport ) Matrix* ref(Matrix* A) {
    //Returns a copy of Matrix A in reduced echelon form.
    Matrix* copy = copy_matrix(A);
    if (copy->rows == 1) {
        row_scale(copy, 0, 1/copy->contents[0][0]);
        return copy;
    }
    //Determine leftmost nonzero column.
    int column = -1;
    for (int j = 0;j < copy->columns; j++) {
        for (int i = 0; i < copy->rows; i++) {
            if (copy->contents[i][j] != 0) {
                column = j;
                break;
            }
        }
        if (column != -1) {
            break;
        }
    }
    if (column == -1) {
        //Returns in case of 0 matrix.
        return copy;
    }
    //Put nonzero entry at the top of the column.
    for (int i = 0; i < copy->rows; i++) {
        if (copy->contents[i][column] != 0) {
            if (i == 0) {
                row_scale(copy, 0, 1/(copy->contents[0][column]));
                break;
            } else {
                row_swap(copy, 0, i);
                row_scale(copy, 0, 1/(copy->contents[0][column]));
                break;
            }
        }
    }
    //Eliminate nonzero entries below with row operations.
    for (int i = 1; i < copy->rows; i++) {
        if (copy->contents[i][column] != 0) {
            row_addition(copy, i, 0, -(copy->contents[i][column]));
        }
    }
    //Make submatrix from remainder of the matrix and recursively call.
    Matrix* submatrix = allocate_matrix((copy->rows)-1, (copy->columns)-1);
    for (int i = 1; i < (copy->rows); i++) {
        for (int j = 1; j < (copy->columns); j++) {
            submatrix->contents[i-1][j-1] = copy->contents[i][j];
        }
    }
    for (int i = 0; i < (copy->rows)-1; i++) {
        for (int j = 0; j < (copy->columns)-1; j++) {
            copy->contents[i+1][j+1] = ref(submatrix)->contents[i][j];
        }
    }
    free_matrix(submatrix);
    return copy;
}

__declspec( dllexport ) Matrix* rref(Matrix* A) {
    //Returns a copy of matrix A in row reduced echelon form.
    Matrix* copy = ref(A);
    for (int j = 1; j < copy->rows; j++) {
        for (int i = 0; i < j; i++) {
            if (copy->contents[i][j] != 0) {
                row_addition(copy, i, j, -copy->contents[i][j]);
            }
        }
    }
    return copy;
}

__declspec( dllexport ) Matrix* augment(Matrix* A, Matrix* B) {
    //Returns an augmented matrix of matrices A and B.
    if (A->rows != B->rows) {
        fprintf(stderr, "Error: Cannot augment matrices with different numbers of rows.");
        exit(1);
    }
    else {
        Matrix* result = allocate_matrix(A->rows, A->columns+B->columns);
        for (int i = 0; i < A->rows; i++) {
            for (int j = 0; j < A->columns; j++) {
                result->contents[i][j] = A->contents[i][j];
            }
            for (int j = 0; j < B->columns; j++) {
                result->contents[i][j+A->columns] = B->contents[i][j];
            }
        }
        return result;
    }
}

__declspec( dllexport ) Matrix* id(int rows) {
    //Returns an identity matrix with the specified amount of rows and columns.
    Matrix* result = allocate_matrix(rows, rows);
    for (int i = 0; i < result->rows; i++) {
        for (int j = 0; j < result->columns; j++) {
            if (i == j) {
                result->contents[i][j] = 1;
            }
            else {
                result->contents[i][j] = 0;
            }
        }
    }
    return result;
}

__declspec( dllexport ) double det(Matrix* A) {
    //Computes the determinant of a matrix.
    if (A->rows != A->columns) {
        fprintf(stderr, "Error: Nonsquare matrices do not have determinants.\n");
        exit(1);
    }
    Matrix* copy = copy_matrix(A);
    double det_value = upper_triangular(copy);
    for (int i = 0; i < A->rows; i++) {
        det_value *= copy->contents[i][i];
    }
    free_matrix(copy);
    return det_value;
}

__declspec( dllexport ) Matrix* inverse(Matrix* A) {
    //Returns a copy of the inverse of matrix A.
    if (det(A) == 0) {
        fprintf(stderr, "Error: Matrix is not invertible.");
        exit(1);
    }
    Matrix* tmp = rref(augment(A, id(A->rows)));
    Matrix* result = allocate_matrix(A->rows, A->columns);
    for (int i = 0; i < A->rows; i++) {
        for (int j = 0; j < A->columns; j++) {
            result->contents[i][j] = tmp->contents[i][j+A->columns];
        }
    }
    free_matrix(tmp);
    return result;
}



int main() {
    Matrix* m1;
    Matrix* m2;
    double data1[] = {
        1.71, 2, 3.14159,
        4.392, 17, 1,
        7, 8, 9.11,
    };
    double data2[] = {
        3, 4,
        4.8, 1,
        7, 8
    };
    m1 = create_matrix(3, 3, data1);
    m2 = inverse(m1);
    print_matrix(matrix_multiply(m1, m2));
    free_matrix(m1);
    free_matrix(m2);
    return 0;
}

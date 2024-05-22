from ctypes import *
import io
import os
import sys
import math
import time
import random

dir_path = os.path.dirname(os.path.realpath(__file__))
dll_path = os.path.join(dir_path, "linalgebralib.dll")
lib = cdll.LoadLibrary(dll_path)

class CMatrix(Structure):
    _fields_ = [("rows", c_int), ("columns", c_int), ("contents", POINTER(POINTER(c_double)))]

lib.create_matrix.argtypes = [c_int, c_int, POINTER(c_double)]
lib.create_matrix.restype = POINTER(CMatrix)

lib.print_matrix.argtypes = [POINTER(CMatrix)]
lib.print_matrix.restype = None

lib.add_matrices.argtypes = [POINTER(CMatrix), POINTER(CMatrix)]
lib.add_matrices.restype = POINTER(CMatrix)

lib.matrix_multiply.argtypes = [POINTER(CMatrix), POINTER(CMatrix)]
lib.matrix_multiply.restype = POINTER(CMatrix)

class Matrix():
    def __init__(self, content=[], size=(0,0)):
        """Create a matrix from a 2D list, or initialize a zero matrix of a specified size passed as a tuple size=(m,n)."""
        if content != []:
            self.rows = len(content)
            self.columns = len(content[0])
            data = []
            for i in range(len(content)):
                if len(content[i]) != self.columns:
                    raise ValueError("Rows of a matrix must be of equal length.")
                else:
                    for j in range(self.columns):
                        data.append(content[i][j])
            arr = (c_double * len(data))(*data)
            self.ptr = lib.create_matrix(self.rows, self.columns, arr)
        else:
            if (size[0] == 0 and size[1] != 0) or (size[1] == 0 and size[0] != 0):
                raise ValueError("Cannot have a matrix with rows and no columns, or columns and no rows.")
            else:
                self.rows = size[0]
                self.columns = size[1]
                data = [0 for i in range(size[0]*size[1])]
                arr = (c_double * len(data))(*data)
                self.ptr = lib.create_matrix(size[0], size[1], arr)
    def __repr__(self):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        lib.print_matrix(self.ptr.contents)
        sys.stdout = old_stdout
        matrix_string = buffer.getvalue()
        return matrix_string
    def __add__(self, B):
        if (self.rows != B.rows) or (self.columns != B.columns):
            raise ValueError("Can only add matrices of the same dimensions.")
        else:
            result_ptr = lib.add_matrices(self.ptr.contents, B.ptr.contents)
            result_data = [[result_ptr.contents.contents[i][j] for j in range(self.columns)] for i in range(self.rows)]
            return Matrix(content=result_data)
    def __mul__(self, B):
        if self.columns != B.rows:
            raise ValueError("To multiply matrix A by matrix B, columns of A must equal rows of B.")
        else:
            result_ptr = lib.matrix_multiply(self.ptr.contents, B.ptr.contents)
            result_data = [[result_ptr.contents.contents[i][j] for j in range(self.columns)] for i in range(self.rows)]
            return Matrix(content=result_data)

def main():
    pass

main()

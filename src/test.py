#This file purely exists for development purposes such that I can test methods and functions as they are implemented.

import random
import time
import statistics
import matplotlib.pyplot as plt
from linalgebralib import LinAlgebraLib as la
from linalgebralib import linalgebralib2 as lac


def main():
    matrix_sizes = []
    python_addition_times = []
    python_multiplication_times = []
    python_setup_times = []
    c_addition_times = []
    c_multiplication_times = []
    c_setup_times = []
    for i in range(5, 500, 5):
        matrix_sizes.append(i)
        padd, pmul, pset = python_speed_test(i)
        python_addition_times.append(padd)
        python_multiplication_times.append(pmul)
        python_setup_times.append(pset)
        cadd, cmul, cset = caugmented_speed_test(i)
        c_addition_times.append(cadd)
        c_multiplication_times.append(cmul)
        c_setup_times.append(cset)
        print(f"Progress: {i/5}/79")
    f = open("results.txt", mode="w")
    for i in range(len(matrix_sizes)):
        f.write(f"For {matrix_sizes[i]}x{matrix_sizes[i]} matrices, the following are python-caugmented runtimes for different operations:\nMatrix Addition: Python {python_addition_times[i]} C {c_addition_times[i]}\n Matrix Multiplication: Python {python_multiplication_times[i]} C {c_multiplication_times[i]}\nSetup Time: Python {python_setup_times[i]} C {c_setup_times[i]}\n\n\n")
    f.close()
    
    
    plt.plot(matrix_sizes, python_multiplication_times, label="Python Runtimes")
    plt.plot(matrix_sizes, c_multiplication_times, label="C Augmented Runtimes")
    plt.suptitle("Matrix Multiplication Runtime (seconds) vs Square Matrix Dimensions")
    plt.legend()
    plt.show()
    

def python_speed_test(n):
    #Measures the elapsed time for matrix operations. Meant to be used with arbitrarily large matrices.
    addition_results = []
    multiplication_results = []
    setup_results = []
    for i in range(5):
        informal_start = time.time()
        data1 = [[random.random() for i in range(n)] for j in range(n)]
        data2 = [[random.random() for i in range(n)] for j in range(n)]
        A = la.Matrix(data1)
        B = la.Matrix(data2)
        start = time.time()
        A+B
        mid = time.time()
        A*B
        end = time.time()
        addition_results.append(mid-start)
        setup_results.append(start-informal_start)
        multiplication_results.append(end-mid)
    return statistics.mean(addition_results), statistics.mean(multiplication_results), statistics.mean(setup_results)

def caugmented_speed_test(n):
    #Measures the elapsed time for matrix operations. Meant to be used with arbitrarily large matrices.
    addition_results = []
    multiplication_results = []
    setup_results = []
    for i in range(5):
        informal_start = time.time()
        data1 = [[random.random() for i in range(n)] for j in range(n)]
        data2 = [[random.random() for i in range(n)] for j in range(n)]
        A = lac.Matrix(data1)
        B = lac.Matrix(data2)
        start = time.time()
        A+B
        mid = time.time()
        A*B
        end = time.time()
        addition_results.append(mid-start)
        setup_results.append(start-informal_start)
        multiplication_results.append(end-mid)
    return statistics.mean(addition_results), statistics.mean(multiplication_results), statistics.mean(setup_results)
        
        

main()


#TODO: Implement vector projections, unit vectors, cross product. FIX MATRIX - COLUMN VECTOR OPERATION

#Changlog: Fixed matrix multiplication with column vectors and row vectors where matrix is multiplied on the left.

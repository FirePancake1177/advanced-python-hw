import numpy as np
import os


class Matrix:
    def __init__(self, data):
        if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
            raise ValueError("Data must be a 2D list")

        row_lengths = [len(row) for row in data]
        if len(set(row_lengths)) != 1:
            raise ValueError("All rows must be of the same length")

        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Can only add another Matrix")
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must be of the same dimensions for addition")

        result_data = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result_data)

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Can only multiply by another Matrix")
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must be of the same dimensions for element-wise multiplication")

        result_data = [[self.data[i][j] * other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result_data)

    def __matmul__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Can only perform matrix multiplication with another Matrix")
        if self.cols != other.rows:
            raise ValueError("Number of columns of the first matrix must equal number of rows of the second matrix")

        result_data = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)]
                       for i in range(self.rows)]
        return Matrix(result_data)

    def __repr__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])


np.random.seed(0)

matrix_a_data = np.random.randint(0, 10, (10, 10)).tolist()
matrix_b_data = np.random.randint(0, 10, (10, 10)).tolist()

matrix_a = Matrix(matrix_a_data)
matrix_b = Matrix(matrix_b_data)

os.makedirs('artifacts_task_1', exist_ok=True)

matrix_sum = matrix_a + matrix_b
with open('artifacts_task_1/matrix+.txt', 'w') as f:
    f.write(str(matrix_sum))

matrix_elementwise = matrix_a * matrix_b
with open('artifacts_task_1/matrix*.txt', 'w') as f:
    f.write(str(matrix_elementwise))

matrix_product = matrix_a @ matrix_b
with open('artifacts_task_1/matrix@.txt', 'w') as f:
    f.write(str(matrix_product))
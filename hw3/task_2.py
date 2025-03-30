import numpy as np
import os

class PrintableMixin:
    def __str__(self):
        return np.array_str(self.data)

class FileWritableMixin:
    def write(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))

class ArithmeticMixin:
    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Can only add another Matrix")
        if self.data.shape != other.data.shape:
            raise ValueError("Matrices must be of the same dimensions for addition")
        return Matrix(self.data + other.data)

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Can only subtract another Matrix")
        if self.data.shape != other.data.shape:
            raise ValueError("Matrices must be of the same dimensions for subtraction")
        return Matrix(self.data - other.data)

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Can only multiply by another Matrix")
        if self.data.shape != other.data.shape:
            raise ValueError("Matrices must be of the same dimensions for element-wise multiplication")
        return Matrix(self.data * other.data)

    def __matmul__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Can only perform matrix multiplication with another Matrix")
        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("Number of columns of the first matrix must equal number of rows of the second matrix")
        return Matrix(self.data @ other.data)

class Matrix(PrintableMixin, FileWritableMixin, ArithmeticMixin):
    def __init__(self, data):
        if not isinstance(data, np.ndarray):
            data = np.array(data)
        self._data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value, np.ndarray):
            value = np.array(value)
        self._data = value

np.random.seed(0)

matrix_a_data = np.random.randint(0, 10, (10, 10))
matrix_b_data = np.random.randint(0, 10, (10, 10))

matrix_a = Matrix(matrix_a_data)
matrix_b = Matrix(matrix_b_data)

os.makedirs('artifacts_task_2', exist_ok=True)

matrix_sum = matrix_a + matrix_b
matrix_sum.write('artifacts_task_2/matrix+.txt')

matrix_elementwise = matrix_a * matrix_b
matrix_elementwise.write('artifacts_task_2/matrix*.txt')

matrix_product = matrix_a @ matrix_b
matrix_product.write('artifacts_task_2/matrix@.txt')

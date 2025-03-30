import numpy as np
import os

PRIME = 101


class HashableMixin:
    def __hash__(self):
        # сумма всех элементов матрицы, умноженная на какое-то заданное простое число
        return int(np.sum(self.data) * PRIME)


class CacheableMatMulMixin:
    _cache = {}

    def cached_matmul(self, other):
        key = (hash(self), hash(other))
        if key not in self._cache:
            self._cache[key] = self @ other
        return self._cache[key]

class Matrix(HashableMixin, CacheableMatMulMixin):
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
size = (3, 3)

matrix_a_data = np.random.randint(0, 10, size)
matrix_b_data = np.random.randint(0, 10, size)
matrix_c_data = matrix_a_data.copy()
matrix_d_data = matrix_b_data.copy()

for i in range(matrix_c_data.size):
    matrix_c_data.flat[i] += 1
    if hash(Matrix(matrix_c_data)) == hash(Matrix(matrix_a_data)):
        break
    matrix_c_data.flat[i] -= 1

matrix_a = Matrix(matrix_a_data)
matrix_b = Matrix(matrix_b_data)
matrix_c = Matrix(matrix_c_data)
matrix_d = Matrix(matrix_d_data)

os.makedirs('artifacts_task_3', exist_ok=True)

with open('artifacts_task_3/A.txt', 'w') as f:
    f.write(str(matrix_a))
with open('artifacts_task_3/B.txt', 'w') as f:
    f.write(str(matrix_b))
with open('artifacts_task_3/C.txt', 'w') as f:
    f.write(str(matrix_c))
with open('artifacts_task_3/D.txt', 'w') as f:
    f.write(str(matrix_d))

ab = matrix_a.cached_matmul(matrix_b)
cd = matrix_c.cached_matmul(matrix_d)

with open('artifacts_task_3/AB.txt', 'w') as f:
    f.write(str(ab))
with open('artifacts_task_3/CD.txt', 'w') as f:
    f.write(str(cd))

with open('artifacts_task_3/hash.txt', 'w') as f:
    f.write(f"Hash(AB): {hash(ab)}, Hash(CD): {hash(cd)}")

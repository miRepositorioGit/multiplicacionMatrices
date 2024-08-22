"""operador_Arroba.py  multiplica dos matrices son el operador @
Descripción
            Muestra como operar la multiplicación de dos matrices 2x2
            con el operador @.

            Se tienen dos operadores de matriz cuadrada de 2x2
            {matrix_a, matrix_b} mismos que son multiplicados para obtener una matrix_c cudrada 2x2

            [[1, 2],    [[5, 6],
            [3, 4]]  * [7, 8]]  = [[5+14, 6+16], [15+28, 18+32]] 
"""
import numpy as np

# Define two matrices as NumPy arrays
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

print(matrix_a)
print(matrix_b)

# Perform matrix multiplication using the "@" operator
result = matrix_a @ matrix_b

# Print the result
print(result)

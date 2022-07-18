"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

"""
from typing import List


class Matrix:
    def __init__(self, matrix_data: List[List]):
        self.__matrix = matrix_data

        # Проверка одинакового размера всех списков
        m_rows = len(self.__matrix)
        self.__matrix_size = frozenset([(m_rows, len(row)) for row in self.__matrix])

        if len(self.__matrix_size) != 1:
            raise ValueError("Invalid matrix size")

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self.__matrix])

    def __add__(self, other: "Matrix") -> "Matrix":
        if not isinstance(other, Matrix):  # Проверка класса второй матрицы
            raise TypeError(f"'{other.__class__.__name__}' "
                            f"incompatible object type")
        if self.__matrix_size != other.__matrix_size:  # Проверка совпадения размеров исходной и второй матриц
            raise ValueError(f"Matrix sizes difference")

        result = []
        for item in zip(self.__matrix, other.__matrix):
            result.append([sum([j, k]) for j, k in zip(*item)])

        return Matrix(result)


if __name__ == '__main__':
    matrix1 = Matrix([[7, 6, 5], [3, 4, 5]])
    print(matrix1, '\n')

    matrix2 = Matrix([[1, 5, 6], [4, 5, 2]])
    print(matrix2, '\n')

    print(matrix1 + matrix2)

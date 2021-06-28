from .Vector import Vector

class Matrix:
    def __init__(self, list2d):
        # 进行复制
        self._values = [row[:] for row in list2d]

    # 返回矩阵的第 index 个行向量
    def row_vector(self, index):
        return Vector(self._values[index])

    # 返回矩阵的第 index 个列向量
    def col_vector(self, index):
        return Vector([row[index] for row in self._values])

    # 返回 pos 位置的元素
    def __getitem__(self, pos):
        r, c = pos
        return self._values[r][c]

    # 返回矩阵元素个数
    def size(self):
        # 返回元组
        r, c = self.shape()
        return r * c

    # 返回矩阵的行数
    def row_num(self):
        return self.shape()[0]

    # 返回矩阵的行数
    def row_num(self):
        return self.shape()[1]

    __len__ = row_num

    # 返回矩阵的形状(行数、列数)
    def shape(self):
        return len(self._values), len(self._values[0])

    def __repr__(self):
        return "Matrix({})".format(self._values)

    __str__ = __repr__
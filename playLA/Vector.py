import math
# . 是指当前模块中
from ._global import EPSILON

class Vector:
    # 构造函数
    def __init__(self, lst):
        # 拷贝 list —— immutable
        self._values = list(lst)

    # 零向量
    # 类特殊的方法 cls 为当前的类，dim 为维度
    @classmethod
    def zero(cls, dim):
        # [0] * 2 = [0, 0]
        return cls([0] * dim)

    # 求向量模
    def norm(self):
        return math.sqrt(sum(e ** 2 for e in self))

    # 返回向量的单位向量
    def normalize(self):
        if self.norm() < EPSILON:
            raise ZeroDivisionError("Normalize error! norm is zero.")
        return Vector(self._values) / self.norm()

    # 向量的加法
    def __add__(self, another):
        assert len(self) == len(another), \
            "Error in adding. Length of vectors must be same."
        return Vector([a + b for a, b in zip(self, another)])

    # 向量减法
    def __sub__(self, another):
        assert len(self) == len(another), \
            "Error in adding. Length of vectors must be same."
        return Vector([a - b for a, b in zip(self, another)])

    # 向量点乘
    def dot(self, another):
        # 向量相乘，维度必须相等
        assert len(self) == len(another), \
               "Error in dot product. Length of vectors must be same."
        return sum(a * b for a, b in zip(self, another))

    # 向量数乘
    def __mul__(self, k):
        # 遍历向量每个分量进行相乘
        return Vector([k * e for e in self])

    # 向量数乘 右乘
    def __rmul__(self, k):
        return self * k

    # 向量数除
    def __truediv__(self, k):
        return (1 / k) * self

    # 向量取正 +(1, 2)
    def __pos__(self):
        return 1 * self

    # 向量取负 -(1, 2)
    def __neg__(self):
        return -1 * self

    # 返回向量的迭代器
    def __iter__(self):
        return self._values.__iter__()

    # 取向量的第 index 个元素
    def __getitem__(self, index):
        return self._values[index]

    # 返回向量长度（有多少个元素）
    def __len__(self):
        return len(self._values)

    # 系统调用：如何显示一个向量；直接打印实例就是调用该规则
    def __repr__(self):
        return "Vector({})".format(self._values)

    # 用户调用: 可以通过 print 进行打印
    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))

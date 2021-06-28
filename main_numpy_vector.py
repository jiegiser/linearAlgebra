import numpy as np

if __name__ == "__main__":
    print(np.__version__)
    # 列表
    lst = [1, 2, 3] # 可以存储任何类型数值
    lst[0] = 'Linear Algebra'

    # numpy 定义一个向量
    vec = np.array([1, 2, 3])
    print(vec)
    # 报错
    # vec[0] = 'Linear Algebra'

    # 不是 immutable 类型，可以进行修改；
    # vec[0] = 666
    # print(vec)

    # 创建 0 向量,创建的是浮点型
    print(np.zeros(5)) # [0. 0. 0. 0. 0.]
    print(np.ones(5)) # [1. 1. 1. 1. 1.]
    print(np.full(5, 66)) # [66 66 66 66 66]

    # np.array 的基本类型
    print("size = ", vec.size)
    print("size = ", len(vec))
    print(vec[0])
    # 最后一个元素
    print(vec[-1])
    # 截取
    print(vec[0:2])
    print(type(vec[0:2]))

    # np.array 的基本运算
    vec2 = np.array([4, 5, 6])
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))

    # 向量数乘
    print("{} * {} = {}".format(vec, 3, vec * 3))
    print("{} * {} = {}".format(3, vec, 3 * vec))

    # 向量取正、取负
    print("+{} = {}".format(vec, +vec))
    print("-{} = {}".format(vec, -vec))

    # 两个向量相乘
    print("{} * {} = {}".format(vec, vec2, vec * vec2))

    # 点乘
    print("{}.dot({}) = {}".format(vec, vec2, vec.dot(vec2)))

    # 向量模
    print(np.linalg.norm(vec))
    # 归一化，单位向量
    print(vec / np.linalg.norm(vec))
    print(np.linalg.norm(vec / np.linalg.norm(vec)))
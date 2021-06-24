from playLA.Vector import Vector

if __name__ == "__main__":
    vec = Vector([2, 3])
    print(vec)
    print(len(vec))
    print("vec[0] = {}, vec[1] = {}".format(vec[0], vec[1]))

    # 向量相加减
    vec2 = Vector([3, 1])
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))

    # 向量数乘
    print("{} * {} = {}".format(vec, 3, vec * 3))
    print("{} * {} = {}".format(3, vec, 3 * vec))

    # 向量取正、取负
    print("+{} = {}".format(vec, +vec))
    print("-{} = {}".format(vec, -vec))

    # 生成 0 向量
    zero2 = vec.zero(2)
    print(zero2)
    print("{} + {} = {}".format(vec, zero2, vec + zero2))

    # 向量模
    print("norm({}) = {}".format(vec, vec.norm()))
    print("norm({}) = {}".format(vec2, vec2.norm()))
    print("norm({}) = {}".format(zero2, zero2.norm()))

    # 单位向量
    print("normalize {} is {}".format(vec, vec.normalize()))
    print(vec.normalize().norm())

    # 归一化
    try:
        zero2.normalize()
    except ZeroDivisionError:
        print("Cannot normalize zero vector {}".format(zero2))

    # 点乘
    print(vec.dot(vec2))

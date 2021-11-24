import numpy as np

def Bilinear_Interpolation(in_X, in_Y, list):
    x0 = np.floor(in_X).astype(int)
    x1 = x0 + 1
    y0 = np.floor(in_Y).astype(int)
    y1 = y0 + 1
    dy = (in_Y - y0)
    dx = (in_X - x0)

    ul = list[x0, y0] * (1 - dy) * (1 - dx)
    ur = list[x0, x1] * dy * (1 - dx)
    ll = list[y1, x0] * dx * (1 - dy)
    lr = list[y1, x1] * dx * dy

    return ul + ur + ll + lr


def BiCubic(var, invar, list, a):
    return a * a * (a - 1) * float(list[var + 2, invar]) + a * (1 + a - a * a) * float(list[var + 1, invar]) + (1 - 2 * a * a + a ** 3) * float(list[var, invar]) - a * ((1 - a) ** 2) * float(list[var - 1, invar])

def Cubic_Convolution(in_X, in_Y, array):
    x0 = np.floor(in_X).astype(int)
    y0 = np.floor(in_Y).astype(int)

    a = in_X - x0
    b = in_Y - y0

    result_X = np.array([])
    for i in range(-1, 3):
        result_X = np.append(result_X, BiCubic(x0, y0 + i, array, a))
    result = BiCubic(1, None, result_X, b)

    return result

in_x = float(input('请输入X的相对坐标）:'))
in_y = float(input('请输入Y的相对坐标）:'))

in_array = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
for i in range(0, 4):
    for j in range(0, 4):
        print('输入第',i + 1,'行第',j + 1,'列的像元值:')
        in_array[i, j] = float(input())

print('双线性内插的结果为：',Bilinear_Interpolation(in_x, in_y, in_array))
print('三次卷积内插的结果为：',Cubic_Convolution(in_x, in_y, in_array))




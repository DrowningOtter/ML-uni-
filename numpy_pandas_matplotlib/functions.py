from typing import List


def sum_non_neg_diag(X: List[List[int]]) -> int:
    """
    Вернуть  сумму неотрицательных элементов на диагонали прямоугольной матрицы X. 
    Если неотрицательных элементов на диагонали нет, то вернуть -1
    """ 
    if len(X) == 0:
        return  -1
    stop = min(len(X), len(X[0]))
    sum = 0
    once = True
    for i in range(stop):
        if X[i][i] >= 0:
            sum += X[i][i]
            once = False
    if once:
        return -1
    return sum


def are_multisets_equal(x: List[int], y: List[int]) -> bool:
    """
    Проверить, задают ли два вектора одно и то же мультимножество.
    """
    x.sort()
    y.sort()
    return x == y


def max_prod_mod_3(x: List[int]) -> int:
    """
    Вернуть максимальное прозведение соседних элементов в массиве x, 
    таких что хотя бы один множитель в произведении делится на 3.
    Если таких произведений нет, то вернуть -1.
    """
    once = True
    if len(x) < 2:
        return -1
    for i in range(len(x) - 1):
        if x[i] % 3 == 0 or x[i + 1] % 3 == 0:
            if once:
                max_val = x[i] * x[i + 1]
                once = False
            else:
                max_val = max(max_val, x[i] * x[i + 1])
    if once:
        return -1
    return max_val


def convert_image(image: List[List[List[float]]], weights: List[float]) -> List[List[float]]:
    """
    Сложить каналы изображения с указанными весами.
    """
    if len(weights) != len(image[0][0]):
        raise ValueError
    ans = [[0] * len(image[0]) for _ in range(len(image))]
    for i in range(len(image)):
        for k in range(len(image[i])):
            for j in range(len(image[i][k])):
                ans[i][k] += image[i][k][j] * weights[j]
    return ans
    pass


def rle_scalar(x: List[List[int]], y:  List[List[int]]) -> int:
    """
    Найти скалярное произведение между векторами x и y, заданными в формате RLE.
    В случае несовпадения длин векторов вернуть -1.
    """
    if len(x) == 0 and len(y) == 0:
        return 0
    x_cur = x[0][0]
    x_am = x[0][1]
    y_cur = y[0][0]
    y_am = y[0][1]
    i, j = 0, 0
    ans = 0
    while i < len(x) and j < len(y):
        if x_am > y_am:
            x_am -= y_am
            ans += x_cur * y_cur * y_am
            j += 1
            if j == len(y):
                break
            y_am = y[j][1]
            y_cur = y[j][0]
        elif x_am < y_am:
            y_am -= x_am
            ans += x_cur * y_cur * x_am
            i += 1
            if i == len(x):
                break
            x_am = x[i][1]
            x_cur = x[i][0]
        else:
            ans += x_cur * y_cur * x_am
            i += 1
            j += 1
            if i == len(x) or j == len(y):
                if i == len(x):
                    x_am = 0
                if j == len(y):
                    y_am = 0
                break
            y_am = y[j][1]
            y_cur = y[j][0]
            x_am = x[i][1]
            x_cur = x[i][0]
    if x_am != 0 or y_am != 0:
        return -1
    return ans
    pass


def cosine_distance(X: List[List[float]], Y: List[List[float]]) -> List[List[float]]:
    """
    Вычислить матрицу косинусных расстояний между объектами X и Y. 
    В случае равенства хотя бы одно из двух векторов 0, косинусное расстояние считать равным 1.
    """
    answer_list = []
    for line in range(len(X)):
        cur_str = []
        for col in range(len(Y)):
            ans = 1.0
            prod = 0
            for i in range(len(X[line])):
                prod += X[line][i] * Y[col][i]
            x2, y2 = 0, 0
            for i in range(len(X[line])):
                x2 += X[line][i] ** 2
                y2 += Y[col][i] ** 2
            if x2 != 0 and y2 != 0:
                ans = prod / ((x2 ** 0.5) * (y2 ** 0.5))
            cur_str.append(ans)
        answer_list.append(cur_str)
    return answer_list
    pass



# import numpy as np
# x = np.load('/home/ubuntu/code/uni/5sem/ml/numpy_pandas_matplotlib/public_tests/06_test_task6_input/input_1/x.npy')
# y = np.load('/home/ubuntu/code/uni/5sem/ml/numpy_pandas_matplotlib/public_tests/06_test_task6_input/input_1/y.npy')
# print(x)
# print(y)

# import pickle
# with open('/home/ubuntu/code/uni/5sem/ml/numpy_pandas_matplotlib/public_tests/06_test_task6_gt/output_1.pkl', 'rb')as f:
#     data = pickle.load(f)
# print(data)

# X = [[0, 0, 0], [1, 0, 0]]
# Y = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
# print(cosine_distance(X, Y))
# X = [[0.04753405, 0.41767951, 0.15895611, 0.37750651, 0.20141682, 0.60621332, 0.92042688, 0.31703947, 0.64286235, 0.58386686],
# [0.51816666, 0.35093686, 0.64810281, 0.10789224, 0.08629358, 0.13154482, 0.53388299, 0.31791607, 0.44886009, 0.26036309],
# [0.21147751, 0.31344511, 0.27828612, 0.25766646, 0.09382452, 0.04118538, 0.0936042,  0.49392149, 0.08907893, 0.8553927],
# [0.28015765, 0.81276383, 0.65319279, 0.93023307, 0.86672749, 0.03500255, 0.21984648, 0.68495555, 0.7227616,  0.15071199],
# [0.42121658, 0.34345005, 0.01032145, 0.4221813,  0.85877763, 0.62246729, 0.17564917, 0.55013502, 0.4916385,  0.17768098],
# [0.26866274, 0.97396451, 0.72781025, 0.65609888, 0.52727596, 0.36274493, 0.95484825, 0.33000732, 0.74946094, 0.06829224],
# [0.46805809, 0.6180785,  0.97007516, 0.61232595, 0.52322352, 0.51997058, 0.49949928, 0.05812933, 0.52209057, 0.62295796],
# [0.75023812, 0.13191085, 0.92804802, 0.46402401, 0.99014688, 0.68994127, 0.38616019, 0.06714398, 0.64277374, 0.13106755],
# [0.44718945, 0.42078053, 0.43086063, 0.87183141, 0.75419383, 0.52357636, 0.80904549, 0.08268864, 0.97266436, 0.83677731],
# [0.49731871, 0.72419395, 0.25431142, 0.22451549, 0.0134126,  0.38240069, 0.44566705, 0.54421713, 0.89917233, 0.56397643]]
# Y = [[0.0667571,  0.68622802, 0.35096025, 0.03796295, 0.52725871, 0.26370552, 0.78452333, 0.75035532, 0.4050578,  0.30577114],
# [0.58153941, 0.84078108, 0.1437545,  0.79020209, 0.72852558, 0.7642259, 0.32043831, 0.20339656, 0.52571048, 0.48555929],
# [0.93107569, 0.01958217, 0.27762515, 0.83840763, 0.77648121, 0.87204028, 0.04903152, 0.52902445, 0.76510562, 0.14081629],
# [0.04447728, 0.33042854, 0.24280913, 0.39156631, 0.62657869, 0.33523543, 0.6974021,  0.69940946, 0.85722314, 0.82537153],
# [0.8806982,  0.05807239, 0.71997973, 0.29324477, 0.93273093, 0.32595428, 0.81101529, 0.23497829, 0.53387987, 0.71864554],
# [0.55778939, 0.72710471, 0.10385319, 0.08659502, 0.98520544, 0.40496352, 0.42851599, 0.91468967, 0.21274986, 0.89480965],
# [0.43868079, 0.92408432, 0.52319526, 0.60672703, 0.19412759, 0.6101888, 0.01173459, 0.13048125, 0.96700808, 0.75292188],
# [0.6018315,  0.20225235, 0.88261119, 0.05830321, 0.99962462, 0.70964374, 0.30412629, 0.84734708, 0.1404898,  0.66834658],
# [0.26256978, 0.61446391, 0.7768096,  0.87608423, 0.01742808, 0.52313444, 0.19929459, 0.59298858, 0.87919364, 0.6674341],
# [0.85400392, 0.92965657, 0.24780675, 0.3639421,  0.7891193,  0.22830665, 0.01978386, 0.05073953, 0.75240904, 0.5779449]]
# print(cosine_distance(X, Y))
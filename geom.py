def hyp(a, b):
    return ((a ** 2) + (b ** 2)) ** 0.5


def len_line(x1, y1, x2, y2):
    return hyp(abs(x1 - x2), abs(y1 - y2))


def perimetr(sides):
    per = 0
    for i in sides:
        per += len_line(i[0], i[1], i[2], i[3])
    return per


def S_tri(x1, y1, x2, y2, x3, y3):
    x = [x1, x2, x3]
    y = [y1, y2, y3]
    square = abs(max(x) - min(x)) * abs(max(y) - min(y))
    for i in range(3):
        square -= (len_line(x[i], 0, x[i-1], 0) * len_line(0, y[i], 0, y[i-1])) / 2
    return square


def S_pol(vertexes):
    v = vertexes.copy()
    if len(v) % 2 == 1:
        return "Error"
    if len(v) == 4:
        return 0
    else:
        print(S_tri(v[0], v[1], v[2], v[3], v[-2], v[-1]))
        return S_tri(v[0], v[1], v[2], v[3], v[-2], v[-1]) + S_pol(v[2:])

# geom.py
Как пользоваться

hyp(a, b)
Считает гипотенузу по данным катетам a и b


len_line(x1, y1, x2, y2)
Посчитает длину линии по координатам ее начала и конца


perimetr(sides)
Посчитает периметр фигуры по координатам ее сторон
!!!Важно!!! Передовать значения нужно ввиде двумерного массива
Пример: perimetr([[x1, y1, x2, y2], [x2, y2, x3, y3], [x3, y3, x1, y1]]


S_tri(x1, y1, x2, y2, x3, y3)
Посчитает площадь треугольника по заданным координатам трех вершин


S_pol(vertexes)
Посчитает площадь многоугольника по заданным координатам всех вершин фигуры
!!!ВАЖНО!!! Передовать координаты нужно ввиде массива
Пример: S_pol([x1, y1, x2, y2, x3, y3])
!!! Примечание !!! Функция S_pol() является рекурсивной и может работать долго.
Количество всех значений должно без остатка делиться на 2, а также должно быть больше 4.
Координаты должны вводиться в том порядке, в котором они следуют на фигуре.


В дальнейшем добавиться больше функций и будут совершенствоваться старые.
При возникновении ошибок обращайтесь по почте kolyag8@yandex.ru

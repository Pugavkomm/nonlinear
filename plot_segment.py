import segment_function
import matplotlib.pyplot as plt
import numpy

quant_it = 100  # количество итераций
quant_el = 10  # количество элементов
quant_start_one = 40  # c этого элемента задаем начальные условия
quant_start_end = 60  # на этом элементе заканчиваем задавать н.у. остальные элементы равны нулю
value_start = .5  # значение начальных условий
alpha = 1
d = .3
a = aa = .002
matrix = segment_function.segment (quant_el, quant_it, quant_start_one, quant_start_end, value_start, a=a, d=d,
                                   alpha=alpha)  # вызываем функцию, которая возвращает матрицу с реализацией системыc
print (matrix[0])
x = numpy.arange (quant_it)
for i in range (1, quant_el):
    plt.plot (x, matrix[i], '.', linestyle='-')
plt.plot ([0, quant_it], [0, 0], linestyle='-', c='black', label='н.т.: u = 0')
plt.plot ([0, quant_it], [1, 1], linestyle='-', c='blue', label='н.т.: u =  1')
plt.plot ([0, quant_it], [aa, aa], linestyle='-', c='red', label='н.т.: u = a = ' + str (aa))
plt.plot (x, matrix[0], '.', linestyle='-', label='Первый элемент', color='black', alpha=.5)
plt.legend ()
plt.xlabel ('n - дискретное время')
plt.ylabel ('$U_j$ значение элемента')
plt.show ()

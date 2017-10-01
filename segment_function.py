import numpy as np
import function
import progress_bar
#зададим систему, но граничные условия будут давать отрезок

def segmen(quant_el = 100, quant_it = 110, quant_start_one= 10, quant_start_end = 50,value_start= .2, d=0.4, a = 0.5, alpha = 1):
    elements = np.zeros((quant_el, quant_it))
    for i in range(quant_start_one, quant_start_end + 1):
        elements[i][0] = value_start
    for i in range(quant_it - 1):
        progress_bar.update_progress(i / (quant_it - 1), 'вычисление системы')
        for j in range(quant_el):
            if j == 0:
                elements[j][i + 1] = function.next_iter(a, d, 0, elements[j][i], elements[j + 1][i], alpha)
            elif j == quant_el - 1:
                elements[j][i + 1] = function.next_iter(a, d, elements[j - 1][i], elements[j][i], 0, alpha)
            else:
                elements[j][i + 1] = function.next_iter(a, d, elements[j - 1][i], elements[j][i], elements[j + 1][i], alpha)
    return elements
'''поместим необходимые функции нашей задачи. А точнее кубическую функцию для нелинейности,
все отображение...'''

# зададим кусочно линейную функцию
def piecewise_line(u, beta = 0.5, alpha = 0.2):
    if u < .5:
        return -alpha*2*u + beta
    elif u > .5:
        return -alpha*2*(u-1) + beta
    else:
        print ("Попали на разрыв")
# кубичческая функция:
# параметр a отвечает за положение корня, позволяет управлять нашей функцией

def nonlin_func(a, u, alpha = 1):
    return alpha*u* (u - a) * (1 - u)

# создадим функцию задающю отображение
# необходимые действия связанные с номером элемента проведем уже в основной части программы

def next_iter(a, d, early, present, next, alpha = 1):
    return present + d*(next - 2*present + early) + nonlin_func(a, present, alpha)

# функция для системы записанной в новых переменных, дл решения в виде стационарных волн

def stat_iter(a, d, x, y, alpha = 1):
    return d/(1-d)*x + ((1-2*d)*y + nonlin_func(a, y, alpha))/(1 - d)

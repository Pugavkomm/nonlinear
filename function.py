'''поместим необходимые функции нашей задачи. А точнее кубическую функцию для нелинейности,
все отображение...'''

# зададим кусочно линейную функцию
def piecewise_line(u, beta = 0, alpha = 0.2):
    if u < 1/2:
        return -alpha*2*u + beta
    elif u > 1/2:
        return -alpha*2*(u-1) + beta
    else:
        print ("Попали на разрыв")
# кубичческая функция:
# параметр a отвечает за положение корня, позволяет управлять нашей функцией

def nonlin_func(a, u):
    return u * (u - a) * (1 - u)

# создадим функцию задающю отображение
# необходимые действия связанные с номером элемента проведем уже в основной части программы

def next_iter(a, d, early, present, next):
    return present + d*(next - 2*present + early) + nonlin_func(a, present)

# функция для системы записанной в новых переменных, дл решения в виде стационарных волн

def stat_iter(a, d, x, y):
    return d/(1-d)*x + ((1-2*d)*y + nonlin_func(a, y))/(1 - d)

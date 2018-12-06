import random

# считаем, что члены последовательности нумеруются начиная с 1. Поэтому генерируем номера от 1.
# причем n<=m, иначе задание интервала некорректно
print('Задача про числа Фибоначчи: \n')
m = random.randint(1,100)
n = random.randint(1,m+1)
print(n, m)

def ffunc(n,m):
    flist = [1, 1]
    for x in range(2,m):
        flist.append(flist[x-1]+flist[x-2])
    return flist[n-1:m]

wanted_list = ffunc(n,m)
print(wanted_list)


print('\n\n\nЗадача про Сортировку: \n')
mylist = [random.randint(0,100) for i in range(10)]
def mysort(in_list):
    for j in range(0,len(in_list)-1):
        for i in range(0,len(in_list)-j-1):
            if in_list[i] > in_list[i+1]:
                in_list[i],in_list[i + 1] = in_list[i + 1], in_list[i]
    return in_list
print(mylist)
print(mysort(mylist))


print('Задача про числа Фильтр: \n')

def test_func(x):
    if x<10: return True
    else: return False

def my_filter(func, iterable):
    new_it = []
    for x in iterable:
        if func(x)==True:
            new_it.append(x)
        else: print('{} filtered out'.format(x))
    return new_it

test_iterable = [1,3,44,53,23,2,6,0]
print(my_filter(test_func, test_iterable))
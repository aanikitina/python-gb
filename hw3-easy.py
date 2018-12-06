
import random
print('Задача про округление:\n')
a = random.uniform(0,10)
b = random.randint(0,10)
def my_round(x, n):
    int_form = x*10**n
    if (int_form - int(int_form))>=0.5:
        int_form+=1
    return int(int_form)/10**n

print('При округлении {} до {} десятичных знаков получаем {}'.format(a, b, my_round(a,b)))
del a, b

print('\n\n\n\n\nЗадача про билет:\n')
# второе задание

ticket = random.randint(100000, 1000000)

def lucky_ticket(ticket_number):
    first = str(ticket_number//1000)
    last = str(ticket_number%1000)

    def dsum(xstring):
        s = 0
        for x in xstring: s = s + int(x)
        return s

    return dsum(first)==dsum(last)
print('Ваш билет: {}'.format(ticket))
if lucky_ticket(ticket):
    print('Lucky!')
else: print('Not today...')
del ticket




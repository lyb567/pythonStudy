
li = ['+', '-', '*', '/']


def compute(a,b,c,d):
    return eval('3{0}3{1}3{2}3{3}3'.format(a,b,c,d))


def strProc(str, x, y):
    temp = ''
    for i in str:
        if i == x:
            temp += y
        else:
            temp += i
    return temp

for i in li:
    for j in li:
        for k in li:
            for l in li:
                res = compute(i, j, k, l)
                if res == 36:

                    print(strProc(strProc('3{0}3{1}3{2}3{3}3={4}'.format(i,j,k,l,int(res)),'*','×'),'/','÷'))



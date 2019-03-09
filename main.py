def cycle(n):
    sum = 0
    for i in range(n):
        if i%3==0 or i%5==0:
            sum = sum + i

    print("\n Сумма чисел кратных 3 и 5, меньше ", n," равна ",sum)

cycle(11000)

def fibo(n):
    pred = 0
    pitem = 1
    item = 1
    sum = 0
    while pred<n:
        pred = pitem
        pitem = item
        item = pred+pitem

        print(item)
        if item%2==0:
            sum = sum + item


    print("\n Сумма чисел ряда Фибоначчи до ", n, " кратных 2м равна ", sum)

fibo(10)

a = 1
b = [2, 3, 4]
for i in range(1, 100):
    if i < 21 and i > 4:
        result = f'{i} процентов'
    elif (i % 10) == 1:
        result = f'{i} процент'
    elif (i % 10) in b:
        result = f'{i} процентa'
    else:
        result = f'{i} процентов'

    print(result)
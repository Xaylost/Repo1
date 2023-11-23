def calculator(*args, sign='сложить'):

    if sign == 'сложить':
        result = sum(args)
    elif sign == 'вычесть':
            result = args[0] - sum(args[1:])
    elif sign == 'умножить':
            result = 1
            for num in args:
                result *= num
    elif sign == 'разделить':
            result = args[0]
            for num in args[1:]:
                result /= num
    else:
            result = 'Неверно указано действие'

    return result
print(calculator(42,5235,12,1,6234634, sign= 'вычесть'))
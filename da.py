spisok =[34,1,23,5,44]


def a(spisok):
    number=[]
    while spisok > 0:
        number.append(spisok % 10)
        spisok = spisok // 10
    number.reverse()
    return(number)


def sort(l):
    l.sort(reverse = True)
    return list(map(a,l))
spisok = sort(spisok)
print(spisok)
number =[] 
for i in spisok:
    number+=i
print(number)


def ch(lst):
    num = 0
    for i in range(len(lst)):
        num = num * 10 + lst[i]
    return num


print(ch(number))
def max_recu(p, n):
    if n == 1:
        return p[0]
    else:
        max_rest = max_recu( p,  n-1)
        if max_rest > p[n-1]:
            return max_rest
        else:
            return p[n-1]
a = [5235,2,35,4,3444,21]
a1 = max_recu(a,(len(a)))
print(a1 )

def max_iterat(p):
    max_element = p[0]
    for i in range(1, len(p)):
        if p[i] > max_element:
            max_element = p[i]
    return max_element
print(max_iterat(a))
if a1 == max_iterat(a):
    print("Время одинаково")
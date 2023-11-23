def find_nums(n):
    assert n <= 27
    nums=[]
    for i in range(1,10):
        for o in range(10):
            for p in range(10):
                if i+o+p==n:
                    num=i*10**2+o*10**1+p*10**0
                    nums.append(num)
    return nums
                
print(find_nums(5))
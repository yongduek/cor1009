from scipy.special import factorial 

def sum_arrangements(num):
    nlst = [int(n) for n in list(str(num))]
    k = len(nlst)
    print(nlst)
    sn = sum(nlst)
    print('sn: ', sn)
    s1s = int('1'*k)
    f = factorial(k-1, exact=True)
    res = sn * s1s * f 
    print('sn*s1s', res, s1s, f)
    return res 


print(sum_arrangements(123))
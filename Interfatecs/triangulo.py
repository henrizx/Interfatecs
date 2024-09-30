import math

a,b,c = map(float,input().split())

if a > 0 and a <= 10**6 and b > 0 and b <= 10**6 and c > 0 and c <= 10**6:
    if (a+b >c) and (a+c>b) and (b+c>a):
        S = (a+b+c)/2
        area = math.sqrt(S*(S-a)*(S-b) * (S -c))
        print(f"{area:.2f}")
    else:
        print('Triangulo invalido!')
else:
    print('Errado!')
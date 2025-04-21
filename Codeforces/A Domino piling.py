m,n = map(int,input().split())

print((m*n//2))
'''
if m%2 == 0 and n % 2 == 0:
        print(int(m*n/2))
elif m%2 ==0 and n % 2 == 1:
        print(int((m*(n-1)+(n+1))/2))
elif m%2 == 1 and n % 2 == 0:
        print(int((n*(m-1)+(m+1))/2))
else:
        print(int(((n-1)*(m-1)+n+m-2)/2))'''
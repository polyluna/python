n,k = map(int,input().split())
arr = input()
l = list(map(int,arr.split(' ')))

count = 0
for i in range(n):
        if l[i]>0 and i<k :
                count +=1
        else:
                if l[i]>0 and l[i]==l[k-1]:
                        count +=1

print(count)


'''
n, k = map(int, input().split())
l = list(map(int, input().split()))

threshold = l[k - 1]  # the score to beat or tie
count = sum(1 for score in l if score >= threshold and score > 0)

print(count)
'''

'''
while True:
        if l[k-1] == 0:
                while i>= 0 and l[i] == 0:
                        i-=1
                print(i+1)
                break
        else:
                while i>= 0 and l[i] == l[k-1]:
                        i+=1
                print(i+1)
                break
'''
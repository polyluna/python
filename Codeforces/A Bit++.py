n = int(input())
count = 0

for _ in range(n):
        inp = input()
        if inp == "++X" or inp == "X++":
                count +=1
        else:    
                count -=1

print (count)

'''
n = int(input())
count = 0

for _ in range(n):
    inp = input()
    if "++" in inp:
        count += 1
    else:
        count -= 1

print(count)
'''
x = int(input())
y = {}

for _ in range (x) :
        y[_] = input()

for i in y :    
        if len (y[i]) <= 10 :
                print (y[i])
        else :
                print (y[i][0],len (y[i])-2,y[i][-1], sep='')
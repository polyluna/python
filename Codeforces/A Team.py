
n_question = int(input())
x = {}
n_question_do = 0

for _ in range(n_question):
        y = 0
        a, b, c= map(int,input().split())
        if a+b+c >= 2:
                n_question_do +=1

print (n_question_do)
'''
n_question = int(input())
n_question_do = sum(
    sum(map(int, input().split())) >= 2
    for _ in range(n_question)
)
print(n_question_do)
'''
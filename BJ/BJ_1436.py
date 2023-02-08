x = int(input())

result = 666
cnt = 0
num = 0

for i in range(0,x):
    if(i==0):
        continue
    if(cnt % 6 == 0):
        if(num == 0):
            num = num + 1
            continue
        num = num + 1
        if(num == 9):
            num=0
            cnt = cnt+1
    else:
        cnt = cnt + 1

print(str(cnt)+str(result))

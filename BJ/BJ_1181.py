n = int(input())
a = []
for i in range(0, n):
    temp = input()
    if(temp not in a):
        a.append(temp)
a_len = len(a)
a.sort()
for i in range(0, a_len-1):
    for  k in range(0, a_len-i-1):
        if(len(a[k]) > len(a[k+1])):
            temp = a[k]
            a[k] = a[k+1]
            a[k+1] = temp
for i in range(0, a_len):
    print(a[i])
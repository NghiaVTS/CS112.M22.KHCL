n = int(input())
lst = []
for i in range (n):
    lst.append(int(input()))
loi = 0
a=0
b=0
for i in range (n):
    sum = 0
    sum += lst[i]
    for j in range (i, n):
        if i != j: 
            sum += lst[j]
        if sum > loi:
            loi = sum
            a = i+1
            b = j+1
        j+=1
print(a," ", b, " ", loi)
    
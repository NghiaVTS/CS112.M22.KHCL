n = int(input())
lst = []
for i in range (n):
    lst.append(int(input()))
loi = 0
p=0
q=0
for i in range (n):
    sum = 0
    sum += lst[i]
    for j in range (i, n):
        if i != j: 
            sum += lst[j]
        if sum > loi:
            loi = sum
            p = i+1
            q = j+1
        j+=1
print(p," ", q, " ", loi)
    

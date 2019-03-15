n = eval(input())
like = input()
like = [eval(i) for i in like.split()]
q = eval(input())
store = []
for i in range(q):#循环q次
    listoftest = input()
    a = [eval(j) for j in listoftest.split()]
    store.append(a)

for i in range(q):
    count = 0
    target = store[i][2]
    for j in like[store[i][0]-1:store[i][1]-1]:
        if j==target:
            count += 1
    print(count)

input = open('input.txt', 'r')
lst = []
for j in range(10):
    s = input.readline()
    s = s.rstrip()
    a = list(map(int, s.split()))
    p = [(0 , 0)] * (int(len(a) / 2))
    for i in range(len(p)):
        p[i] = a[i*2], a[i*2 + 1]
    lst.append(p)
    print(lst[j])
input.close()    
    
    

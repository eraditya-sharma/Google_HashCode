import numpy as np
M, N = map(int, input().split())
main_s = np.array([int(x) for x in input().split()])
S=np.unique(main_s)
rv_array = np.argsort(-1*S)[:len(S)]
count=0
orders=np.array([])
for pizza in S[rv_array]:
    if (count+pizza)>=M:
        continue
    else:
        srch = np.where(main_s==pizza)[0]
        if len(srch)>1:
            for indices in srch:
                if (count+pizza)>=M:
                    continue
                else:
                    orders=np.insert(orders,0,indices)
                    count+=pizza
        else:
            orders=np.insert(orders,0,srch)
            count+=pizza 
print(len(orders))
print(" ".join(map(str, orders.astype(int))))


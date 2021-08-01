def next_smaller(n):
    nda = list(str(n))
    nda.sort()
    if(n == int(''.join(nda))):
        return -1

    n = str(n)
    f = False
    for i in range(len(n)-1,-1,-1,):
        for j in range(len(n)-1,i,-1):
            if(n[j] < n[i]):
                f = True
                break
        if(f == True):
            break
    n = list(n)
    n[i],n[j] = n[j],n[i]
    nd1,nd2 = n[:i+1],n[i+1:]
    nd2.sort(reverse=True)
    ndr = nd1 + nd2
    return int(''.join(ndr)) if ndr[0] != "0" else -1

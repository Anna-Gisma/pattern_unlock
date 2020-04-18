def PatternUnlock(N, hits):
    c = float(0)
    diag = 2**0.5
    result = 0
    r = []
    q = 0
    i = 0
    m = 100000
    r_result = 0
    if N == 0:
       return None
    
    else:
        for i in range(N):
            if hits[i] == 1:
                if N == i+1:
                    break
                else:
                    if hits[i+1] == 6 or hits[i+1] == 2 or hits[i+1] == 9:
                        c += 1
                    elif hits[i+1] == 3:
                        c += 2
                    else:
                        c += diag
            elif hits[i] == 2:
                if N == i+1:
                    break
                else:
                    if (hits[i+1] == 1 or hits[i+1] == 5 or hits[i+1] == 8
                                                or hits[i+1] == 3):
                        c += 1
                    else:
                        c += diag
            elif hits[i] == 3:
                if N == i+1:
                    break
                else:
                    if hits[i+1] == 4 or hits[i+1] == 2 or hits[i+1] == 7:
                        c += 1
                    elif hits[i+1] == 1:
                        c += 2
                    else:
                        c += diag
            elif hits[i] == 4:
                if N == i+1:
                    break
                else:
                    if hits[i+1] == 3 or hits[i+1] == 5:
                        c += 1
                    elif hits[i+1] == 9:
                        c += diag*2
                    elif hits[i+1] == 6 or hits[i+1] == 7:
                        c += 2
                    else:
                        c += diag
            elif hits[i] == 5:
                if N == i+1:
                    break
                else:
                    if hits[i+1] == 4 or hits[i+1] == 2 or hits[i+1] == 6:
                        c += 1
                    elif hits[i+1] == 8:
                        c += 2
                    else:
                        c += diag
            elif hits[i] == 6:
                if N == i+1:
                    break
                else:
                    if hits[i+1] == 5 or hits[i+1] == 1:
                        c += 1
                    elif hits[i+1] == 7:
                        c += diag*2
                    elif hits[i+1] == 4 or hits[i+1] == 9:
                        c +=2
                    else:
                        c += diag
            elif hits[i] == 7:
                if N == i+1:
                    break
                else:
                    if hits[i+1] == 3 or hits[i+1] == 8:
                        c += 1
                    elif hits[i+1] == 6:
                        c += diag*2
                    elif hits[i+1] == 4 or hits[i+1] == 9:
                        c +=2
                    else:
                        c += diag
            elif hits[i] == 8:
                if N == i+1:
                    break
                else:
                    if hits[i+1] == 7 or hits[i+1] == 2 or hits[i+1] == 9:
                        c += 1
                    elif hits[i+1] == 5:
                        c += 2
                    else:
                        c += diag
            else:
                if N == i+1:
                    break
                else:
                    if hits[i+1] == 1 or hits[i+1] == 8:
                        c += 1
                    elif hits[i+1] == 7:
                        c += diag*2
                    elif hits[i+1] == 6 or hits[i+1] == 7:
                        c +=2
                    else:
                        c += diag
    if N == 1:
        return int(c)
    else:
        q = c*m
        k = int(q)
        i = int((q - k)*10)
        if i >= 5:
            k += 1
        result = list(str(k))
        for el in result:
            if el != '0':
                r.append(str(el))
        r_result = ''.join(r)

        return r_result


               

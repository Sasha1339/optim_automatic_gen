

def generate(f_discret, f1, f2, sig1, sig2):
    f = abs(f1 - f2)
    f_d = int(f_discret / (f * 2) + 1)
    isPlus = True
    discr_value = 1 / (f_d)
    saw = [0]
    for i in range(1, len(sig1)-1, 1):
        if i % f_d == 0:
            isPlus = not isPlus
        if isPlus:
            saw.append(saw[i-1] + discr_value)
        else:
            saw.append(saw[i - 1] - discr_value)
    return saw
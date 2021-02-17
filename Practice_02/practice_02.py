def f21(x):
    if x[2] == 1994:
        if x[1] == 1981:
            if x[4] == 'plsql':
                if x[0] == 'nesc':
                    return 0
                elif x[0] == 'nsis':
                    return 1
                elif x[0] == 'oz':
                    return 2
            elif x[4] == 'xml':
                if x[3] == 1963:
                    return 3
                elif x[3] == 2017:
                    return 4
                elif x[3] == 1962:
                    return 5
        elif x[1] == 1985:
            return 6
    elif x[2] == 2004:
        if x[1] == 1981:
            if x[0] == 'nesc':
                if x[4] == 'plsql':
                    return 7
                elif x[4] == 'xml':
                    return 8
            elif x[0] == 'nsis':
                if x[4] == 'plsql':
                    return 9
                elif x[4] == 'xml':
                    return 10
            elif x[0] == 'oz':
                return 11
        elif x[1] == 1985:
            return 12
    elif x[2] == 2006:
        return 13


def f22(x):
    str_bin = str(bin(x))[2:]
    if len(str_bin) < 32:
        str_bin = '0' * (32 - len(str_bin)) + str_bin
    a_str_bin = str_bin[-15:]
    b_str_bin = str_bin[-29:-15]
    c_str_bin = str_bin[:-29]
    return int(a_str_bin + c_str_bin + b_str_bin, 2)

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
    str_hex = str(hex(int(a_str_bin + c_str_bin + b_str_bin, 2)))
    if len(str_hex) < 10:
        return str(str_hex[:2] + '0' * (10 - len(str_hex)) + str_hex[2:])
    return hex(int(a_str_bin + c_str_bin + b_str_bin, 2))


def f23(x):
    res = []
    tmp_arr = []
    for i in range(len(x)):
        while None in x[i]:
            x[i].remove(None)
        tmp_arr.append(list())
        for tmp in x[i]:
            if tmp not in tmp_arr[i]:
                tmp_arr[i].append(tmp)
        res.append(list())
        res[i].append(int(tmp_arr[i][0].split(':')[1][:-1]) / 100)
        res[i].append(tmp_arr[i][0].split(':')[0][5:])
        res[i].append(tmp_arr[i][1].replace('-', '.'))
        res[i].append(tmp_arr[i][2].split(' ')[1].split('.')[0] + '. ' + tmp_arr[i][2].split(' ')[0])
    return res


print(f23([[None, None, '+74327612358:99%', None, '17-03-01', 'Шуфский Н.М.','17-03-01', 'Шуфский Н.М.'],
           [None, None, '+70939609830:1%', None, '07-10-01', 'Кесушяк Л.С.','07-10-01', 'Кесушяк Л.С.'],
           [None, None, '+74999760260: 6%', None, '10-06-04', 'Мекетев Г.Т.','10-06-04', 'Мекетев Г.Т.'],
           [None, None, '+75196019960:96%', None, '12-11-03', 'Токев Ф.О.','12-11-03', 'Токев Ф.О.']]))

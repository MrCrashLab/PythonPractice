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
    c = (x & ((2 ** 32 - 1) & ~(2 ** 29 - 1))) >> 15
    b = (x & ((2 ** 29 - 1) & ~(2 ** 15 - 1))) >> 15
    a = (x & (2 ** 15 - 1)) << 17
    return a | b | c


def f23(x):
    tmp_arr = []
    arr = []
    res = []
    for i in [list(i) for i in zip(*x)]:
        if not all(tmp is None for tmp in i):
            tmp_arr.append(i)
    for tmp in tmp_arr:
        if tmp not in arr:
            arr.append(tmp)
    arr = [list(i) for i in zip(*arr)]
    for i in range(len(arr)):
        res.append(list())
        line = str(int(arr[i][0].split(':')[1][:-1]) / 100)
        if len(line) < 4:
            res[i].append(line + '0')
        else:
            res[i].append(line)
        res[i].append(str('0' * (7 - len(str(int(arr[i][0].split(':')[0][5:])))) + \
                          str(int(arr[i][0].split(':')[0][5:]))))
        res[i].append(arr[i][1].replace('-', '.'))
        res[i].append(arr[i][2].split(' ')[1].split('.')[0] + '. ' + arr[i][2].split(' ')[0])
    return res


uyt = [([[None, None, '+74327612358:99%', '17-03-01', 'Шуфский Н.М.', 'Шуфский Н.М.'],
         [None, None, '+74999760260:6%', '10-06-04', 'Мекетев Г.Т.', 'Мекетев Г.Т.'],
         [None, None, '+75196019960:96%', '12-11-03', 'Токев Ф.О.', 'Токев Ф.О.'],
         [None, None, '+72124416492:69%', '28-07-02', 'Фовян А.О.', 'Фовян А.О.']],
        [['0.99', '7612358', '17.03.01', 'Н. Шуфский'], ['0.06', '9760260', '10.06.04', 'Г. Мекетев'],
         ['0.96', '6019960', '12.11.03', 'Ф. Токев'], ['0.69', '4416492', '28.07.02', 'А. Фовян']]),

       ([[None, None, '+70939609830:1%', '07-10-01', 'Кесушяк Л.С.', 'Кесушяк Л.С.'],
         [None, None, '+74034009153:98%', '02-03-04', 'Фобов В.Т.', 'Фобов В.Т.'],
         [None, None, '+73402641650:28%', '08-08-01', 'Гашочак Т.И.', 'Гашочак Т.И.'],
         [None, None, '+72307668959:2%', '20-12-04', 'Ценебберг Р.Е.', 'Ценебберг Р.Е.']],
        [['0.01', '9609830', '07.10.01', 'Л. Кесушяк'], ['0.98', '4009153', '02.03.04', 'В. Фобов'],
         ['0.28', '2641650', '08.08.01', 'Т. Гашочак'], ['0.02', '7668959', '20.12.04', 'Р. Ценебберг']]),

       ([[None, None, '+79274667211:50%', '28-09-99', 'Бичов В.З.', 'Бичов В.З.'],
         [None, None, '+70185021746:22%', '16-01-04', 'Леков А.З.', 'Леков А.З.'],
         [None, None, '+75167657965:81%', '28-04-04', 'Тетак Н.В.', 'Тетак Н.В.'],
         [None, None, '+78069313138:10%', '14-09-02', 'Сенберг И.Ч.', 'Сенберг И.Ч.']],
        [['0.50', '4667211', '28.09.99', 'В. Бичов'], ['0.22', '5021746', '16.01.04', 'А. Леков'],
         ['0.81', '7657965', '28.04.04', 'Н. Тетак'], ['0.10', '9313138', '14.09.02', 'И. Сенберг']]),

       ([[None, None, '+70643533587:64%', '25-05-99', 'Лософук Т.В.', 'Лософук Т.В.'],
         [None, None, '+78745751203:58%', '07-06-99', 'Цозеций Б.Е.', 'Цозеций Б.Е.'],
         [None, None, '+73145210516:7%', '28-12-99', 'Шизский С.О.', 'Шизский С.О.'],
         [None, None, '+77181333422:91%', '12-05-02', 'Сишиди М.Л.', 'Сишиди М.Л.']],
        [['0.64', '3533587', '25.05.99', 'Т. Лософук'], ['0.58', '5751203', '07.06.99', 'Б. Цозеций'],
         ['0.07', '5210516', '28.12.99', 'С. Шизский'], ['0.91', '1333422', '12.05.02', 'М. Сишиди']]),

       ([[None, None, '+74055939098:16%', '18-03-01', 'Китубич Р.В.', 'Китубич Р.В.'],
         [None, None, '+75938569820:18%', '09-12-99', 'Фачян Л.З.', 'Фачян Л.З.'],
         [None, None, '+78767708675:47%', '02-12-00', 'Гезяк Я.О.', 'Гезяк Я.О.'],
         [None, None, '+79471156791:32%', '18-08-00', 'Чалский Д.А.', 'Чалский Д.А.']],
        [['0.16', '5939098', '18.03.01', 'Р. Китубич'], ['0.18', '8569820', '09.12.99', 'Л. Фачян'],
         ['0.47', '7708675', '02.12.00', 'Я. Гезяк'], ['0.32', '1156791', '18.08.00', 'Д. Чалский']]),

       ([[None, None, '+78062719559:19%', '08-06-99', 'Цадатянц А.Р.', 'Цадатянц А.Р.'],
         [None, None, '+71055890793:70%', '07-08-03', 'Зизиди П.О.', 'Зизиди П.О.'],
         [None, None, '+78222967913:73%', '27-08-00', 'Вачавберг Д.Б.', 'Вачавберг Д.Б.']],
        [['0.19', '2719559', '08.06.99', 'А. Цадатянц'], ['0.70', '5890793', '07.08.03', 'П. Зизиди'],
         ['0.73', '2967913', '27.08.00', 'Д. Вачавберг']]),

       ([[None, None, '+79470930730:31%', '20-04-99', 'Сулерянц А.Ш.', 'Сулерянц А.Ш.'],
         [None, None, '+74901928891:60%', '04-11-00', 'Чишузий М.Ч.', 'Чишузий М.Ч.'],
         [None, None, '+79310014023:57%', '07-07-99', 'Лосакберг И.Е.', 'Лосакберг И.Е.']],
        [['0.31', '0930730', '20.04.99', 'А. Сулерянц'], ['0.60', '1928891', '04.11.00', 'М. Чишузий'],
         ['0.57', '0014023', '07.07.99', 'И. Лосакберг']]),

       ([[None, None, '+76965953356:59%', '14-12-99', 'Цемин А.Т.', 'Цемин А.Т.'],
         [None, None, '+79901220807:6%', '26-08-01', 'Лодезман Д.С.', 'Лодезман Д.С.'],
         [None, None, '+73144639696:46%', '14-03-01', 'Мелашянц Т.А.', 'Мелашянц Т.А.'],
         [None, None, '+79469935923:54%', '02-09-02', 'Чусокли А.С.', 'Чусокли А.С.']],
        [['0.59', '5953356', '14.12.99', 'А. Цемин'], ['0.06', '1220807', '26.08.01', 'Д. Лодезман'],
         ['0.46', '4639696', '14.03.01', 'Т. Мелашянц'], ['0.54', '9935923', '02.09.02', 'А. Чусокли']])]

for tmp in uyt:
    if f23(tmp[0]) == tmp[1]:
        print(True)
    else:
        print(False)

print(f23([[None, None, '+79470930730:31%', '20-04-99', 'Сулерянц А.Ш.', 'Сулерянц А.Ш.'],
           [None, None, '+74901928891:60%', '04-11-00', 'Чишузий М.Ч.', 'Чишузий М.Ч.'],
           [None, None, '+79310014023:57%', '07-07-99', 'Лосакберг И.Е.', 'Лосакберг И.Е.']]))

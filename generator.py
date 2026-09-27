def gener(put_klast):
    import random
    #Генерим размеры вспомогателного(обычного) лабиринта
    a = 12
    b = 24
    #список рёбер вспомогательного лабиринта
    ar = []
    #делаем "лучше" 2 алгоритма (пустые столбец и строка в рандомных местах
    col = random.randint(0, b-1)
    row = random.randint(0, a-1)
    #заносим то, что они пустые в  список
    for i in range (a-1):
        ar.append([[col, i], [col, i+1]])
    for j in range (b-1):
        ar.append([[j, row], [j+1, row]])
    #идём по остальным клеткам
    for i in range(b):
        for j in range(a):
            if i != col and j != row:    #с такими клетками, где "=" +- разобрались
                # выбираем сторону, в которую ходим(0 - горизонталь, 1 - вертикаль)
                go = random.randint(0, 1)
                # Теперь делаем так, чтоб стрелки смотрели внутрь лабиринта
                if go == 0:
                    if i < col:
                        ar.append([[i, j], [i+1, j]]) #стрелка вправо
                    else:
                        ar.append([[i-1, j], [i, j]]) #стрелка влево
                else:
                    if j < row:
                        ar.append([[i, j], [i, j+1]]) #стрелка вниз
                    else:
                        ar.append([[i, j-1], [i, j]]) #стрелка вверх
    #Мы сделали вспомагательный лабиринт. Он состоит из клеток (нч, нч) итогового, если индексы с 0
    #Размеры итогового q x w - от 7х7 до 201х201
    q = 2*a + 1
    w = 2*b + 1
    #Создаём заготовку для файла только из стенок
    fil = []
    for i in range(q):
        fil.append([])
        for j in range(w+1):
            fil[-1].append(("█"))
    # Заполняем рёбра
    for k in ar:
        #рассматриваем 2 вида пар вершин
        if k[1][0] == k[0][0] + 1:
            fil[2 * k[0][1] + 1][2 * k[0][0] + 1] = "·"
            fil[2 * k[0][1] + 1][2 * k[0][0] + 3] = "·"
            fil[2 * k[0][1] + 1][2 * k[0][0] + 2] = "·"
        if k[1][1] == k[0][1] + 1:
            fil[2 * k[0][1] + 1][2 * k[0][0] + 1] = "·"
            fil[2 * k[0][1] + 3][2 * k[0][0] + 1] = "·"
            fil[2 * k[0][1] + 2][2 * k[0][0] + 1] = "·"
    n = random.randint(0, a-1)
    m = random.randint(0, a-1)
    fil[2 * n + 1][0] = "S"
    fil[2 * m + 1][-1] = "F"
    fil[2 * m + 1][-2] = "·"
    for i in range(25):
        if i % 2 == 1:
            fil[i][-2] = "·"
    for k in range(len(fil)):
        fil[k] = "".join(fil[k])+"\n"
    lab = open(put_klast, "w", encoding="utf-8")
    lab.writelines(fil)
    lab.close()

def Tinh_Tong(st1, st2):
    st3 = 0
    st3 = int(st1)+int(st2)
    return st3


tinhtong = Tinh_Tong(1, 2)
print(tinhtong)


def Tinh_Tong2(st1, st2):
    st3 = 0
    st3 = int(st1)+int(st2)
    return st3, st1


tinhtong = Tinh_Tong2(1, 2)
print(tinhtong)


def Get_Age(lst):
    a = 0
    for i in lst:
        if i['address'] == 'Da Nang':
            a = i['age']
    return a


def Get_xyz(lst):
    a = ''
    for i in range(0, len(lst)-0):
        for j in lst[i].keys():
            if j == 'body':
                for z in lst[i][j].keys():
                    if z == 'abc':
                        for v in lst[i][j][z].keys():
                            if v == 'xyz':
                                a = lst[i][j][z][v]
    return a


    # return a
lst = [
    {
        'name': 'tuan1',
        'age': 21,
        'address': 'Da Nang'
    },
    {
        'name': 'tuan2',
        'age': 22,
        'address': 'Ha Noi'
    },
    {
        'name': 'tuan3',
        'age': 23,
        'address': 'TP HCM'
    },
    {
        'name': 'tuan3',
        'age': 23,
        'address': 'TP HCM',
        'body': {
            'height': 172,
            'weight': 70,
            'abc': {
                'xyz': 'ok',
                'bcd': 'welcome'
            }
        }
    }
]
print(Get_Age(lst))
print(lst[3].keys())
print(Get_xyz(lst))

lst=[
    {
        'name':'Minh Tuan',
        'age':32,
    },
    {
        'name':'Tuan Minh',
        'age': 25,
    }
]
print(lst[0])
print(type(lst[0]))
print(lst[0].get('name'))
detail=lst[0]
print(detail)
lst.append({'name':'dsfs'})
print(lst)

lst2=[1,2,3,4,5,6,7]
print(lst2)
lst2.remove(1) # 1 la pt dau tien chu khong phai 0
print(lst2)

lst3=[0,[1,'tuantn']]
print(lst3[1][1])

lst1=[1,2,3,4,5]
lst2=[1,2,3,4,5]
lst3=[3,4,5]
lst1.extend(lst3)
print(lst1)
lst2.append(3)
print(lst2)

print(7 not in lst1)
print(3 in lst1)
print(lst1.index(3)) #tra ve vi tri phan tu trong mang

print(max(lst1))
print(min(lst1))

print("Hello world")
# tuple: la 1 dang list nhung k cho chinh sua du lieu (read-only)
tup = ()

lstContent = [
    {
        'title': 'title1',
        'image': 'link1'
    },
    {
        'title': 'title2',
        'image': 'link2'
    }
]
print("lstContent")
print(lstContent)
print("type(lstContent)")
print(type(lstContent))
print("lstContent[0]")
print(lstContent[0]['title'])
for obj in lstContent:
    print(obj)
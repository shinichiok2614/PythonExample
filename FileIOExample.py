""" mode:
    r: read-only, mặc định nếu k khai báo
    rb: mở dạng nhị phân
    w: tạo file mới để ghi
    wb: dạng nhị phân
    a: mở file để ghi thêm vào cuối
    ab: dạng nhị phân
encoding:
    None
    utf-8 """
# f=open('tuan','w',encoding='utf-8')
f=open('tuan','r',encoding='utf-8')
print(f.read())
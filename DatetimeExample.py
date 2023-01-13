from datetime import datetime,date
d=date(2022,12,5)
print(d)
d1=datetime.now()
print(d1)
d2=datetime(2022,1,1,1,1,1,1)
print(d2)
print(d2.hour)
print(d2.year)
d3=d2.strftime('%d-%m-%Y')
print(d3)
print(type(d3))
d4=d2.strftime('%d-%m-%Y %H:%M:%S') # định dạng hiện
print(d4)
d5=datetime.strptime(d4,'%d-%m-%Y %H:%M:%S') # định dạng parsing
print(d5)
print(type(d5))

# dt1=input('Nhap ngay thang nam thu nhat')
# dt2=input('Nhap ngay thang nam thu hai')
dt1='2/3/2000'
dt2='2/3/2001'
_dt1=datetime.strptime(dt1, '%d/%m/%Y')
_dt2=datetime.strptime(dt2, '%d/%m/%Y')
duration=_dt2-_dt1
days=duration.days
print(days)
days=duration.max
print(days)
days=duration.min
print(days)
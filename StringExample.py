print('Tuan'.lower())
print('Tuan'.upper())
print('Tuan'.replace('an','sfasdf'))
print(len('sdfsdf'))
str1='sdnfansf'
s=0
print(str1[0])
for i in str1:
    if i=='n': s+=1
print(s)
print(str1[0:])
print(str1[0::])
print(str1[0::2])
print(str1[:4])
print(str1[::4])
print(str1[0:6:2])
print('Tim boi so tu 1 den 50 cua so nguyen')
songuyen=5
str1=''
for i in range(1,50):
    if(i%songuyen==0):
        str1+=str(i)+','
print(str1)
print('Tim cac so chan tu 1 den n')
n=9
str1=''
for i in range(1,n):
    if i%2==0:
        str1+=str(i)+','
print(str1)

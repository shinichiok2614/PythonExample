#set: k chua phan tu trung nhau, k su 
s=set([1,1,1,1,2,2,2,3,4])
print(s)
s.add(5)
print(s)
s.remove(2)
print(s)
print(6 not in s)
print(3 in s)
s2=set([12,33,5,5,3,2,2,1,1,1])
s3=s.union(s2)  #phep hop
print(s3)
s4=s.intersection(s2) #phep giao
print(s4)
s5=s.difference(s2) #s\s2
print(s5)
s6=s2.difference(s) #s2\s
print(s6)

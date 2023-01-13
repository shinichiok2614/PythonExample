import re

pattern='^a...s$'
text_string='abyss'
print("text_string='abyss'")
result=re.match(pattern,text_string)
r='ok' if result else 'not ok'; print(r)

pattern='ma?n'
text_string='mannnn'
print('text_string=''mannnn''')
result=re.match(pattern,text_string)
r='ok' if result else 'not ok'; print(r)

pattern='[0-9]{2,3}' # chuoi toi thieu 2 toi da 4 nhung k co gioi han toi da
text_string='2236634234sfaaaaaaamaannnn'
print('text_string=''2236634234sfaaaaaaamaannnn''')
result=re.match(pattern,text_string)
r='ok' if result else 'not ok'; print(r)

pattern='a{2,3}'
text_string='aaaaadfsfdq432'
print('text_string=''aaaaadfsfdq432''')
result=re.match(pattern,text_string)
r='ok' if result else 'not ok'; print(r)

pattern='a|b'
text_string='asdfsf'
print('text_string=''asdfsf''')
result=re.match(pattern,text_string)
r='ok' if result else 'not ok'; print(r)

pattern='(a|b|c)xy'
text_string='axy'
print('text_string=''axy''')
result=re.match(pattern,text_string)
r='ok' if result else 'not ok'; print(r)

pattern='\Athe' # đầu chuỗi
text_string='thethedsfsd sun'
print('text_string=''the sun''')
result=re.match(pattern,text_string)
r='ok' if result else 'not ok'; print(r)

pattern='\\bfoo' # đầu hoặc cuối từ, lưu ý \\ vì trùng với \ của print
text_string='football'
print('text_string=''football''')
result=re.match(pattern,text_string)
r='ok' if result else 'not ok'; print(r)

pattern='\\bfoo' # đầu hoặc cuối từ
text_string='a football'
print('text_string=''a football''')
result=re.match(pattern,text_string)
r='ok' if result else 'not ok'; print(r)

result=re.match('foo\b','foo')
print('foo\\b')
r='ok' if result else 'not ok'; print(r)

result=re.match("foo\b",'foo')
print('foo\\b')
r='ok' if result else 'not ok'; print(r)

result=re.match("\\Bfoo",'sfoofdsd')
print('foo')
r='ok' if result else 'not ok'; print(r)

result=re.match("\d",'12sfoofdsd') # có số
print('d')
r='ok' if result else 'not ok'; print(r)

result=re.match("\D",'sfoofdsd') # k có số
print('D')
r='ok' if result else 'not ok'; print(r)

result=re.match("\s",' ádf') # khoảng trắng
print('s')
r='ok' if result else 'not ok'; print(r)

result=re.match("\S",'ádf') # k khoảng trắng
print('S')
r='ok' if result else 'not ok'; print(r)

result=re.match("\w",'asf') #a-z A-Z 0-9 _ # lưu ý _
print('w')
r='ok' if result else 'not ok'; print(r)

result=re.match("\W",'%') # a-z A-Z 0-9 _
print('W')
r='ok' if result else 'not ok'; print(r)

result=re.match("\W",'%') # 
print('W')
r='ok' if result else 'not ok'; print(r)

print('findall')
result=re.findall("\w", "sdfa wfw 234 n+_=-") # trả về chuỗi khớp cú pháp
print(result)
result=re.findall("\w+", "sdfa wfw 234 n+_=-") # trả về chuỗi khớp cú pháp
print(result)
print('r')
result=re.findall(r"\w", "\wsdfa wfw 234 n+_=-") # trả về chuỗi khớp cú pháp
print(result)


result=re.split('\s', 'sdfasdfadfsad sdfsdf sdfsdfsd df')
print(result)

result=re.split('\s', 'sdfasdfadfsad sdfsdf sdfsdfsd df',1) # ngắt 1 chuỗi đầu
print(result)

result=re.split('\s', 'sdfasdfadfsad sdfsdf sdfsdfsd df',2) # ngắt 2 chuỗi đầu
print(result)

str1='sfd sfd sadf sadf sa dfsa dfsafd asdf'
result=re.sub('\s', '-', str1)
print(result)
print(type(result))

str1='sfd sfd sadf sadf sa dfsa dfsafd asdf' # hien so lan chèn
result=re.subn('\s', '-', str1)
print(result)
print(type(result))


str1='sfd sfd sadf sadf sa dfsa dfsafd asdf'
result=re.sub('\S', '-', str1)
print(result)

str1='sfd sfd sadf sadf sa dfsa dfsafd asdf'
result=re.sub('\s', '-', str1,2)
print(result)

result=re.search('\Aquantri','quantrimang.com')
r='ok' if result else 'not ok'; print(r)

result=re.search('\Aquantri','quantrimang.com')
r='ok' if result else 'not ok'; print(r)

str1 = '39801 356, 2102 1111'
match=re.search('(\d{3}) (\d{2})', str1)
print(match.group())
print(match.group(1))
print(match.group(2))
print(match.start()) # index của group 1
print(match.end()) # index cuoi cung của group 2
print(match.span()) # tuple
print(type(match.span()))
print(match.re) # trả về regex
print(match.string)

string = '\n \w and \r are escape sequences.'
result = re.findall(r'[\n\r]', string) 
print(result)
result = re.findall(r'[\n]', string) 
print(result)
result = re.findall(r'[\w]', string) 
print(result)




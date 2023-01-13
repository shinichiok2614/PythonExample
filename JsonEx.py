# Vi du XML SOAP
# <listContent>
#     <content>
#         <title> title1 </title>
#         <image> image1 </image>
#     </content>
#     <content>
#         <title> title2 </title>
#         <image> image2 </image>
#     </content>
#     <content>
#         <title> title3 </title>
#         <image> image3 </image>
#     </content>
# </listContent>

#JSON bản chất là dictionary
import requests
import json
# pip install requests
# callApi=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
# print(callApi)
# callApi=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').text
# print(callApi)
callApi=requests.get('https://www.boredapi.com/api/activity/').text
print(callApi)
print(type(callApi))
res=json.loads(callApi)
print(res)
print(type(res))
print(res["activity"])
print(res.items())
print(res.keys())
print(res.values())
[print(i) for i in res]
[print(i) for i in res.values()]
# phải biết kiểu dữ liệu của nó là gì thì mới biết cách xử lý phù hợp

print("Hello world")
# tuple: la 1 dang list nhung k cho chinh sua du lieu (read-only)
# tup = ()

# lstContent = [
#     {
#         'title': 'title1',
#         'image': 'link1'
#     },
#     {
#         'title': 'title2',
#         'image': 'link2'
#     }
# ]
# print("lstContent")
# print(lstContent)
# print("type(lstContent)")
# print(type(lstContent))
# print("lstContent[0]")
# print(lstContent[0]['title'])
# for obj in lstContent:
# print(obj)

'''
TCP/IP (Transmission Control Protocol/Internet Protocol)
Giao thức chuyển và nhận liên mạng

Tầng vật lý truyền tải dữ liệu trong cùng 1 mạng
Tầng internet để truyền chung
Tầng transport xử lý vấn đề giao tiếp giữa các máy chủ, định tuyến
Bộ định tuyến: tạo đường mạng kết nối những máy muốn trao đổi dữ liệu với nhau
Tầng ứng dụng
'''
# import socket
# HOST='127.0.0.1'
# PORT=8080
# CLIENT_ID='cl1'
# s=socket.socket()
# s.connect((HOST,PORT))
# s.send(CLIENT_ID.encode())
# data=s.recv(4096)
# print(data.decode())
# s.close()


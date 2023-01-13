#Thread va Process

# process:
#     code
#     static data
#     dynamic data
#     stack
# static data: là các biến được khai báo tường minh
# dynamic data: là bộ nhớ biến có thể thay đổi

# product={} là dynamic data vì size nó có thể thay đổi
# stack: phục vụ cho việc gọi hàm
# caching trong django
# cpu scheduler

# Tạo process
#     Do hệ thống tự tạo theo nhu cầu quản lý hệ thống
#     Do user chạy 1 phần mềm
#     Do giải thuật của 1 phần mềm đang chạy (gọi dịch vụ CreateProcess để tạo process mới theo nhu cầu riêng)
# process bị chuyển trạng thái
# trạng thái vĩ mô và vi mô
    # vĩ mô: là trạng thái do HĐH quy định
    # 3 trạng thái process: running, blocked, ready
    # vi mô: là trạng thái sau khi thực hiện lệnh máy
"""
    str --> list
        列表 = 字符串.split("分隔符")
    练习:exercise07
"""
# 使用字符串记录的多个数据
message = "张无忌-翠山-张三丰"
# 转换为使用列表存储
list_result = message.split("-")
print(list_result)

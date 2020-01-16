"""
    列表推导式
     将一个可迭代对象，转换为列表。

     [对变量的处理 for 变量 in 可迭代对象 if 条件]
"""
list01 = [4, 54, 5, 6, 7, 8]
# list02 = []
# for item in list01:
#     list02.append(item + 1)
list02 = [item + 1 for item in list01]

# list02 = []
# for item in list01:
#     if item % 2:
#         list02.append()
list02 = [item ** 2 for item in list01 if item % 2]

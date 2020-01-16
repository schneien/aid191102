"""一、练习
1. 创建列表存储下列行星:
    "金星","地球","木星","土星"
2. 补全八大行星
3. 打印距离太阳最近的行星(第一个元素)、最远的行星(最后)
4. 打印前三个行星、火星后面所有行星。(多个元素)
5. 删除天王星;删除太阳到地球之间的行星(前两个)
6. 反向打印所有行星(一行一个)
"""
# 1. 创建列表存储下列行星:
list_planets = ["金星", "地球", "木星", "土星"]
# 2. 补全八大行星
list_planets.insert(0, "水星")
list_planets.insert(3, "火星")
# list_planets.append("天王星")
# list_planets.append("海王星")
list_planets[len(list_planets):] = ["天王星", "海王星"]
# 3. 打印距离太阳最近的行星(第一个元素)、最远的行星(最后)
print(list_planets[0])
print(list_planets[-1])
# 4. 打印前三个行星、火星后面所有行星。(多个元素)
print(list_planets[:3])
print(list_planets[4:])
# 5. 删除天王星;删除太阳到地球之间的行星(前两个)
list_planets.remove("天王星")
del list_planets[:2]
# 6. 反向打印所有行星(一行一个)
for i in range(len(list_planets) - 1, -1, -1):
    print(list_planets[i])

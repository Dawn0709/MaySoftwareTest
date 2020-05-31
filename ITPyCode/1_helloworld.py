print("hello world")

"""
这个是多行注释，单行注释ctrl+/，块注释Alt+shift+A
"""

# 用来输入内容的api，键盘键入值
""" aa = input()
print(aa) """

""" # 字符串
a = "这个是我赋值的内容"
print(a)

# 数字/整型
b = 100
print(b)

# bool类型
c = True
d = False
print(c)
print(d)

# 空类型，啥都没有，但存在
e = None
print(e) """

# 元组()

""" f = () # 空元组，它的类型是元组，但是元组里面没有东西
f = (1,2,3,4,5,6) # 元素和元素之间使用逗号隔开

f = (1,"python", True, None, 8, "demo", "漂洋过海","python")# 元组的元素可以是任意类型的

print("f的长度是：",len(f)) # len统计长度（元素的个数）
print("python出现的次数",f.count("python"))  # count统计该元素出现的次数

name = "wangyao"
print("wangyao中a出现的次数：",name.count("a"))


print("python在f元组中的位置是：",f.index(8))# index找到出现元素的下标# index找到出现元素的下标 """

# list 数组

""" g = [1,2,3,4,5,6]
g = [1,"python",True,None,"python"]
# append添加元素
g.append("增加第一个")
g.append("哎哟喂")
print(g)
# remove移除指定元素，只执行一次
g.remove("python")
print(g)
# insert指定位置添加元素
g.insert(3,"我是第四个")
print(g)
# 通过元素下标修改内容
g[2] = "噔噔噔"
print(g)
# clear清空元素
g.clear()
print(g)
print("————————这是一条分割线————————")

# sort冒泡排序———从小到大
gg = [54,78,132,576,4,16,47,65,320]
gg.sort()
print(gg)
# reverse倒序
gg.reverse()
print(gg) """

# 字典：接口测试的json格式————key：键
# username为key值，wangyao为value值，他们为一对，用冒号隔开
users = {"username":"wangyao","gf":None}
# 取值
print(users.get("username"))
print(users["gf"])
""" # get如果取不存在的键，则返回none，使用[]取不存在的键，则报错
print(users.get("name"))
users["bf"] """
# 添加
users["bf"] = "鸣翠柳"
print(users.get("bf"))


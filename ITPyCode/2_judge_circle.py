

# 判断
""" a = input("请问shuzhan是不是憨憨，1：是；0：不是：")
if a == "1":
    print("hhhhh敢敢有心")
else:
    print("小天才你好呀")
 """

# is/is not，跟==和!=类似
""" c = 123
d = 321
if c is d:
    print("c和d的类型相同")
else:
    print("c和d的类型不相同") """



# in/not in判断两值的包含关系
""" f = "python"
g = "I love python"
if f in g:
    print("f在g里面出现过")
else:
    print("f没在g里面出现过")

h = "Good"
i = "Good afternoon"
if h in i:
    print("h在i里出现过")
else:
    print("h没在i里出现过") """

# 循环
# for循环
for i in range(10):
    print("python好简单噢：",i)

# 遍历str/()/[]/{}

a = "的金发科技的开发将飞机阿萨德出现"
for i in a:
    print(i)
# 循环字典的第一种方式
a = {"username":"test","password":"123456"}
for i in a:
    # print("遍历出来的是键值：value值；",i,":",a.get(i))
    print(i)
    print(a.get(i))
    # print(a[i])    
    

# 循环字典的第二种方式
# 通过key和value来进行遍历
for k, v in a.items():
    print("{}->{}".format(k, v))

# format格式字符串
z = "好难啊"
x = "是真的"
print("python",z)
print("python"+z)
print("python{}".format(z))
print("python{}{}".format(z,x))
print("{}python{}".format(z,x))

# while循环
# break：跳出循环
# continue：跳出单次循环
""" a = input("是否需要循环？0：不需要，1：需要：")
while a == "1":
    print("正在循环")
    break # 让条件不满足循环or使用break跳出循环
else:
    print("那我不循环了噢")

for a in range(10):
    if a == 5:
        print("执行了continue,跳出了第",a+1,"次循环")
        continue
    print("第{}次循环".format(a+1)) """

# 九九乘法表 for循环
# end可以实现不换行
for i in range(10):
    for j in range(1,i+1):
        print("{}x{}={}".format(i,j,i*j),end = " ")
    print()
print("——————————这是使用for循环的分割线——————————")

# 九九乘法表 while循环
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("{}x{}={}".format(i,j,i*j),end=" ")
        j = j+1
    print()
    i = i+1
    
# 给字典添加value值

db = {"username":"test","password":"test"}
print(db)



db["phone"]="123456"
print(db)
db["username"]="newtest"
print(db)

test = {"username":"testname","password":"testpassword","sex":"female"}
# 获取该字典的所有x.keys()
print("该字典的key值是：",test.keys())
# 获取该字典的所有x.values()
print("该字典的value值是：",test.values())
# 初始化定义一个数组list取名为newbox，用来装字典
newbox = []
# 使用for循环对字典进行遍历
for i in test:
    # 这步是将key值装入newbox中
    newbox.append(i)
    # 这步是将对应的values值装入newbox中
    newbox.append(test.get(i))
# 打印检查是否成功将字典中的数据转化成数组里 
print(newbox)

  

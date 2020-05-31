""" # 输入账号、密码、手机号跟邮箱
username = input("用户名：")
password = input("密码:")
phone = input("手机号：")
email = input("邮箱：")

# db模拟数据
db = {"username":"test","password":"test","phone":"13332165478","email":"test@163.com"}

# 判断用户名密码是否为空，手机号邮箱是否为空
if username == "" or password == "":
    print("用户名或密码不能为空")
    exit()
else:
    if phone == "" or email == "":
        print("请完善手机号与邮箱信息")
    else:
        # 若所有信息都填充完毕，则开始跟数据库中的数据进行对比
        if username != db.get("username"):
            # 如果用户名不存在，则添加到字典中，若value存
            db["username"]=username
            db["password"]=password
            db["phone"]=phone
            db["email"]=email
            print(db)
        else:
            print("该用户名已存在，注册失败") """

# 字典转换成列表
a = {"username":"123","password":"1234"}
print("原字典数据：",a) 

# 完成注册功能，并添加新用户
# ——————————答案——————————

# 注册功能
# 定义一个user数据
db = [{"username":"test","password":"test","phone":"————","email":"————"}]

# 输入用户名和密码
username=input("请输入用户名：")
password=input("请输入密码：")
phone=input("请输入手机号：")
email=input("请输入邮箱账号：")

# 判断用户名密码是否为空
if username == "" or password == "":
    print("用户名或密码不可为空，请重新输入")
    exit()
# 若不为空则判断用户名是否存在
else:
    for user in db:
        if user.get("username") == username:
            print("用户名已存在")
            exit()
    # 如何执行到这，说明db里面没有重复的用户名
    # 定义一个新的user数据记录当前进行注册的用户信息
    u = {"username":username,"password":password,"phone":phone,"email":email}
    # 使用append方法添加到db列表数据里
    db.append(u)
    print(db)

# 将字典转换成列表list
# ——————————答案——————————

a = {"username":"123","password":"1234"}
b = []
for i in a:
    b.append(i)
    b.append(a[i])
print("结果是：",b)




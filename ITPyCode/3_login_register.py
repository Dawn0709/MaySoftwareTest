# 1.输入用户名和密码

# 2.判断登录是否成功,若成功,打印登录成功

# 变量命名，能看懂
username = input("请输入用户名：")
password = input("请输入密码：")

# 对用户名密码进行判断
if username == "" or password == "":
    print("用户名或密码不能为空")
    exit()

# db的作用就是模拟数据
db = {"username":"test","password":"test"}

# 如何判断输入的账号密码跟db的密码一致
if username == db.get("username") and password == db.get("password"):
    print("登录成功")
else:
    print("登录失败")
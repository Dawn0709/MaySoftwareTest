# 导入
""" import time
time.sleep(1)

from selenium import webdriver """

# 1、声明方法
def add(a,b):
    sum = a + b
    print(sum)
    return sum


# 2、调用方法
c = add(1,2)

print("————————————这是一条分割线————————————")

# 练习：登录方法,成功返回true，错误返回false
def login(username, password):
    if username == "" or password == "":
        print("用户名或密码不能为空")
        exit()
    # db的作用就是模拟数据
    db = {"username":"test","password":"tpw"}

    # 判断输入的账号密码跟数据库中的账号密码是否一致
    if username == db.get("username") and password == db.get("password"):
        print("登陆成功")
        return True
    else:
        print("登录失败")
        return False

un = input("请输入用户名：")
pw = input("请输入密码：")
login(un,pw)

print(login(un,pw))
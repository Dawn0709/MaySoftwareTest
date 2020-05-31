




# 虚拟数据
db = [{"username":"liuyun","password":"test","age":18}]

""" 
方法：注册方法
参数：username，password
返回值：true：成功/false：失败
 """
def reg(username,password):
    # 判断用户名和密码
    if username == "" or password == "":
        print("用户名或密码不能为空")
        return False
    # 判断用户名是否已经存在
    for user in db:
        if user.get("username") == username:
            print("注册失败，用户名已存在")
            return False
    # 不存在对应的用户名，则将注册信息传入到user字典中
    user = {"username":username,"password":password,"age":18,"weight":50}
    # 将新注册的user数据传入到总用户db数组中
    db.append(user)
    print("注册成功")
    return True

# 调用方法
username = input("请输入用户名：")
password = input("请输入密码:")
reg(username,password)
print(db)
print(reg)


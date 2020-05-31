# 类的声明

# 类名首字母大写
class Person():
    # 个人信息
    # 成员变量，类里面的变量
    name = "张三"
    sex = "男"
    height = 180
    weight = 50
    # 构造方法：初始化成员变量
    def __init__(self, mz, xb, sg, tz):
        # 给成员变量赋值
        self.name = mz
        self.sex = xb
        self.height = sg
        self.weight = tz

    # 功能
    # self：固定写法，类本身的对象
    # 成员方法
    def eat(self):
        print("人能跑")
    def talk(self, msg):
        print("人能说话{}".format(msg))

# 如何去使用：实例化-实例化对象
# 加了构造方法后，需要传参
p = Person("李四","女",170,40)
print(p.name)
p.eat()
p.talk("u say what?")
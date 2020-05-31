class Father():
    name = "孩子他爹"
    rmb = 500
    def kuang(self):
        print("爹有矿")

# 类的继承：被继承的是父类，继承的是子类
# 子类中跟父类重名的变量或方法，叫重写
class Son(Father):
    name = "别人家的孩子"
    rmb = 5
    
    # 不通过重写调用父类的方法
    def ta_ba_de(self):
        super().kuang()

    # 重写调用父类的方法
    def kuang(self):
        print("被他儿子败光了")
    
# 子类可以使用父类的成员方法和属性
s = Son()
print(s.rmb)
# 通过子类中的super调用父类
s.ta_ba_de()
# 重写
s.kuang()
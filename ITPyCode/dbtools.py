""" 
pymysql操作mysql数据库
 """

 import pymysql

 class DBTool():
     def __init__(self, host="127.0.0.1",username="root",password="123456", db="test"):
        #  用成员变量来存放这些信息
        self.db = db
        self.host = host
        self.username = username
        self.password = password

    # 查询方法
    def query(self,sql):
        """ 
            名字：查询方法
            参数：sql，查询的sql语句
            返回值：成功返回结果，失败返回false
         """
        #  连接并且得到数据库的操作对象
        try:
            db = pymysql.connect(host=self.host, user=self.username, db=self.db)        
            cursor = db.cursor() # 获取游标        
            cursor.execute(sql) # 执行查询语句
            res = cursor.fetchall() # 获取查询结果
            db.close() # 关闭数据库连接
            return res
        except:
            return False


d = DBTool()
res = d.query("select from tbl_user")
    

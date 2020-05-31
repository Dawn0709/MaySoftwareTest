a = [1,2,3,4,5,6]

print(a[0])
print(a[1])
print(a[4])
print(a[5])


# 异常处理，若代码没报错就执行try里的语句，报错了就执行except里的语句
# 增加代码的健壮性：报错后也可以运行
# 执行顺序：try -> (报错-except/没报错-else) ->finally，else跟finally根据实际情况添加使用
try:
    # 对某代码不确认时，可对其进行一场处理，让其出现异常仍可使程序执行下去
    print(a[100])
except:
    print ("这个代码报错了")
else:
    print("并没有报错")
finally:
    print("最后执行以下这一步")

# 输入某年某月某日，计算这一天是这一年的第几天
y = int(input("请输入年份:"))
m = int(input("请输入月份:"))
d= int(input("请输入日:"))
days = [31,28,31,30,31,30,31,31,30,31,30,31]
# 首先判断年份是平年还是闰年
# 闰年法则：能被4且不能被100整除，能被400整除
if (y%4 == 0 and y%100 != 0 )or y%400 == 0:    
    days[1] = 29
print("每月的天数是：",days)
sum = 0
for i in range(m-1):
    sum = days[i]+sum
# 前面月份的天数加起来，再加当月的号数
sum = sum + d
print("{}月{}号是{}年的第{}天".format(m,d,y,sum))
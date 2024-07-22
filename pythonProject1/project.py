print(1+1);

days=['Monday','Tuesday'];
# 文本类型怎么写？双引号和单引号都一样
# word='这个星期的前两天是'
print(days);
# print(word,days)

# print输出
x="a"
y="b"
# 换行
print(x)
print(y)
print('------')
# 并列输出
print(x,y)

a=b=c=1
print(a,b,c)
# 同时给a,b,c赋值
a,b,c=1,2,"john"
print(a,b,c)

# python的五个数据类型
# numbers(数字) string(字符串)list(列表)tuple(元组) dictionary(字典)
# python四种不同数字类型 int(符号整型) long(长整型) float(浮点型) complex(复数)
# python字符串的取值：从左到右的索引从0开始逐渐变大，从右到左的索引从-1开始逐渐变小
s='abcdef'
# 输出从1到5的字符
print(s[1:5])
print(s[0])
# 输出从下标2开始的字符
print(s[2:])
# 加号（+）是字符串连接运算符，星号（*）是重复操作。
print(s+"TEST")
print(s*2)

# python数组
# 截取字符，头部为包括，尾部不包括[头部，尾部，步长]
# 数组用[]，元组用()，数组可定位下标去修改数组的值，元组不可修改值
letters=['a','b','c','d','e']
print(letters[0:3:1])
letters[0]='s'
print(letters)
tuple=('runoob',7.87,2.23)
# tuple[0]='s'
# print(tuple)

# python字典

# python运算符
# /为除数，%为取模即返回除法的余数，**为幂，返回x的y次幂

flag=False
name='showMeAi'
if name=='yi':
    flag=True;
    print('欢迎boss')
else:
    print('欢迎',name)

# while循环语句
numbers=[12,37,5,42,8,3]
even=[]
odd=[]
while len(numbers)>0:
    number=numbers.pop()
    if(number%2==0):
        even.append(number)
    else:
        odd.append(number)
print(even,odd)

# while循环语句＋continue语句
i=1
while i<10:
    i+=1
    if i%2!=0:
        continue
    print(i)

# 无限循环，需终止时使用快捷键ctrl+C
# var=1
# while var==1:
#     num=input("请输入数字：")
#     print("您输入的数字为",num)
# print("结束")

# 循环中的else语句
count = 0
while count < 5:
   print(count, "比5要小")
   count = count + 1
else:
   print(count, "不比5小")

# for循环语句
for letter in 'ShowMeAI':     # 第一个实例
   print("当前字母: %s" % letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print('当前水果: %s'% fruit)

# range：范围  range(len(fruits))在水果的长度内
fruits=['香蕉','苹果','葡萄']
for index in range(len(fruits)):
    print('当前水果:%s' %fruits[index])
print("完成")

# 循环使用else语句
for num in range(20,30):
    for i in range(2,num):
        if num%i==0:
            j=num/i
            print('%d等于%d*%d'%(num,i,j))
            break
    else:
            print('%d是一个质数'%num)

str='千里之行，始于足下'
print(str[2:7])

# score=int(input('分数:'))
# if score>=90:
#     print('优秀')
# elif score>=80:
#     print('好')
# elif score>=70:
#     print('良')
# elif score>=60:
#     print('及格')
# else:
#     print('你要努力了')

# 集合,当集合元素只有一个时，用一个括号；当集合元素有多个，用两个括号
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
# 集合a中包含而集合b中不包含的元素
print(a-b)
# 集合a或b中包含的所有元素
print(a|b)

# 列表['a','b'],元组(1,2) 集合set('asdfd')
company = set("Google")
print(company)
company1 = set(("Google", "ShowMeAI", "Taobao"))
print(company1)
company.add("Facebook","abc")
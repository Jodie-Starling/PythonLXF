print('hello\nworld') #换行
a=input('请输入你的名字：') #字符串类型
import random
b=random.randint(1,100) #随机整数
c=random.uniform(1,100) #随机浮点数
d=random.random() #0到1之间的随机浮点数
print(d)
e=10
e/=3 #自动类型转换，整数变成浮点数
print(e)
e%=3 #求余
s1='hello'
s2='world'
s3=s1+s2*2 #字符串拼接和复制
#for while 循环
#字符串取代，分离，拼接
a = a.replace('old_text', 'new_text')  # 字符串替换
a=string.split(separator, maxsplit)  #字符串分离，返回列表，最大分割次数默认-1，即不限次数
a=separator.join(iterable) #字符串拼接 返回字符串，与split互逆
a=b.capitalize()/title()/upper()/lower()/lstrip()/rstrip()/strip() 
#字符串可以索引
#列表也可以索引，可以无限嵌套
if i in a: #判断i是否在a中
    print('i在a中')
if i not in a: #判断i是否不在a中
    print('i不在a中')
a.append(x)/insert(i,x)/pop(i)/remove(x)/clear()
del a #删除列表
a.sort() #排序
#字符串不可以通过索引改值，不可变数据类型；列表可以通过索引改值，可变数据类型
#元组不可变数据类型，列表可变数据类型   
b=a.copy() #复制列表 a变b不变
b=a #浅拷贝，b和a指向同一块内存 a变b变
b=a[:] #深拷贝，b和a指向不同的内存
a.sort() #排序列表，返回None，直接修改原列表
a=sorted(a) #排序列表，返回新列表，不修改原列表，用a接收相当于更新原列表
#元组
#集合
#字典 键是不可变数据类型，值可以是任意数据类型
a.keys()/values()/items() #获取字典的键/值/键值对  键和值会返回在列表里，键值对会返回在元组组成的列表里
for k,v in a.items(): #遍历字典
    print(k,v)
#字典和集合都是{}包起来的
a={} #空字典
a=set() #空集合
#在函数内部修改全局变量的值,需要使用global关键字，只读取不需要
#元组拆包 函数返回值不只1个，用b=g()，用b来接收，b是一个元组，也可以拆包，b,c = g() #g()返回一个元组，b和c分别接收元组的第1个和第2个值
#不定长参数 *args,**kwargs 普通参数，默认参数(只要派到它，就覆盖)，不定长参数(包裹成元组或字典，位置参数)，关键字参数（包裹成字典，提到关键字就调用它）

#初始化
dict1 = dict()
dict2 = {}

dict3 = {"key":"value"}
dict4 = dict(key="value")

list = [("key","value")]
dict5 = dict(list)

dict6 = dict(zip('abc',[1, 2, 3]))

dict7 = dict.fromkeys(range(3),'x')

dict8 = {i:2*i for i in range(3)}


# 更新
dict1["key"] = "value"
dict1.update([("key",1)])
dict1.update({2:3})

# 查找
a = dict1['key']
b = dict1.get('3',3)

# 删除
dict1 = {'a':5,'b':5,'c':7}
del dict1['a']
dict1.pop('b')
dict1.popitem()
del dict1

# 清空
my_dict = {'a':5,'b':5,'c':7}
my_dict.clear()

# 复制，被复制的dict变动，复制后的dict不变
my_dict = {'a':5,'b':5,'c':7}
my_dict2 = my_dict.copy()
my_dict['a'] = 7
print(my_dict2)

my_dict = {'a':5,'b':5,'c':7}
# 键排序
dict1 = sorted(my_dict.items(),key=lambda x:x[0])

# 值排序，保留键
dict2 = sorted(my_dict.items(),key=lambda x:x[1],reverse=True)
print(dict2)

# 其他方法
my_dict = {'a':5,'b':5,'c':7}
print(type(my_dict))
print(isinstance(my_dict,dict))




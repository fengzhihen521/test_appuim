#读取yaml文件
import yaml #导入yaml

file = open('familyInfo.yaml') #打开文件
data = yaml.load(file) #将文件内容赋值

print(data) #打印

print(data['name'])
print(data['age'])

print(data['spouse'])#一起打印
print(data['spouse']['name'])#分别打印
print(data['spouse']['age'])

print(data['children'])#一起打印
print(data['children'][0]['name'])#分别打印
print(data['children'][0]['age'])
print(data['children'][1]['name'])
print(data['children'][1]['age'])

data['name']='lyp' #修改后打印
print(data['name'])
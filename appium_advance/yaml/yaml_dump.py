import yaml

slogan = ['welcome','to','51Z']
website = {'url':'www.51zxw.com'}

print(slogan)
print(website)

print(yaml.dump(slogan)) #使用yaml.dump将Python转换为yaml
print(yaml.dump(website))
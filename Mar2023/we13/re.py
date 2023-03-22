import re
print("afasfasdf")
s = '''
Nguyen 5 Hoai 7 Nam 2
'''
# i=re.findall(r'\d{1,5}', s)
# print (i)

pattern= "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
print("Nhap email")

user_input = input()

if(re.search(pattern, user_input)):
    print("valid email")
else:
    print("nam said not valid email")

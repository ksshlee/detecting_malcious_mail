d = {}
f = open('test.txt','r')

line = f.read().splitlines()
for data in line:
    (key,value) = data.split(" : ")
    d[key] = value


for flag in d.keys():
    if '2000-03-03 12:13:23' in d[flag]:
        print('yes! your flag is %s' %(flag))
        break


print(flag)
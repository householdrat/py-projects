'''
t = [[3-i for i in range (3)] for j in range (3)]
s = 0
for i in range (3):
    s += t[i][i]
print (s)
'''
'''
my_list = [1,2,3]
for v in range (len(my_list)):
    my_list.insert(1, my_list[v])
print (my_list)
'''
'''
z = 10
y = 0
x = y < z and z > y or y > z and z < y
print (x)
'''
'''
var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")
'''
'''
my_list = [3,1,-2]
print (my_list[my_list[-1]])
'''
'''
a= 1
b = 0
c = a & b 
d = a|b
e = a ^b
print (c+d+e)
'''
'''
my_list = [i for i in range(-1,2)]
print(len(my_list))
'''
'''
vals = [0,1,2]
vals.insert(0,1)
del vals [1]
print (vals)
'''
'''
i = 0
while i <= 3 :
    i += 2
    print ("*")
'''
'''
x = 1
x = x == x
print(x)
'''
'''
my_list_1 = [1,2,3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0,v)
print(my_list_2)
'''
'''
i=0
while i <= 5:
    i+=1
    if i%2==0:
        break
    print("*")
'''
'''
nums = [1,2,3]
vals = nums[-1:-2]
print(len(nums))
print(len(vals))
print(vals)
'''
'''
my_list =[1,2,3,4]
print(my_list[-3:-2])
'''

var = 1
while var < 10:
    print("#")
    var = var << 1

'''
for i in range(1):
    print("#")
else:
    print("#")
'''
'''
nums=[1,2,3]
vals = nums
del vals [1:2]
print(len(vals))
print(len(nums))
print(vals)
print(nums)
'''
'''
my_list = [[0,1,2,3]for i in range(2)]
print (my_list[2][0])
'''
#quiz
'''
i=2
while i >= 0:
    print("*")
    i -= 2
'''
'''
for i in range(-1,1):
    print("#")
'''
'''
z=10
y=0
x=z > y or z == y
print(x)
'''
'''
my_list = [3,1,-1]
my_list[-1]=my_list[-2]
print(my_list)
'''
'''
vals=[0,1,2]
vals[0], vals[1] = vals[1], vals[2]
print(len(vals), vals)
'''
'''
my_list = [0 for i in range(1,3)]
print(my_list)
'''
'''
my_list=[0,1,2,3]
x=1
for elem in my_list:
    x*= elem
print(x)
'''
l = []
z = []
for x in range(3):
    l.append(x)
    for x in range(1):
        z.append(l)
print(z)

# fazem a mesma coisa 
      
d =  [[x for x in range(3)]for z in range(3)]        
print(d)

# 
# f = []
# for x in range(3):
#     l2 =  [x for x in range(3)]
#     f.append(l2)
# 
# print(f)
# 
# 
# # print(l2)
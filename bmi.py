height = float(input('請問身高:')) #123123
weight = float(input('請問體重:'))
print('身高為:', height,'體重為:', weight)
bmi = float(weight / (height/100)**2)
print('你的bmi是:', bmi)

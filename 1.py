import models

y = './street.jpg'
x = models.detect(y)
num = 0
ps = 0
# print(x[0][6])
for i in range(len(x)):
    if (x[i][6] == 0):
        num += 1
if (num != 0):
    ps = 1
    print('People')
else:
    print('Nobody')
print(x)

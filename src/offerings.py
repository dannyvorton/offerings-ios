import math

gross_pay = 1006.21
pto_hours = 397

i = math.ceil(gross_pay)
t = math.ceil(i * .1)
f = math.ceil(i * .01)
m = math.ceil(i * .01)
h = math.ceil(i * .01)
pto = math.floor(pto_hours / 40)

print('Increase: $' + str(i))
print('Tithing: $' + str(t))
print('Fast Offerings: $' + str(f))
print('Mission: $' + str(m))
print('Humanitarian: $' + str(h))
print('PTO (weeks): ' + str(pto))

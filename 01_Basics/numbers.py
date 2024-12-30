x = 2
y = 3
z = 4
x+y
print(x+y)
print(x+y*z)
print((x+y)*z)

print('chai ' + 'aur ' + 'code')
print(x,y,z)
print(x+1,y*2)
print(x%z)
#print(2 ** 10000)

result = 1/3.0
print(result)

print(repr('chai'))
print(str('chai'))
print('chai')

print(5.0 == 5.0)
print(4.0 != 5.0)
print(5.0 is 5.0)
print(x<y and y>z)
print(x<y and y<z)
print(x<y or y>z)
print(x<y or y<z)
print(1 == 2 < 3)

print('---')
import math
print(math.floor(3.5))  # floor --> it looks for bottom value
print(math.floor(-3.5))
print(math.trunc(-2.8)) # trunc --> it looks for 0
print(9999999999999999 + 2)

print( (2+1j) * 3 )

print(0o20) # 16
print(0xFF) # 255
print(0b1000) # 8
print(oct(64))
print(hex(64))
print(bin(64))
print(int('64', 8))

b = 1
print(b << 2)


# ----->>>  move from basics

import random 
print(random.random())
print(random.randint(1,100))

l1 = ['lemon', 'masala', 'ginger', 'mint']
print(random.choice(l1))

random.shuffle(l1)
print(l1)

print(0.1 + 0.1 + 0.4)
print((0.1 + 0.1 + 0.1) - 0.3)
# from decimal import Decimal           
# print(Decimal('0.1') + Decimal(0.1) + Decimal(0.1))


# ------->> SET

setone = {1,2,3,4,5}
print(setone)

# & for intersection
# | for union
# - for difference


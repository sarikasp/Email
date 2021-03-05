# # split breaks the string on given parameter and return list
# flowers = 'lotus jasmine sunflower rose lily marygold'
# flowerList = flowers.split('')
# print(type(flowerList))
# print(flowerList)

# flower = 'Orchid Lily Rose Jasmine Aster'
# print(flower)
# flowersList = flower.split()
# print(flowersList)
#
# print(flower.split(', ', 0))
flw = 'Orchid, Lily, Rose, Jasmine, Aster'
# print(flw.split(', ', 2))
print(flw.split(',', 4))
z = flw.split(',', 4)
for i in z:
    print(i)



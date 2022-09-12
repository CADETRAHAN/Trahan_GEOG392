product = 1
sum = 0
sumeven = 0
part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
for n in part1:
    product *= n
part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
for n in part2:
    sum += n
part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21] 
for n in part3:
    if n % 2 == 0:
        sumeven += n
    else:
        pass
print(product)
print(sum)
print(sumeven)
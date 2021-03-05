"""
このファイルに解答コードを書いてください
"""
file = open("input.txt")
data = file.read()
new_list = []
with open("input.txt") as file:
    for l in file:
        new_list.append(l[:-1])

# data_wash for store the processing data
data_wash = []
for nums in new_list:
    data_wash.append(nums.split(":"))

N = len(data_wash)
for item in data_wash:
    item[0] = int(item[0])

# count for the situation that if no output
count = 0
m = data_wash[-1][0]
for i in range(N-1):
    if m%data_wash[i][0] == 0:
        count += 1
        print(data_wash[i][1])

# if no output then print m
if count == 0:
    print(m)


# print(data_wash)



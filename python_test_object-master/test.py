"""
このファイルに解答コードを書いてください
"""

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


m = data_wash[-1][0]

# remove m
data_wash = data_wash[:-1]

# sorting data_wash for sはiの小さい順に出力してください(
data_wash = sorted(data_wash, key=lambda data: data[0])
# print(data_wash)
res = ""
for i in range(N-1):
    if m%data_wash[i][0] == 0:
        res += data_wash[i][1]

print(res) if res else print(m)


# print(data_wash)



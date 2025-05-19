# n=5
# 15
# 7  14
# 6  8  13
# 2  5  9  12
# 1  3  4  10  11

n = 5
numbers = [15,14,13,12,11]
left_numbers = [[], [7], [6,8], [2,5,9], [1,3,4,10]]

for i in range(n):
    for num in left_numbers[i]:
        print(num, "", end="")
    print(numbers[i])
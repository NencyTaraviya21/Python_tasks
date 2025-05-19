# n=4
# 10
# 4  9
# 3  5  8
# 1  2  6  7


n = 4
numbers = [10, 9, 8, 7]
left_numbers = [[], [4], [3,5], [1,2,6]]

for i in range(n):
    for num in left_numbers[i]:
        print(num, "", end="")
    print(numbers[i])
def pattern_righttri_fliped(n):
    num = n * (n + 1) // 2 

    for i in range(1, n + 1):
        row = []
        for j in range(i):
            row.append(num)
            num -= 1
        if i % 2 == 0: 
            row = reversed(row)
        spaces = '   ' * (n - i)
        print(spaces + ' '.join(f"{x:2}" for x in row))

# x = 5
# print(f"{x:2}")   # prints: " 5"

pattern_righttri_fliped(4)
pattern_righttri_fliped(5)
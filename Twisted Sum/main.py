def compute_sum(n):
    result = 0

    for x in range(n):
        x += 1

        if x > 9:
            for i in str(x):
                result += int(i)
        else:
            result += x

    return result

print(compute_sum(1), "->", 1)
print(compute_sum(2), "->", 3)
print(compute_sum(3), "->", 6)
print(compute_sum(4), "->", 10)
print(compute_sum(10), "->", 46)
print(compute_sum(12), "->", 51)
def max(*num):
    if len(num) == 0 :
        return None
    max_num = num[0]
    for numbers in num:
        if numbers > max_num:
             max_num = numbers
    return max_num

print(max(12,13,1,11,45,6))
    
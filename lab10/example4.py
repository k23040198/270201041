def sum_of_a_nested_list(num):
    if type(num)!= type([]):
        return num
    else:
        sum = 0
        for i in num:
            sum += sum_of_a_nested_list(i)
        return sum

print(sum_of_a_nested_list([3, 12, 76, [4, 56, 43], [2, 8], 1500, 75]))